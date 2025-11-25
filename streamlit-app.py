import PyPDF2
import google.generativeai as genai
import streamlit as st

# -----------------------------
# Configure Gemini API Key
# -----------------------------
genai.configure(api_key="AIzaSyCe7Hv1CWDioVyWI7nnWx7-sGBwukIW6kg")   # put your valid key here

# -----------------------------
# Extract Text From PDF
# -----------------------------
def extract_text_from_pdf(pdf_file):
    text = ""
    reader = PyPDF2.PdfReader(pdf_file)
    for page in reader.pages:
        extracted = page.extract_text()
        if extracted:
            text += extracted + "\n"
    return text

# -----------------------------
# Ask Question Using Gemini
# -----------------------------
def ask_question_from_pdf(pdf_text, question):
    model = genai.GenerativeModel("models/gemini-2.5-flash")   # ✅ correct working model

    prompt = f"""
Use ONLY the content in the PDF to answer the question.

Document:
{pdf_text}

Question:
{question}

Answer:
"""

    response = model.generate_content(prompt)
    return response.text

# -----------------------------
# Streamlit UI
# -----------------------------
st.title("📄 PDF Question-Answering App")

uploaded_file = st.file_uploader("Upload a PDF document", type="pdf")

if uploaded_file:
    with st.spinner("Extracting text..."):
        pdf_text = extract_text_from_pdf(uploaded_file)

    st.success("PDF text extracted!")

    question = st.text_input("Ask something about the PDF:")

    if st.button("Get Answer") and question.strip():
        with st.spinner("Generating answer..."):
            answer = ask_question_from_pdf(pdf_text, question)

        st.write("### Answer:")
        st.write(answer)
