import random
from flask import Flask, render_template, request, make_response, jsonify

import firebase_admin
from firebase_admin import credentials, firestore
cred = credentials.Certificate("serviceAccountKey.json")
firebase_admin.initialize_app(cred)
db = firestore.client()

app = Flask(__name__)
@app.route("/webhook3", methods=["POST"])
def webhook3():
    req = request.get_json(force=True)
    action =  req.get("queryResult").get("action")
    if (action == "keywordchoice"):
        keyword =  req.get("queryResult").get("parameters").get("keyword")
        guessnum = int(data.get("queryResult").get("parameters").get("any"))

        collection_ref = db.collection("riddle")
        docs = collection_ref.get()
        dict = doc.to_dict()

        if(keyword==dict["item"]):
            #random = random.randint(1,11))
            random = 1
            if(random==dict["num"])
                info += dict["Question"] + dict["Answer"] + dict["Explanation"] + dict["Link"]
                return info
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