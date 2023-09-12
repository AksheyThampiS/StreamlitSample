import streamlit as st
import os
import time

# Function to upload and save a file to a local folder
def save_uploaded_file(uploaded_file, folder_path):
    if uploaded_file:
        file_path = os.path.join(folder_path, uploaded_file.name)
        with open(file_path, "wb") as f:
            f.write(uploaded_file.read())
        return file_path
    return None

# Streamlit UI
st.title("File Upload Progress Bar")

# Create a folder to save uploaded files
upload_folder = "uploads"
os.makedirs(upload_folder, exist_ok=True)

# Upload a file
uploaded_file = st.file_uploader("Upload a file:", type=["csv", "txt", "xlsx"])

if uploaded_file:
    
    # Display progress bar
    progress_bar = st.progress(0)

    time.sleep(3)

    # Save the uploaded file to the local folder with progress tracking
    file_path = save_uploaded_file(uploaded_file, upload_folder)

    if file_path:
        st.success(f"File saved to: {file_path}")
        progress_bar.empty()  # Clear the progress bar
    else:
        st.error("Failed to save the file.")

# Display files in the local folder
st.subheader("Uploaded Files")
uploaded_files = os.listdir(upload_folder)
for file_name in uploaded_files:
    st.write(file_name)
