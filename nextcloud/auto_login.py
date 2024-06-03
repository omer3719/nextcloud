import requests

# Nextcloud sunucunuzun URL'si
nextcloud_url = "https://example.com"

# Nextcloud kullanıcı adı ve parolası
username = "user"
password = "password"

# Oturum açma isteği için gerekli veri
login_data = {
    'userid': username,
    'password': password
}

# Oturum açma isteği gönderme
response = requests.post(f"{nextcloud_url}/index.php/login", data=login_data)

# Yanıtı kontrol etme
if response.status_code == 200:
    print("Oturum açma başarılı!")
    # İsteğin yanıtını kullanabilirsiniz
    # Örneğin, oturumunuzun geçerli olduğunu doğrulayabilirsiniz
else:
    print("Oturum açma başarısız. Hata kodu:", response.status_code)
    # Yanıtın içeriğini kontrol ederek hatayı belirleyebilirsiniz