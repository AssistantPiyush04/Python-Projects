import streamlit as st
from PyPDF2 import PdfReader
    
st.title("PDF File Extractor")

upload_file=st.file_uploader("Upload your file",type=['pdf'])

if upload_file is not None:
    
    reader=PdfReader(upload_file)
    text = ""
    
    for page in reader.pages:
         
         text += page.extract_text()

    st.subheader("Extract text")

    st.text_area("Pdf text",text,height=460)