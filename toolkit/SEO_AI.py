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

TOKEN_LIMIT = 1000  # Daily limit per token type

def check_token_limit(input_tokens=0, output_tokens=0):
    try:
        with open("../data/tokens_records.json", "r", encoding="utf-8") as f:
            tokens_data = json.load(f)
    except (FileNotFoundError, json.JSONDecodeError):
        tokens_data = {}

    today = str(date.today())
    if today not in tokens_data:
        tokens_data[today] = {"input_tokens": 0, "output_tokens": 0}

    tokens_data[today]["input_tokens"] += input_tokens
    tokens_data[today]["output_tokens"] += output_tokens

    with open("../data/tokens_records.json", "w", encoding="utf-8") as f:
        json.dump(tokens_data, f, indent=4, ensure_ascii=False)

    logging.info(
        f"Input tokens today: {tokens_data[today]['input_tokens']} | "
        f"Output tokens today: {tokens_data[today]['output_tokens']}"
    )

    if tokens_data[today]["input_tokens"] > TOKEN_LIMIT or tokens_data[today]["output_tokens"] > TOKEN_LIMIT:
        logging.warning("Daily token limit exceeded.")
        return False

    return True


def generate_seo_title(current_title=""):
    api_key = os.getenv("GEMINI_API_KEY")
    if not api_key:
        raise ValueError("Gemini API key not found. Check your .env file.")

    if not check_token_limit():
        return "Daily AI limit reached. Please try again tomorrow."

    genai.configure(api_key=api_key)
    model = genai.GenerativeModel("gemini-2.5-flash")

    context = """You are an expert real estate SEO specialist.
    Your only job is to generate optimized SEO titles for real estate website pages.
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