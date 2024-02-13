import os
import streamlit as st
from PIL import Image
import shutil
from io import BytesIO
from DECIMER import predict_SMILES 

# Function to predict SMILES
def predict_smiles(image):
    SMILES = predict_SMILES(image)
    return SMILES

# Main function for Streamlit app
def main():
    st.title("SMILES Prediction from PNG Images")
    st.write("ℹ️ Upload PNG images and let me predict the SMILES notation for each one!")

    uploaded_files = st.file_uploader("📂 Upload PNG Images", type="png", accept_multiple_files=True)
    
    if uploaded_files:
        temp_dir = "temp_images"
        if not os.path.exists(temp_dir):
            os.makedirs(temp_dir)
        for uploaded_file in uploaded_files:
            # Save uploaded file to temporary directory
            image = Image.open(uploaded_file)
            image_path = os.path.join(temp_dir, uploaded_file.name)
            image.save(image_path)

            # Read and display uploaded image
            st.image(image, caption=f'🖼️ Uploaded Image - {uploaded_file.name}', width=400)

            with st.spinner("⌛ Creating SMILES..."):
                # Predict SMILES
                SMILES = predict_smiles(image_path)
            
            st.write(f"🔍 Predicted SMILES for {uploaded_file.name}:")
            st.write(SMILES)
            st.write("---")
        
        # Clean up temporary directory
        shutil.rmtree(temp_dir)

if __name__ == "__main__":
    main()
