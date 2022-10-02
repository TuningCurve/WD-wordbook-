import streamlit as st
import s3fs
import os
from PIL import Image, ImageStat

# Create connection object.
# `anon=False` means not anonymous, i.e. it uses access keys to pull data.
fs = s3fs.S3FileSystem(anon=False)

# Retrieve file contents.
# Uses st.experimental_memo to only rerun when the query changes or after 10 min.
@st.experimental_memo(ttl=600)
def read_file(filename):
    with fs.open(filename) as f:
        return f.read().decode("utf-8")

content = read_file("wd-wordbook/myfile.csv")

# Print results.
for line in content.strip().split("\n"):
    name, pet = line.split(",")
    st.write(f"{name} has a :{pet}:")

infile = fs.open("wd-wordbook/girl01.png")
image = Image.open(infile)
st.image(image, caption='test')