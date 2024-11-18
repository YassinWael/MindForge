from flask import Flask,render_template
import json
from random import choice
import re

with open("messages.json","r",encoding="utf-8") as messages:
    messages_list = json.load(messages)

with open("links.json","r",encoding="utf-8") as links: 
    links_list = json.load(links)
    print(links_list)


def strongify(text):
    """Takes text (str) and turns all the '*' into opening and closing strong tags """
    result = re.sub(r'\*(.*?)\*', r'<strong>\1</strong>', text)
    return result







app = Flask(__name__)

app.jinja_env.filters['strongify'] = strongify

@app.route("/home")
@app.route("/")
def home():
    return render_template('home.html',message=choice(messages_list),link=choice(links_list))


if __name__ == "__main__":
    app.run(debug=True,host='0.0.0.0',port=8080)



# TODO: add the "*" becomes italic/bold