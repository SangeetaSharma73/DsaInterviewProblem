import fitz  # PyMuPDF for PDF extraction
import openai
import textwrap

# Set your OpenAI API Key
OPENAI_API_KEY = "your_openai_api_key_here"
openai.api_key = OPENAI_API_KEY

def extract_text_from_pdf(pdf_path):
    """Extracts text from a given PDF file."""
    doc = fitz.open(pdf_path)
    text = "\n".join([page.get_text("text") for page in doc])
    return text

def chunk_text(text, max_length=4000):
    """Splits text into chunks within the token limit."""
    return textwrap.wrap(text, max_length)

def summarize_text_gpt(text):
    """Summarizes the text using OpenAI's GPT model."""
    prompt = ("Extract key information for an investor from the following document. "
              "Focus on future growth prospects, key changes in business, key triggers, "
              "and material effects on next year's earnings and growth.\n\n" + text)
    
    response = openai.ChatCompletion.create(
        model="gpt-4",  # Use GPT-4 for better summarization
        messages=[{"role": "system", "content": "You are a financial analyst."},
                  {"role": "user", "content": prompt}],
        temperature=0.3,
    )
    
    return response["choices"][0]["message"]["content"].strip()

def process_pdf_for_investors(pdf_path):
    """Extracts key investor insights from a given PDF file."""
    text = extract_text_from_pdf(pdf_path)
    chunks = chunk_text(text)
    
    summary_parts = [summarize_text_gpt(chunk) for chunk in chunks]
    full_summary = "\n\n".join(summary_parts)
    
    return full_summary

if __name__ == "__main__":
    pdf_path = "C:\Users\user\Downloads\SJS Transcript Call.pdf"  # Change this to the actual PDF path
    summary = process_pdf_for_investors(pdf_path)
    print("\n=== Investor Summary ===\n")
    print(summary)
