import firebase_admin
import random
import requests
from bs4 import BeautifulSoup
from firebase_admin import credentials, firestore
cred = credentials.Certificate("serviceAccountKey.json")
firebase_admin.initialize_app(cred)
db = firestore.client()

from flask import Flask, render_template, request
from datetime import datetime

app = Flask(__name__)

@app.route("/")
def index():
    homepage = "<h1>猜謎語</h1>"
    homepage += "<a href=/riddle>物品型謎語</a><br>"
    homepage += "<a href=/place>地方型謎語</a><br>"
    homepage += "<a href=/slang>俚語型謎語</a><br>"
    homepage += "<a href=/random>隨機型謎語</a><br>"
    return homepage

@app.route("/riddle",methods=["GET", "POST"])
def riddle():
    if request.method == "POST":
        keyword = request.form["keyword"]
        
        db = firestore.client()
        collection_ref = db.collection("item")
        docs = collection_ref.get()
        
        result =""

        for doc in docs:
            dict = doc.to_dict()
            if keyword in dict["num"]:
                result = format(dict["Question"])

        if result == "":
            result = "是怎樣?皮啊?給我重輸"
        return result
    else:
        return render_template("riddle.html")
