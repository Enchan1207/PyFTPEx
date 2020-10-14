#
# FTP, SFTP接続を試してみる
#
import settings
from ftplib import FTP
import paramiko as SFTP

def main():
    # FTP
    print("FTP Connection.")
    ftp = FTP(
        settings.HOST,
        settings.USERNAME,
        passwd = settings.PASSWORD
    )
    # ls
    print("ls: ")
    fileList = ftp.nlst("./www/")
    print(fileList)

    ftp.quit()

    # SFTP
    print("SFTP Connection.")
    sftp = SFTP.SSHClient()
    sftp.set_missing_host_key_policy(SFTP.AutoAddPolicy)
    sftp.connect(
        settings.HOST,
        port = settings.PORT,
        username = settings.USERNAME,
        password = settings.PASSWORD
    )
    try:
        # セッションを開く
        connection = sftp.open_sftp()

        # ls
        print("ls: ")
        fileList = connection.listdir("./www/")
        print(fileList)

    finally:
        sftp.close()

if __name__ == "__main__":
    main()
    print("Type Ctrl+C to exit.")
    try:
        while True:
            pass
    except KeyboardInterrupt:
        pass

