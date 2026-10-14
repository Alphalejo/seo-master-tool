import os
import json
import logging
from datetime import date
from dotenv import load_dotenv
import google.generativeai as genai

# Configure logging
logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s - %(levelname)s - %(message)s"
)

load_dotenv()

context = SYSTEM_CONTEXT = """
## Role
You are an expert real estate SEO specialist with deep knowledge of search engine optimization for real estate websites.
Your only job is to generate SEO titles and meta descriptions for real estate agent and team pages.

## SEO Title Rules
- Length: strictly between 40 and 60 characters (count every character including spaces and pipes)
- Always include the page context, agent/team name, and location
- Use pipes (|) as natural separators between elements
- Never use quotes, explanations, or extra text in the output

## Meta Description Rules
- Length: strictly between 120 and 158 characters (count every character including spaces)
- Mention the agent/team name and location naturally
- Tone: professional, compelling, and human — never robotic
- Never use quotes, explanations, or extra text in the output

## Examples
input: Featured Properties, Brittany Carney, Gainesville
title: "Gainesville, FL Homes for Sale | Brittany Carney"
description: "Explore Brittany Carney's Gainesville, FL property listings, featuring homes for sale and past sales showcasing her expertise in meeting diverse client needs."

input: About, Kim Bock Wilson, Parkersburg
title: "Kim Bock Wilson | Parkersburg, WV Real Estate Agent"
description: "Meet Kim Bock Wilson, a trusted Parkersburg, WV real estate agent known for personalized service. Contact her today to buy or sell your home with confidence."

input: Contact, Claire Hanssen, Santa Ynez Valley
title: "Contact Claire Hanssen | Pickford Real Estate Agent"
description: "Contact Claire Hanssen of Pickford Real Estate to discuss buying, selling, or renting homes in the Santa Ynez Valley. Schedule your consultation today."

input: Testimonials, Claire Hanssen, Santa Ynez Valley
title: "Client Testimonials | Santa Ynez Valley | Claire Hanssen"
description: "Read what clients say about their positive experiences working with Claire Hanssen for their real estate needs in the Santa Ynez Valley. Get genuine feedback."

input: Mortgage Calculator, Peter McFarren, Charlottesville
title: "Charlottesville Mortgage Calculator | Peter McFarren"
description: "Use Peter McFarren's mortgage calculator to estimate monthly payments for your Charlottesville, VA home purchase. Explore your options and contact him today!"

## Task
When given an input in the format: Page Name, Agent/Team Name, Location
- If asked for a title: return ONLY the SEO title, nothing else
- If asked for a description: return ONLY the meta description, nothing else
- Follow the style and structure of the provided examples strictly
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

def connect_to_gemini():
    client = genai.Client()

    cache = client.caches.create(
        model='gemini-3.8-flash',
        contents= context
    )

def generate_seo_title(current_title=""):
    api_key = os.getenv("GEMINI_API_KEY")
    if not api_key:
        raise ValueError("Gemini API key not found. Check your .env file.")

    if not check_token_limit():
        return "Daily AI limit reached. Please try again tomorrow."

    genai.configure(api_key=api_key)
    model = genai.GenerativeModel("gemini-2.5-flash")

    context = """You are an expert luxury real estate SEO specialist.
    Your only job is to generate optimized SEO titles for luxury real estate website pages.
    Rules:
    - Length: strictly between 45 and 60 characters (count carefully)
    - Deduce the page name, client/brokerage name, and location from the current title provided
    - Tone: professional, clear, and compelling
    - Return ONLY the title, no explanations, no quotes, no extra text
    """

    chat = model.start_chat(history=[
        {"role": "user", "parts": [context]}
    ])

    prompt = f"""Generate an optimized SEO title based on this current title (extract all context from it): {current_title}
    """

    try:
        response = chat.send_message(prompt)

        input_tokens = response.usage_metadata.prompt_token_count
        output_tokens = response.usage_metadata.candidates_token_count
        check_token_limit(input_tokens, output_tokens)

        logging.info(f"SEO title generated. Tokens used — input: {input_tokens}, output: {output_tokens}")
        return response.text.strip()

    except Exception as e:
        logging.error(f"Error generating SEO title: {e}")
        raise


def generate_seo_title_v2(page_name: str, agent_name: str, location: str) -> str:
    if not check_token_limit():
        return "Daily AI limit reached. Please try again tomorrow."

    genai.configure(api_key=os.getenv("GEMINI_API_KEY"))
    model = genai.GenerativeModel("gemini-2.5-flash")

    context = f"""You are an expert real estate SEO specialist.
    Generate ONLY an SEO title — no quotes, no explanation, no extra text.
    Rules:
    - Strictly between 40 and 60 characters (count every character including spaces and pipes)
    - Follow the style from these examples:
    {FEW_SHOT_EXAMPLES}
    - Include location, page context, and agent/team name
    - Use pipes (|) as separators when needed
    """

    chat = model.start_chat(history=[{"role": "user", "parts": [context]}])
    prompt = f"input: {page_name}, {agent_name}, {location}"

    try:
        response = chat.send_message(prompt)
        input_tokens = response.usage_metadata.prompt_token_count
        output_tokens = response.usage_metadata.candidates_token_count
        check_token_limit(input_tokens, output_tokens)
        return response.text.strip().strip('"')
    except Exception as e:
        logging.error(f"Error generating SEO content: {e}")
        return "⚠️ Could not generate content. Please try again later."


def generate_seo_description(page_name: str, agent_name: str, location: str) -> str:
    if not check_token_limit():
        return "Daily AI limit reached. Please try again tomorrow."

    genai.configure(api_key=os.getenv("GEMINI_API_KEY"))
    model = genai.GenerativeModel("gemini-2.5-flash")

    context = f"""You are an expert real estate SEO specialist.
    Generate ONLY a meta description — no quotes, no explanation, no extra text.
    Rules:
    - Strictly between 120 and 158 characters (count every character including spaces)
    - Follow the style and tone from these examples:
    {FEW_SHOT_EXAMPLES}
    - Include a call to action, location context, and agent/team name
    - Natural, compelling, professional tone
    """

    chat = model.start_chat(history=[{"role": "user", "parts": [context]}])
    prompt = f"input: {page_name}, {agent_name}, {location}"

    try:
        response = chat.send_message(prompt)
        input_tokens = response.usage_metadata.prompt_token_count
        output_tokens = response.usage_metadata.candidates_token_count
        check_token_limit(input_tokens, output_tokens)
        return response.text.strip().strip('"')
    except Exception as e:
        logging.error(f"Error generating SEO content: {e}")
        return "⚠️ Could not generate content. Please try again later."    