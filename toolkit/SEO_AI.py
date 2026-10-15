import os
import json
import logging
from datetime import date
from dotenv import load_dotenv
from google import genai 

# Configure logging
logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s - %(levelname)s - %(message)s"
)

load_dotenv()
api_key = os.getenv("GEMINI_API_KEY")
gemini_model = "gemini-3.8-flash"

SEO_title_context ="""
## Role
You are an expert real estate SEO specialist with deep knowledge of search engine optimization for real estate websites.
Your only job is to generate SEO titles for real estate agent and team pages.

## SEO Title Rules
- Length: strictly between 40 and 60 characters (count every character including spaces and pipes)
- Include the page context, agent/team name, and location
- Use pipes (|) as natural separators between elements
- Never use quotes, explanations, or extra text in the output

## Examples
-input: Featured Properties, Brittany Carney, Gainesville
-title: Gainesville, FL Homes for Sale | Brittany Carney

-input: About, Kim Bock Wilson, Parkersburg
-title: Kim Bock Wilson | Parkersburg, WV Real Estate Agent

-input: Contact, Claire Hanssen, Santa Ynez Valley
-title: Contact Claire Hanssen | Pickford Real Estate Agent

-input: Testimonials, Claire Hanssen, Santa Ynez Valley
-title: Client Testimonials | Santa Ynez Valley | Claire Hanssen

-input: Mortgage Calculator, Peter McFarren, Charlottesville
-title: Charlottesville Mortgage Calculator | Peter McFarren

## Task
When given an input in the format: Page Name, Agent/Team Name, Location
- return ONLY the SEO title, nothing else
- Follow the style and structure of the provided examples strictly
- Strictly follow the SEO title rules above
"""
SEO_description_context ="""
## Role
You are an expert real estate SEO specialist with deep knowledge of search engine optimization for real estate websites.
Your only job is to generate meta descriptions for real estate agent and team pages.

## Meta Description Rules
- Length: strictly between 120 and 158 characters (count every character including spaces)
- Mention the agent/team name and location naturally
- Tone: professional, compelling, and human — never robotic
- Never use quotes, explanations, or extra text in the output

## Examples
-input: Featured Properties, Brittany Carney, Gainesville
-description: Explore Brittany Carney's Gainesville, FL property listings, featuring homes for sale and past sales showcasing her expertise in meeting diverse client needs.

-input: About, Kim Bock Wilson, Parkersburg
-description: Meet Kim Bock Wilson, a trusted Parkersburg, WV real estate agent known for personalized service. Contact her today to buy or sell your home with confidence.

-input: Contact, Claire Hanssen, Santa Ynez Valley
-description: Contact Claire Hanssen of Pickford Real Estate to discuss buying, selling, or renting homes in the Santa Ynez Valley. Schedule your consultation today.

-input: Testimonials, Claire Hanssen, Santa Ynez Valley
-description: Read what clients say about their positive experiences working with Claire Hanssen for their real estate needs in the Santa Ynez Valley. Get genuine feedback.

-input: Mortgage Calculator, Peter McFarren, Charlottesville
-description: Use Peter McFarren's mortgage calculator to estimate monthly payments for your Charlottesville, VA home purchase. Explore your options and contact him today!

## Task
When given an input in the format: Page Name, Agent/Team Name, Location
- return ONLY the meta description, nothing else
- Follow the style and structure of the provided examples strictly
- Strictly follow the Meta Description Rules above
"""
TOKEN_LIMIT = 1000  # Daily limit per token type

TOKENS_FILE = os.path.join(os.path.dirname(os.path.abspath(__file__)), '..', 'data', 'tokens_records.json')

def check_token_limit(input_tokens=0, output_tokens=0):
    try:
        with open(TOKENS_FILE, "r", encoding="utf-8") as f:
            tokens_data = json.load(f)
    except (FileNotFoundError, json.JSONDecodeError):
        tokens_data = {}

    today = str(date.today())
    if today not in tokens_data:
        tokens_data[today] = {"input_tokens": 0, "output_tokens": 0}

    tokens_data[today]["input_tokens"] += input_tokens
    tokens_data[today]["output_tokens"] += output_tokens

    with open(TOKENS_FILE, "w", encoding="utf-8") as f:
        json.dump(tokens_data, f, indent=4, ensure_ascii=False)

    logging.info(
        f"Input tokens today: {tokens_data[today]['input_tokens']} | "
        f"Output tokens today: {tokens_data[today]['output_tokens']}"
    )

    if tokens_data[today]["input_tokens"] > TOKEN_LIMIT or tokens_data[today]["output_tokens"] > TOKEN_LIMIT:
        logging.warning("Daily token limit exceeded.")
        return False

    return True


def generate_seo_title_v2(page_name: str, agent_name: str, location: str) -> str:
    if not check_token_limit():
        return "Daily AI limit reached. Please try again tomorrow."

    client = genai.Client(api_key=api_key)

    try:
        response = client.models.generate_content(
            model=gemini_model,
            contents=f"{SEO_title_context}\n\nGenerate a SEO title for: {page_name}, {agent_name}, {location}",
            )

        input_tokens = response.usage_metadata.prompt_token_count
        output_tokens = response.usage_metadata.candidates_token_count
        check_token_limit(input_tokens, output_tokens)

        return response.text.strip().strip('"')

    except Exception as e:
        logging.error(f"Error generating SEO title: {e}")
        return "⚠️ Could not generate content. Please try again later." 


def generate_seo_description(page_name: str, agent_name: str, location: str) -> str:
    
    if not check_token_limit():
            return "Daily AI limit reached. Please try again tomorrow."

    client = genai.Client(api_key=api_key)
    
    try:
        response = client.models.generate_content(
            model=gemini_model,
            contents=f"{SEO_description_context}\n\nGenerate a meta description for: {page_name}, {agent_name}, {location}",
            )

        input_tokens = response.usage_metadata.prompt_token_count
        output_tokens = response.usage_metadata.candidates_token_count
        check_token_limit(input_tokens, output_tokens)

        return response.text.strip().strip('"')

    except Exception as e:
        logging.error(f"Error generating SEO description: {e}")
        return "⚠️ Could not generate content. Please try again later."   