import random
from flask import Flask, request, make_response, jsonify

import firebase_admin
from firebase_admin import credentials, firestore
cred = credentials.Certificate("serviceAccountKey.json")
firebase_admin.initialize_app(cred)
db = firestore.client()

app = Flask(__name__)

@app.route("/")
def index():
    homepage = "<h1>猜謎語</h1>"
    homepage += "<a href=/riddle>物品型謎語</a><br>"
    homepage += "<a href=/place>地方型謎語</a><br>"
    homepage += "<a href=/slang>俚語型謎語</a><br>"
    homepage += "<a href=/random>隨機型謎語</a><br>"
    return homepage

@app.route("/webhook", methods=["POST"])
def webhook():
    req = request.get_json(force=True)
    action =  req.get("queryResult").get("action")
    session = req.get("session")[-12:-1]  #取最後12個字元

    if (action == "keywordchoice"):
        keyword =  req.get("queryResult").get("parameters").get("keyword")
       
        collection_ref = db.collection("riddle")
        docs = collection_ref.get()
        
        result =""
        
        if(keyword=="物品"):
            n = random.randint(1, 10)
        
            i = docs.to_dict()["item"]
            
        
            for doc in i:
                dict = doc.to_dict() 
                if n == dict["num"]:
                    info = "問題"+ n +" : "+format(dict["Question"])+"\n"+"答案 : \n"+format(dict["Answer"])+"\n"+"解釋 : \n"+format(dict["Explanation"])+"\n"
                    return make_response(jsonify({"fulfillmentText": info}))
        else:
            result = "是怎樣?皮啊?給我重輸"
            return make_response(jsonify({"fulfillmentText": result}))
            # else:
            #     return render_template("riddle.html")

            # result =""

            # for doc in docs:
            #     dict = doc.to_dict()
            #     if keyword in dict["num"]:
            #         result = "問題 : <br>"+format(dict["Question"])+"<br>"+"答案 : <br>"+format(dict["Answer"])+"<br>"+"解釋 : <br>"+format(dict["Explanation"])+"<br>"

            # if result == "":
            #     result = "是怎樣?皮啊?給我重輸"
            # return result
            
           
 '''      elif(keyword==dict["place"]):
            random = random.randint(1,7))
            if(random==dict["num"])
                info+=(dict["Question"])
                guessnum = int(req.get("queryResult").get("parameters").get("any"))
                if guessnum == dict["Answer"]:
                    reply += "恭喜你答對了\n" 
                    reply += dict["Link"]
                    return mjsonify(reply)
                else:
                    reply += "喔喔你答錯了喔，請繼續猜呦\n" 
                    return make_response(jsonify({"fulfillmentText": reply})) 

        elif(keyword==dict["random"]):
            random = random.randint(1,11))
            if(random==dict["num"])
                info+=(dict["Question"])
                guessnum = int(req.get("queryResult").get("parameters").get("any"))
                if guessnum == dict["Answer"]:
                    reply += "恭喜你答對了\n" 
                    reply += dict["Link"]
                    return ("fulfillmentText": reply)
                else:
                    reply += "喔喔你答錯了喔，請繼續猜呦\n" 
                    return make_response(jsonify({"fulfillmentText": reply}))

        elif(keyword==dict["slang"]):
            random = random.randint(1,7))
            if(random==dict["num"])
                info+=(dict["Question"])
                guessnum = int(req.get("queryResult").get("parameters").get("any"))
                if guessnum == dict["Answer"]:
                    reply += "恭喜你答對了\n" 
                    reply += dict["Link"]
                    return jsonify(reply)
                else:
                    reply += "喔喔你答錯了喔，請繼續猜呦\n" 
                    return make_response(jsonify({"fulfillmentText": reply})) 
'''

if __name__ == "__main__":
    app.run()