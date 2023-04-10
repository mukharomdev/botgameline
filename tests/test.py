import os
import sys
from dotenv import load_dotenv
import botgameline
import unnittest

load_dotenv()  # take environment variables from .env.

# Code of your application, which uses environment variables (e.g. from `os.environ` or
# `os.getenv`) as if they came from the actual environment.
# 
if __name__ == '__main__':
	unnittest.main()
	print(os.environ["DOMAIN"])
	print(os.environ["EMAIL"])
	print(os.environ)
