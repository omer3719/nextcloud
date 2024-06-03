import nc_py_api

if __name__ == "__main__":
    # Nextcloud istemcisini oluştur
    nc = nc_py_api.Nextcloud(nextcloud_url="https://birbulut.com", nc_auth_user="omer", nc_auth_pass="R2dxkf22")

    # Kullanıcıları listele
    users = nc.users.list()

    print("Nextcloud Kullanıcıları:")
    for user in users:
        print(user)