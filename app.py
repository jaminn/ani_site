import pymongo
import os
from flask import Flask, render_template

app = Flask(__name__)
client = pymongo.MongoClient("mongodb://rnnwkals1:hi000319@ds041939.mlab.com:41939/ani_db")
db = client.ani_db


def query2db(query):
    anis = db.anime2.find_one({"info.name": {"$regex": query + ""}})
    # print(anis["info"]["name"])
    # print(anis["info"]["sumnail"])
    # for ani in anis["list"]:
    #     print(ani["name"], ani["url"], ani["sumnail"])
    return anis


@app.route('/aaa')
def hello():
    return "Sang"


@app.route('/<query>')
def index(query):
    anis = query2db(query)
    return render_template("ani_page.html", anis=anis)
    # return "jamin:"+query+str(anis)+"end"


if __name__ == '__main__':
    app.debug = True
    port = int(os.environ.get("PORT", 5000))
    app.run(host='0.0.0.0', port=port)
