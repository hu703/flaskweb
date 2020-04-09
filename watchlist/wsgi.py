import os
from dotenv import load_dotenv

#  部署环境的配置
dotenv_path = os.path.join(os.path.dirname(__file__),'.env')
if os.path.exists(dotenv_path):
    load_dotenv(dotenv_path)

from watchlist import app