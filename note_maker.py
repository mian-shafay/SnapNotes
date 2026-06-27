import os
from groq import Groq
from dotenv import load_dotenv

load_dotenv()

def generate_notes(md_text: str) -> str:
    """Takes markdown text and summarizes it while preserving original headings."""
    api_key = os.getenv("GROQ_API_KEY")
    if not api_key or api_key == "your_groq_api_key_here":
        raise ValueError("Please set a valid GROQ_API_KEY in your .env file.")

    client = Groq(api_key=api_key)

    prompt = f"""
You are an expert note-taking assistant.
I will provide you with markdown text extracted from a document.

Your task is to summarize the content into clean, concise notes.

CRITICAL INSTRUCTIONS:
1. You MUST preserve the exact markdown headings (e.g., # Heading, ## Subheading) exactly as they appear in the original text.
2. Under each heading, provide a concise summary or key takeaways of the content using bullet points.
3. Use very simple, easy-to-understand wording (avoid overly complex jargon).
4. Provide clear, relatable examples to explain the concepts.
5. Remove any fluff or redundant information, but keep key metrics and facts.
6. Output proper Markdown format.

Document Text:
{md_text}
"""
    
    # We use llama-3.1-8b-instant or mixtral-8x7b-32768 from Groq as it's extremely fast and capable
    response = client.chat.completions.create(
        model="llama-3.1-8b-instant",
        messages=[
            {"role": "system", "content": "You are a professional summarizer and note taker."},
            {"role": "user", "content": prompt}
        ],
        temperature=0.3
    )
    
    return response.choices[0].message.content or ""
