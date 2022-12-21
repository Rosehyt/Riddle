from flask import Flask, render_template, request, make_response, jsonify

import firebase_admin
import random
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
            if keyword == dict["num"]:
                result = "問題"+keyword+" : <br>"+format(dict["Question"])+"<br>"+"答案 : <br>"+format(dict["Answer"])+"<br>"+"解釋 : <br>"+format(dict["Explanation"])+"<br>"
            
        if result == "":
            result = "是怎樣?皮啊?給我重輸"
        return result
    else:
        return render_template("riddle.html")

@app.route("/webhook", methods=["POST"])
def webhook():
	req = request.get_json(force=True)

# 	session = req.get("session")[-12:-1]  #取最後12個字元
	
	action =  req.get("queryResult").get("action")
	msg =  req.get("queryResult").get("queryText")
	# info = "動作：" + action + "； 查詢內容：" + msg
	# return make_response(jsonify({"fulfillmentText": info}))

    	if (action == "keywordchoice"):
		keyword = req.get("queryResult").get("parameters").get("keyword")
		
		if(keyword=="物品"):
			n = random.randint(1, 10)
			
            		collection_ref = db.collection("item")
		    	docs = collection_ref.get()
		    	result =""

			for doc in docs:
				dict = doc.to_dict()
				if n == dict["num"]:
					result = "問題"+ "\n" +" : "+format(dict["Question"])+"\n"+"答案 : \n"+format(dict["Answer"])+"\n"+"解釋 : \n"+format(dict["Explanation"])+"\n"
		return make_response(jsonify({"fulfillmentText": result}))
	else:
		result = "是怎樣?皮啊?給我重輸"
		return make_response(jsonify({"fulfillmentText": result}))


