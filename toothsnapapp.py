import os
import streamlit as st
import io
from PIL import Image, ImageDraw
from Library.vertex_ai_predict_image import predict_image_object_detection_sample
def upload_my_image_and_predict():
    st.write("## Detect potential dental issues")
    st.write(
        ":grin: Try uploading one or more images"
    )

    MAX_FILE_SIZE = 5 * 1024 * 1024  # 5MB
    col1,col2,col3,col4 = st.columns([2,1,1,1])
    col5,col6,col7,col8 = st.columns([2,1,1,1])
    col9,col10,col11,col12 = st.columns([2,1,1,1])
    col13,col14,col15,col16 = st.columns([2,1,1,1])


    # Add upload buttons to each cell in the matrix
    with col1:
        my_upload_1 = st.file_uploader("Upper Left")

    with col5:
        my_upload_2 = st.file_uploader("Upper Right")

    with col9:
        my_upload_3 = st.file_uploader("Lower Left")

    with col13:
        my_upload_4 = st.file_uploader("Lower Right")
    def convert_img_to_bytes(input_image):
        image_original = Image.open(input_image)
        img_bytes_arr = io.BytesIO()
        image_original.save(img_bytes_arr, format=image_original.format)
        img_bytes_arr = img_bytes_arr.getvalue()
        return img_bytes_arr


    def predict_image(input_image,col112,col111):
        json_token = 'authorization.json'
        project_id = '231827684533'
        location = 'us-central1'
        endpoint_id = "5807455491168665600"

        # Define image original
        image_original = Image.open(input_image)
        image_rectangle = Image.open(input_image)
        #col3.write("Original Image :camera:")
        #col3.image(image_original)

        # Update GCP credential using our json token
        os.environ["GOOGLE_APPLICATION_CREDENTIALS"] = json_token

        # Predict image
        try:
            result = predict_image_object_detection_sample(
                project=project_id,
                endpoint_id=endpoint_id,
                location=location,
                bytes_file=convert_img_to_bytes(input_image),
                confidence_threshold=0.08,
            )
            if len(result['displayNames']) > 0:
                for i in range(0,len(result['displayNames'])):
                    print("Result Category:", result['displayNames'][i])
                    print("Result Bounding Box:", result['bboxes'][i])
                    print("Result confidences:", result['confidences'][i])
                    bbox = result['bboxes'][i]
                    category_name = result['displayNames'][i]

                    # Get Image Size
                    width, height = image_rectangle.size

                    # Scale coordinates
                    x_min = bbox[0] * width
                    x_max = bbox[1] * width
                    y_min = bbox[2] * height
                    y_max = bbox[3] * height

                    # Draw Rectangle
                    draw = ImageDraw.Draw(image_rectangle)
                    draw.rectangle([(x_min, y_min), (x_max, y_max)], outline="red", width=2)
                    status = f" :blue[{category_name}] is detected"
            else:
                print("no result")
                category_name = "No Result from Prediction"
                status = f":red[{category_name}] :exploding_head:"

            col111.write(status)
            col112.image(image_rectangle)
        except:
            message = 'Kindly ensure that the API is enabled, as I was unable to obtain the results.'
            st.write(f":red[{message}]")

    with col2:
        if my_upload_1 is not None:
            if my_upload_1.size  > MAX_FILE_SIZE:
                st.error("The uploaded file is too large. Please upload an image smaller than 5MB.")
            else:
                image1 = Image.open(my_upload_1)
                st.image(image1,width=400)
                predict_image(my_upload_1,col3,col4)
    # else:
    #     print("Error: Please upload all the images")
    with col6:
        if my_upload_2 is not None:
            if my_upload_2.size > MAX_FILE_SIZE:
                st.error("The uploaded file is too large. Please upload an image smaller than 5MB.")
            else:
                image1 = Image.open(my_upload_2)
                st.image(image1,width=400)
                predict_image(my_upload_2,col7,col8)
    with col10:
        if my_upload_3 is not None:
            if my_upload_3.size > MAX_FILE_SIZE:
                st.error("The uploaded file is too large. Please upload an image smaller than 5MB.")
            else:
                image1 = Image.open(my_upload_3)
                st.image(image1,width=400)
                predict_image(my_upload_3,col11,col12)
    with col14:
        if my_upload_4 is not None:
            if my_upload_4.size > MAX_FILE_SIZE:
                st.error("The uploaded file is too large. Please upload an image smaller than 5MB.")
            else:
                image1 = Image.open(my_upload_4)
                st.image(image1,width=400)
                predict_image(my_upload_4,col15,col16)

    css = '''
    <style>
        [data-testid='stFileUploader'] {
            width: max-content;
        }
        [data-testid='stFileUploader'] section {
            padding: 0;
            float: right;
        }
        [data-testid='stFileUploader'] section > input + div {
            display: none;
        }
        [data-testid='stFileUploader'] section + div {
            float: left;
            padding-top: 0;
        }
    }

    </style>
    '''

    st.markdown(css, unsafe_allow_html=True)

def createPage():
    #st.markdown("<h1 style='text-align: center; color:#779fd6;'>Toothpix</h1>", unsafe_allow_html=True)
    #image = Image.open('smileimg.jpg')
    set_bg_hack_url()
    # col1, col2, col3 = st.columns(3)
    # with col1:
    #     st.write(' ')
    # with col2:
    #     st.video("introvideo.mp4",loop=True,autoplay=True)
    # with col3:
    #     st.write(' ')
    #st.image(image,width=400)
    return True

def set_bg_hack_url():
    '''
    A function to unpack an image from url and set as bg.
    Returns
    -------
    The background.
    '''

    st.markdown(
        f"""
         <style>
         .stApp {{
             background: url("https://wallpapercave.com/wp/wp11901739.jpg");
             background-size: cover
         }}
         </style>
         """,
        unsafe_allow_html=True
    )

if __name__ == '__main__':
    upload_my_image_and_predict()
    set_bg_hack_url()