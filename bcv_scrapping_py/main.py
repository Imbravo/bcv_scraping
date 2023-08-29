from flask import Flask
import requests
from bs4 import BeautifulSoup
from scrapper import get_bcv
app = Flask(__name__)




@app.route("/")
def get_bcv_result():
    return get_bcv()


