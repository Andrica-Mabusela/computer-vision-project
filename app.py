import streamlit as st
import tempfile

st.markdown(
    """
        <style>
            @import url('https://fonts.googleapis.com/css2?family=Google+Sans:ital,opsz,wght@0,17..18,400..700;1,17..18,400..700&display=swap');
            .stApp {
                background-color: #f5945c;
                color: #fff;
            }
            
            .custom-title {
                font-family: "Google Sans", sans-serif;
                font-size: 48px;
                font-weight: 700;
                }
            
            div[role="radiogroup"] label {
                font-size: 20px !important;
                font-weight: 700;
                color: white !important;
                padding: 8px 15px;
                margin-bottom: 10px;
                display: flex;
                align-items: center;
                }
            
            /*VIDEO UPLOADER CSS STYLES*/
            div[data-testid="stFileUploader"] {
                background-color: #fec76f;
                padding: 20px;
                border-radius: 12px;
                border: 2px dashed #333;
            }

            div[data-testid="stFileUploader"] button {
                background-color: #f5945c !important;
                color: white !important;
                border-radius: 8px;
                padding: 8px 16px;
            }

          /* VIDEO PLAYER STYLES */
            video {
                margin: 15px 10px !important;
                width: 80% !important;
                height: 400px !important;
                border-radius: 12px;
                border: 2px solid black;
            }
        </style>
    """,
    unsafe_allow_html=True
)

# Set App Configs 
st.set_page_config(
    page_icon="uj_logo.jpg",
    layout="wide"
)

# Show the UJ logo
st.logo("uj_logo.jpg")


# -------------------- Start Of App Reactive Functions ------------------------
def my_function():
    st.success("Okay, Let's classify the video.")

# -------------------- END Of App Reactive Functions ------------------------

# Set the Page Title using custom html.
st.markdown(
    '<h1 class="custom-title">Daily Living Action Recognition Using Neural Network</h1>',
    unsafe_allow_html=True
)

# Create columns
sidebar, main = st.columns([1, 4])

# Sidebar column
with sidebar:
    # st.markdown("### Menu")

    page = st.radio(
        "Navigation Menu",
        ["Dashboard", "Analytics", "Settings", "Classify", "List Item 5", "List Item 6", "List Item 7"]
    )

# Main content column
with main:

# NEW SECTION
    if page == "Dashboard": # Show Dashboard Content
        st.title("Dashboard Main Content")
        st.write("This is the main dashboard area.")
        
        
# NEW SECTION
    elif page == "Analytics":
        st.title("Analytics")
        st.write("Analytics content goes here.")

        st.line_chart([1, 5, 2, 6, 2, 1])
        
        
        
        
# NEW SECTION
    elif page == "Settings":
        st.title("Settings")
        st.write("Settings page.")

# NEW SECTION
    elif page == "Classify":
        st.title("Video Action Recognition")
        # st.write("")
        uploaded_video = st.file_uploader(
        "Choose a video to be classified",
        type=["mp4"]
        )
        
        if uploaded_video is not None:

            # Save uploaded file temporarily
            tfile = tempfile.NamedTemporaryFile(delete=False)
            tfile.write(uploaded_video.read())

            # Display video player
            st.video(tfile.name)

            # Metadata
            st.write("Filename:", uploaded_video.name)
            st.write("File type:", uploaded_video.type)
            st.write("File size:", round(uploaded_video.size / (1024 * 1024), 2), "MB")
            
            st.success("Video uploaded successfully.")
            
            # Button to trigger video action recognition
            if st.button("Recognize action"):
                my_function()

        
        
        
# NEW SECTION
        
    elif page == "List Item 5":
        st.title("List Item 5")
        st.write("List Item 5 page.")
        
# NEW SECTION
    elif page == "List Item 6":
        st.title("List Item 6")
        st.write("List Item 6")
    
# NEW SECTION
    elif page == "List Item 7":
        st.title("List Item 7")
        st.write("List Item 7")