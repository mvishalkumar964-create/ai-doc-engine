import streamlit as st
from extractor import extract_text
from analyzer import analyze_document

st.set_page_config(page_title="AI Document Engine", layout="wide")

st.title("📄 AI Document Intelligence Engine")

# Upload file
uploaded_file = st.file_uploader("Upload PDF / Image", type=["pdf", "png", "jpg", "jpeg"])

if uploaded_file is not None:
    st.success("✅ File Uploaded")

    # Extract text
    text = extract_text(uploaded_file)

    st.subheader("📜 Extracted Text")
    st.text_area("", text, height=200)

    # ✅ TEXT LIMIT (IMPORTANT FIX)
    short_text = text[:1000]

    # Analyze with spinner
    st.subheader("🧠 AI Output")

    with st.spinner("⚡ AI is analyzing... Please wait"):
        result = analyze_document(short_text)

    # Show result
    st.code(result, language="json")
