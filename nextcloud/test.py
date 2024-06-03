import nc_py_api

from io import BytesIO
from PIL import Image

import sys
import os
from os.path import dirname
from os.path import join
sys.path.insert(0, join(dirname(__file__), 'src'))


nc = nc_py_api.Nextcloud(nextcloud_url="https://birbulut.com", nc_auth_user="omer", nc_auth_pass="R2dxkf22")

# Quick start







# def upload():
#     asd = open("omer.html", "r")

    # buf = BytesIO()
    # Image.merge(
    #     "RGB",
    #     [
    #         Image.linear_gradient(mode="L"),
    #         Image.linear_gradient(mode="L").transpose(Image.ROTATE_90),
    #         Image.linear_gradient(mode="L").transpose(Image.ROTATE_180),
    #     ],
    # ).save(
    #     buf, format="PNG"
    # )
    # buf.seek(0)
    # nc.files.upload_stream("omer_.html", asd)


# def list_dir(directory):
#     for node in nc.files.listdir(directory):
#         if node.is_dir:
#             list_dir(node)
#         else:
#             print(f"{node.user_path}")
#
#
# def find_file():
#     result = nc.files.find(["like", "omer", "%.html"])
#     for i in result:
#         print(i)
#     print("####" * 50)
#
#     result = nc.files.find(["eq", "name", "Nextcloud_Server_Administration_Manual.pdf"])
#     for i in result:
#         print(i)
#
#     result = nc.files.find(["eq", "name", "RGB.png"])
#     for i in result:
#         print(i)
#
#
# upload()
# find_file()
# list_dir("")