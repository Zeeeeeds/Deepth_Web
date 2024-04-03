import streamlit as st
import base64
import os
from PIL import Image

def main_bg(main_bg_path):
    with open(main_bg_path, "rb") as image_file:
        encoded_string = base64.b64encode(image_file.read()).decode()
    st.markdown(
        f"""
        <style>
            .stApp {{
                background: url(data:image/jpeg;base64,{encoded_string});
                background-size: cover;
            }}
        </style>
        """,
        unsafe_allow_html=True
    )

# 构建正确的文件路径
base_dir = os.path.dirname(os.path.abspath(__file__))  # 获取当前脚本文件所在的目录
backimage_path = os.path.join(base_dir, 'files', 'back4.jpg')  # 构建图片文件路径
main_bg(backimage_path)

st.title("Bin-Imaging")
image_path = os.path.join(base_dir, 'files', 'logo.jpg')  # 构建Logo图片路径
image = Image.open(image_path)
st.image(image)

button = st.button("Start our travel!")
if button:
    st.write("Welcome to our website!")

st.write("\n\n\n\n\n\n\n\n\n\n\n")
st.markdown("---")
st.caption("If you want to learn about our website, please turn to the Introduction part.")