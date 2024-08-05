import streamlit as st

from rag import query_gemini





st.title('Simple Rag App For The Lord of the Rings')

question = st.text_input("Ask a question:")

uploaded_file = st.file_uploader("Upload a file (optional):", type=["txt"])

if uploaded_file is not None:
    # Read the content of the file
    file_content = uploaded_file.getvalue().decode("utf-8", errors="ignore")
else:
    file_content = None

response = query_gemini(question, file_content)

#return the response to the user
st.write(response)




