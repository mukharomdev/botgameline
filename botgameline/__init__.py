from botgameline.linepy import  *
# from akad.ttypes import Message,
from liff.ttypes import LiffChatContext, LiffContext, LiffSquareChatContext, LiffNoneContext, LiffViewRequest
from akad.ttypes import ContentType as Type,Message,TalkException
# from akad.ttypes import TalkException
from KhieBots.thrift.protocol import TCompactProtocol
from KhieBots.thrift.transport import THttpClient
from KhieBots.ttypes import LoginRequest
from datetime import datetime, timedelta
from time import sleep
from bs4 import BeautifulSoup
from humanfriendly import format_timespan, format_size, format_number, format_length
from gtts import gTTS
from threading import Thread
from io import StringIO
from multiprocessing import Pool
from googletrans import Translator
from urllib.parse import urlencode
from wikiapi import WikiApi
from tmp.MySplit import *
from zalgo import zalgoname
from random import randint
from shutil import copyfile
from youtube_dl import YoutubeDL
from lineservice import LineService
import subprocess, youtube_dl, humanize, traceback
import subprocess as cmd
import time, random, sys, json, null, codecs, html5lib ,shutil ,threading, glob, re, base64, string, os, requests, six, ast, pytz, wikipedia, urllib, urllib.parse, atexit, asyncio, traceback
_session = requests.session()
try:
    import urllib.request as urllib2
except ImportError:
    import urllib2

# __all__ = [
# 'LINE', 'Channel', 'OEPoll', 'OpType',
# 'LiffChatContext', 'LiffContext', 'LiffSquareChatContext', 'LiffNoneContext','LiffViewRequest',
# 'Type','Message','TalkException',

# ]
# import os
# platform = ...
# dirname = __path__[0]		# Package's main folder
# __path__.insert(0, os.path.join(dirname, "plat-" + platform))

