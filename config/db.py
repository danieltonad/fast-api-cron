from deta import Deta
from dotenv import load_dotenv
import os

load_dotenv()

# init
deta =  Deta()

# connect to db
database =  deta.Base('fast-api-dump')