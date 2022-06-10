import streamlit as st
import numpy as np
from PIL import Image
from requests import post, get
image = Image.open('wally_foto.jpeg')
st.title('Where is Wally?')
wally = st.image(image, width=700)
def content():
    option = st.radio(
     'How would you like to upload a picture of Wally?',
     ('Upload file', 'Take photo through camera', 'URL to photo'),key='radio')
    if option == 'Upload file':
        uploader = st.file_uploader('Upload Picture with Wally in it here:')
    if option == 'Take photo through camera':
        uploader = st.camera_input('Take a photo of Wally')
    if option == 'URL to photo':
        url = st.text_input('Copy and paste URL here')
        if url:
            uploader = get(url).content
        else:
            uploader = False
    if uploader:
        original = st.image(uploader)
    else:
        original = False
    @st.cache(show_spinner = False)
    def upload():
        with st.spinner('Uploading picture...'):
            file = {'file': uploader}
            response = post("https://whereswallyimageimage-6hz62gkxgq-ew.a.run.app/", files=file)
        return response
    if uploader:
        response = upload()
    else:
        response = False
    if uploader:
        button = st.button('Start searching for Wally')
    else:
        button = False
    if uploader:
        suc = st.success('Photo uploaded')
    if button and not uploader:
        st.error('You have not uploaded any picture. Upload picture and try again.')
    if response and button:
        wally.empty()
        suc.empty()
        st.success('Wally is found!')
        forbal = st.image(response.content)
        original.empty()
    else:
        forbal = False
    if forbal:
        st.balloons()
content()
