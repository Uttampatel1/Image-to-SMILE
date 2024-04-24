import streamlit as st
from DECIMER import predict_SMILES
from PIL import Image
import os
import pandas as pd


# Function to predict SMILES from image
@st.cache_resource
def predict_smiles(image):
    smiles = predict_SMILES(image)
    return smiles

# Streamlit app
def main():
    st.title("Image to SMILES Converter")

    # Upload multiple images
    uploaded_files = st.file_uploader("Upload Images", type=["png", "jpg"], accept_multiple_files=True)

    if uploaded_files:
        smiles_data = []
        for uploaded_file in uploaded_files:
            # Save uploaded image
            image_path = os.path.join("uploaded_images", uploaded_file.name)
            with open(image_path, "wb") as f:
                f.write(uploaded_file.getbuffer())

            # Predict SMILES
            smiles = predict_smiles(image_path)

            # Save image name and SMILES
            smiles_data.append({"Image Name": uploaded_file.name, "SMILES": smiles})

            # Display uploaded image
            st.image(uploaded_file, caption="Uploaded Image", use_column_width=True)

            # Display predicted SMILES
            st.write("Predicted SMILES:", smiles)
            st.write("---")

        # Create DataFrame from collected data
        df = pd.DataFrame(smiles_data)

        # Add a download button for CSV file
        csv = df.to_csv(index=False)
        st.download_button(
            label="Download CSV",
            data=csv,
            file_name="smiles_predictions.csv",
            mime="text/csv"
        )

if __name__ == "__main__":
    main()
