import os
import google.generativeai as genai

genai.configure(api_key=os.getenv("GOOGLE_API_KEY"))

model = genai.GenerativeModel("gemini-pro")

def analyze_document(text):

    prompt = f"""
    You are an AI document analyzer.

    Step 1: Detect document type (invoice / academic / other)

    Step 2:
    - If invoice → extract:
        vendor, amount, date
    - If academic → give summary
    - Else → give key insights

    Return response in JSON format.

    TEXT:
    {text}
    """

    response = model.generate_content(prompt)

    return response.text