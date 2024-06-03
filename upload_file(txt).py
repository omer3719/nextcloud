from io import BytesIO
import nc_py_api

if __name__ == "__main__":
    # Nextcloud bağlantısını başlatma
    nc = nc_py_api.Nextcloud(nextcloud_url="https://birbulut.com", nc_auth_user="omer", nc_auth_pass="R2dxkf22")

    # Bellekte bir tampon oluşturma
    buf = BytesIO()

    # Tampona metin yazma
    buf.write("Bu bir örnek metin dosyasıdır.".encode("utf-8"))

    # Tamponun konumunu başa döndürme
    buf.seek(0)

    # Metin dosyasını tampondan Nextcloud'a yükleme
    nc.files.upload_stream("örnek.txt", buf)
