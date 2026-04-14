import requests
from bs4 import BeautifulSoup
from urllib.parse import urlparse, urljoin
from collections import deque
import logging

def get_seo_data(base_url, max_pages=50, check_broken_links=False):
    """
    Single-pass crawl: extracts SEO titles and optionally checks for broken internal links.
    Returns: (results, broken_links) — broken_links is empty list if check_broken_links=False
    """
    domain = urlparse(base_url).netloc
    to_visit = deque([base_url])
    visited = set()
    results = []
    link_map = []  # (source_page, target_url) pairs collected during crawl

    ignored_folders = ('/blog/', '/neighborhoods/', '/developments/', '/properties/', '/agent/', '/agents/')
    allowed_exceptions = ('/properties/sale', '/properties/sold')
    headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64)'}

    # --- Single crawl pass ---
    while to_visit and len(visited) < max_pages:
        current_url = to_visit.popleft()
        if current_url in visited:
            continue
        visited.add(current_url)

        try:
            response = requests.get(current_url, headers=headers, timeout=10)
            if response.status_code != 200 or 'text/html' not in response.headers.get('Content-Type', ''):
                continue

            soup = BeautifulSoup(response.text, 'html.parser')

            # Extract SEO title
            title_tag = soup.find('title')
            title_text = title_tag.text.strip() if title_tag else "No Title Found"
            results.append({'url': current_url, 'title': title_text, 'length': len(title_text)})

            # Link discovery
            for link in soup.find_all('a', href=True):
                absolute_url = urljoin(base_url, link['href']).split('#')[0].rstrip('/')
                url_path = urlparse(absolute_url).path.rstrip('/')

                if urlparse(absolute_url).netloc != domain:
                    continue

                is_exception = any(url_path == p.rstrip('/') for p in allowed_exceptions)
                is_ignored = any(url_path.startswith(c) for c in ignored_folders)

                # Collect ALL internal links for broken check, regardless of crawl filter
                if check_broken_links:
                    link_map.append((current_url, absolute_url))

                if is_exception or not is_ignored:
                    if absolute_url not in visited and absolute_url not in to_visit:
                        to_visit.append(absolute_url)
        except Exception:
            continue

    # --- Broken link check (only if enabled) ---
    broken_links = []
    if check_broken_links:
        try:
            excluded_links = ['/cdn-cgi/l/email-protection']
            link_sources = {}

            for source, target in link_map:
                if any(exc in target for exc in excluded_links):
                    continue
                if target not in link_sources:
                    link_sources[target] = []
                if source not in link_sources[target]:
                    link_sources[target].append(source)

            for target, sources in link_sources.items():
                try:
                    r = requests.get(target, headers=headers, timeout=5, allow_redirects=True, stream=True)
                    final_url = r.url
                    status = r.status_code

                    is_soft_404 = (
                        status == 200 and (
                            "404" in r.text[:5000]
                            or "not found" in r.text[:5000].lower()
                            or "page not found" in r.text[:5000].lower()
                        )
                    )
                    r.close()

                    if status == 404 or is_soft_404:
                        label = f"{status} (soft)" if is_soft_404 else str(status)
                        for source in sources:
                            broken_links.append({'Page': source, 'Broken Link': target, 'Status': label})

                except requests.exceptions.ConnectionError:
                    for source in sources:
                        broken_links.append({'Page': source, 'Broken Link': target, 'Status': 'Connection Error'})
                except requests.exceptions.Timeout:
                    for source in sources:
                        broken_links.append({'Page': source, 'Broken Link': target, 'Status': 'Timeout'})
                except requests.exceptions.TooManyRedirects:
                    for source in sources:
                        broken_links.append({'Page': source, 'Broken Link': target, 'Status': 'Redirect Loop'})
                except Exception as e:
                    for source in sources:
                        broken_links.append({'Page': source, 'Broken Link': target, 'Status': f'Error: {str(e)[:30]}'})

        except Exception as e:
            logging.error(f"Broken link check failed: {e}")

    return results, broken_links