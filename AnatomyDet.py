import streamlit as st
from PIL import Image
import configurations
import utility
import tempfile
import cv2
from pathlib import Path
im = Image.open("assets/ico.png")


# Setting page layout
st.set_page_config(
    page_title="Anatomy Detection",
    page_icon=im,
    layout="wide",
    initial_sidebar_state="expanded"
)


header_image = "assets/header_img.jpeg"
st.image(header_image, width=600)

# Main page heading
st.title("Humerus and Glenoid Detection")

# Sidebar
st.sidebar.header("Detection configuration")


model_type = st.sidebar.radio(
    "Select Task", ['Detection', 'Segmentation'])

confidence = float(st.sidebar.slider(
    "Select Model Confidence", 25, 100, 75)) / 100

st.sidebar.header("Image/Video Config")
source_radio = st.sidebar.radio(
    "Select Source", configurations.SOURCES_LIST)


@st.cache_resource
def get_model_path(model_type):
    if model_type == 'Detection':
        return Path(configurations.DETECTION_MODEL)

# Load Pre-trained ML Model
@st.cache_resource
def load_model(model_path):
    try:
        model = utility.load_model(model_path)
        return model
    except Exception as ex:
        st.error(f"Unable to load model. Check the specified path: {model_path}")
        st.error(ex)

model_path = get_model_path(model_type)
model = load_model(model_path)

source_img = None
# If image is selected
if 'image_file_name' not in st.session_state:
	st.session_state.image_file_name = None
if source_radio == configurations.IMAGE:
    source_img = st.sidebar.file_uploader(
        "Choose an image...", type=("jpg", "jpeg", "png", 'bmp', 'webp'))
    if source_img:
        if source_img.name != st.session_state.image_file_name:
            print("running every time")
            st.session_state.image_file_name = source_img.name
            uploaded_image = Image.open(source_img)
            col1, col2 = st.columns(2)
            with col1:
                    # adding the uploaded image to the page with caption
                    st.image(
                        image=uploaded_image,
                        caption="Uploaded Image",
                        use_column_width=True
                    )

            with col2:
                res = model.predict(uploaded_image,
                                    conf=confidence)
                boxes = res[0].boxes
                if len(boxes) > 0:
                    res_plotted = res[0].plot()[:, :, ::-1]

                    st.image(res_plotted,
                                caption="Detected Image",
                                use_column_width=True)
# If video is selected
if 'vid_file_name' not in st.session_state:
	st.session_state.vid_file_name = None
if source_radio == configurations.VIDEO:
     source_video = st.sidebar.file_uploader(label="Choose a video...")
     if source_video:
          if source_video.name != st.session_state.vid_file_name:
                st.session_state.vid_file_name = source_video.name
                try:
                    tfile = tempfile.NamedTemporaryFile()
                    tfile.write(source_video.read())
                    vid_cap = cv2.VideoCapture(
                        tfile.name)
                    st_frame = st.empty()
                    while (vid_cap.isOpened()):
                        success, image = vid_cap.read()
                        if success:
                            utility.display_detected_frames(confidence,
                                                     model,
                                                     st_frame,
                                                     image
                                                     )
                        else:
                            vid_cap.release()
                            break
                except Exception as e:
                    st.error(f"Error loading video: {e}")
