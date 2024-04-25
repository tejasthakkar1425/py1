from io import BytesIO
import json
import hashlib
import random
import hmac
from random import randint
from datetime import datetime
import os

def getShaStr(msg):
    key="abc"
    print(msg.encode())
    h = hmac.new(key.encode(), msg.encode(), hashlib.sha256)
    digest = h.hexdigest()
    return digest

