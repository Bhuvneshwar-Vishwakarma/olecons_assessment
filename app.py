import streamlit as st
import requests
import io
from PIL import Image
from constants import API_URL, headers

def query(payload):
    response = requests.post(API_URL, headers=headers, json=payload)
    return response.content

def main():
    st.title("Image Generation App")
    user_input = st.text_input("Enter your description:")
    
    if st.button("Generate Image"):
        if user_input:
            image_bytes = query({"inputs": user_input})
            image = Image.open(io.BytesIO(image_bytes))
            st.image(image, caption="Generated Image", use_column_width=True)
            
            image_filename = "generated_image.png"
            st.download_button(label="Download Image", data=image_bytes, file_name=image_filename, mime="image/png")
        else:
            st.warning("Please enter a description above to generate the image.")

if __name__ == "__main__":
    main()
