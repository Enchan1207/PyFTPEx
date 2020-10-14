#
# 環境変数設定
#
import os
from os.path import join, dirname
from dotenv import load_dotenv

load_dotenv(verbose=True)

dotenv_path = join(dirname(__file__), '.env')
load_dotenv(dotenv_path)

HOST = os.environ.get("HOST")
PORT = os.environ.get("PORT")
USERNAME = os.environ.get("USERNAME")
PASSWORD = os.environ.get("PASSWORD")
