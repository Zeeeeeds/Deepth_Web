import streamlit as st
import base64
from PIL import Image
import io
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
#设置背景
base_dir = os.path.dirname(os.path.abspath(__file__))  # 获取当前脚本文件所在的目录
backimage_path = os.path.join(base_dir,'..' ,'files', 'back4.jpg')  # 构建图片文件路径
main_bg(backimage_path)
st.header("Depth image")
st.divider()
#设置图片上传按钮
st.subheader("Upload Image")
image_file = st.file_uploader("Upload Images", 
type=["png","jpg","jpeg"])
check_details = st.button("Check Details")
if check_details:
    if image_file is not None:
        # To See details
        image_details = {"file_name":image_file.name, 
        "file_type":image_file.type,
                        "file_size":image_file.size}
        st.write(image_details)
        # To View Uploaded Image
        image_data = image_file.read()
        image = Image.open(io.BytesIO(image_data))
        st.image(image, width=250)
    else:
        st.write("No Image File is Uploaded")