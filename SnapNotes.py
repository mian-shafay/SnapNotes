import streamlit as st
from document_parser import parse_pdf, parse_pptx
from note_maker import generate_notes

st.set_page_config(page_title="SnapNotes", layout="wide")

st.title("📄 SnapNotes")
st.markdown("Upload multiple PDF and PPTX files. The AI will read them, preserve the exact headings, and generate concise notes under each heading.")

uploaded_files = st.file_uploader(
    "Choose PDF or PPTX files", 
    type=["pdf", "pptx"], 
    accept_multiple_files=True
)

if uploaded_files:
    if st.button("Generate Notes"):
        for uploaded_file in uploaded_files:
            file_name = uploaded_file.name
            file_bytes = uploaded_file.read()
            
            st.subheader(f"Processing: {file_name}...")
            
            try:
                with st.spinner(f"Extracting text from {file_name}..."):
                    if file_name.endswith(".pdf"):
                        md_text = parse_pdf(file_bytes)
                    elif file_name.endswith(".pptx"):
                        md_text = parse_pptx(file_bytes)
                    else:
                        st.error("Unsupported file type.")
                        continue
                
                with st.spinner("Analyzing and Generating Notes (this may take a bit)..."):
                    notes = generate_notes(md_text)
                
                with st.expander(f"📝 Notes for {file_name}", expanded=True):
                    st.markdown(notes)
                    
                st.download_button(
                    label=f"Download {file_name} Notes",
                    data=notes,
                    file_name=f"{file_name}_notes.md",
                    mime="text/markdown"
                )
                
            except ValueError as ve:
                st.error(str(ve))
                break
            except Exception as e:
                st.error(f"Error processing {file_name}: {e}")

st.sidebar.title("Setup Instructions")
st.sidebar.markdown("""
1. Go to your project folder
2. Add your `GROQ_API_KEY` in the `.env` file.
3. Run `.\\venv\\Scripts\\python run.py`
""")
