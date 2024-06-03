from io import BytesIO

from PIL import Image  # this example requires `pillow` to be installed

import nc_py_api

if __name__ == "__main__":
    nc = nc_py_api.Nextcloud(nextcloud_url="https://birbulut.com", nc_auth_user="omer", nc_auth_pass="R2dxkf22")
    buf = BytesIO()
    Image.merge(
        "RGB",
        [
            Image.linear_gradient(mode="L"),
            Image.linear_gradient(mode="L").transpose(Image.ROTATE_90),
            Image.linear_gradient(mode="L").transpose(Image.ROTATE_180),
        ],
    ).save(
        buf, format="JPEG"
    )  # saving image to the buffer
    buf.seek(0)  # setting the pointer to the start of buffer
    nc.files.upload_stream("LGBT.jpeg", buf)  # uploading file from the memory to the user's root folder

