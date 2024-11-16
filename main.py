from flask import Flask,render_template
import json
from random import choice

with open("messages.json","r",encoding="utf-8") as messages:
    messages_list = json.load(messages)
    print(messages_list)





app = Flask(__name__)



@app.route("/")
def home():
    return render_template('home.html',message=choice(messages_list))


if __name__ == "__main__":
    app.run(debug=True,host='0.0.0.0',port=8080)



# TODO: add the "*" becomes italic/bold