import streamlit as st
import base64
import sys
import os
def main_bg(main_bg):
    main_bg_ext = "png"
    st.markdown(
        f"""
         <style>
         .stApp {{
             background: url(data:image/{main_bg_ext};base64,{base64.b64encode(open(main_bg, "rb").read()).decode()});
             background-size: cover
         }}
         </style>
         """,
        unsafe_allow_html=True
    )
base_dir = os.path.dirname(os.path.abspath(__file__))  # 获取当前脚本文件所在的目录
backimage_path = os.path.join(base_dir,'..' ,'files', 'back4.jpg')  # 构建图片文件路径
main_bg(backimage_path)
st.header("About us:")
text = '''
####   Binocular depth estimation is to shoot the same scene from different angles with two cameras, and then calculate the depth information of pixels in the picture according to the principle of parallax. At present, binocular depth estimation has become one of the research hotspots in the field of computer vision, and has been widely used in many fields.
####   We are developers from HIT and hope that the Bin-Imaging website will help users who want to achieve binocular depth estimation. There are Function 1: Generate depth images and Function 2: Generate 3D point cloud images, which users can freely choose to achieve their goals.
####   Finally, if you have any suggestions and doubts about the use of the website, please feel free to communicate with us.
'''
st.markdown(text)

