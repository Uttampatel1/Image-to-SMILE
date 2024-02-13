import os
import streamlit as st
from PIL import Image
from io import BytesIO
import tempfile


# Initialize 'key' in session state if not already initialized
if 'key' not in st.session_state:
    st.session_state['key'] = 'value'

# Function to predict SMILES
def predict_smiles(image_path):
    if st.session_state['key'] == 'value':
        from DECIMER import predict_SMILES
        st.session_state['key'] = 'loaded'
    
    SMILES = predict_SMILES(image_path)
    return SMILES
# Main function for Streamlit app
def main():
    st.title("SMILES Prediction from PNG Images")
    st.write("ℹ️ Upload PNG images and let me predict the SMILES notation for each one!")

    uploaded_files = st.file_uploader("📂 Upload PNG Images", type="png", accept_multiple_files=True)
    
    if uploaded_files:
        for uploaded_file in uploaded_files:
            # Save uploaded file to temporary directory
            temp_dir = tempfile.mkdtemp()
            temp_image_path = os.path.join(temp_dir, "uploaded_image.png")
            with open(temp_image_path, "wb") as f:
                f.write(uploaded_file.getvalue())

            # Read and display uploaded image
            image = Image.open(temp_image_path)
            st.image(image, caption=f'🖼️ Uploaded Image - {uploaded_file.name}', width=400)

            with st.spinner("⌛ Creating SMILES..."):
                # Predict SMILES
                SMILES = predict_smiles(temp_image_path)
            
            st.write(f"🔍 Predicted SMILES for {uploaded_file.name}:")
            st.write(SMILES)
            st.write("---")

if __name__ == "__main__":
    main()
