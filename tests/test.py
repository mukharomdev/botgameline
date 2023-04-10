import os
import path
from dotenv import load_dotenv

load_dotenv()  # take environment variables from .env.

# Code of your application, which uses environment variables (e.g. from `os.environ` or
# `os.getenv`) as if they came from the actual environment.
# 
print(os.environ["DOMAIN"])
print(os.environ["EMAIL"])
print(os.environ)