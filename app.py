import streamlit as st
from extractor import extract_text
from analyzer import analyze_document

st.set_page_config(page_title="AI Document Engine", layout="wide")

st.title("📄 AI Document Intelligence Engine")

uploaded_file = st.file_uploader(
    "Upload PDF / Image",
    type=["pdf", "png", "jpg", "jpeg"]
)

if uploaded_file:

    st.success("✅ File Uploaded")

    # Extract text
    with st.spinner("Extracting text..."):
        text = extract_text(uploaded_file)

    st.subheader("📜 Extracted Text")
    st.text_area("", text[:2000], height=200)

    # AI Analysis
    with st.spinner("Analyzing document..."):
        result = analyze_document(text)   # ✅ FIXED

    st.subheader("🧠 AI Output")
    st.code(result, language="json")