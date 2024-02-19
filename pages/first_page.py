import os
import streamlit as st
from clarifai.client.model import Model
from clarifai.client.input import Inputs
from clarifai.client.auth import create_stub
from clarifai.client.auth.helper import ClarifaiAuthHelper
from clarifai.client.user import User
from clarifai.modules.css import ClarifaiStreamlitCSS
from clarifai_grpc.channel.clarifai_channel import ClarifaiChannel
from clarifai_grpc.grpc.api import resources_pb2, service_pb2, service_pb2_grpc
from clarifai_grpc.grpc.api.status import status_code_pb2
from google.protobuf import json_format, timestamp_pb2

st.set_page_config(layout="wide")
ClarifaiStreamlitCSS.insert_default_css(st)

st.title("Clarifai NextGen Nexus App")

def main():

    response = client.images.generate(
      model="dall-e-2",
      prompt=promptt,
      size="1024x1024",
      quality="standard",
      n=1,
    )
    image_url = response.data[0].url
    return image_url

if __name__ == '__main__':
    st.title("Dalle - App")
    password = ""
    password = st.text_input("Enter your API-KEY:", type="password")
    prompt = st.text_input("Enter a prompt:")
    if st.button("Generate Image"):
        if(password != ""):
            client = OpenAI(api_key = password)
            url = main(prompt)
            #url = "https://oaidalleapiprodscus.blob.core.windows.net/private/org-yAYPjlgfGXibO0vm2BcHo8Ds/user-Hj9p1PrLa4pl6IqwSOTGUWAC/img-Qn4jGiW847QexJALxgHjbgkE.png?st=2024-02-17T09%3A40%3A49Z&se=2024-02-17T11%3A40%3A49Z&sp=r&sv=2021-08-06&sr=b&rscd=inline&rsct=image/png&skoid=6aaadede-4fb3-4698-a8f6-684d7786b067&sktid=a48cca56-e6da-484e-a814-9c849652bcb3&skt=2024-02-17T00%3A12%3A11Z&ske=2024-02-18T00%3A12%3A11Z&sks=b&skv=2021-08-06&sig=0fa7RSvbDqes/Rg5pJfT9LxM/39CoX3%2BqyfTPRgV1OY%3D"
            try:
                st.image(url, caption="Image", use_column_width=True)
            except:
                st.error("Sorry, no image created for the provided prompt.")
            st.markdown(url)
        else:
            st.markdown("Write Correct API_KEY")
