from flask import Flask, render_template
import requests

page = requests.get("https://services5.arcgis.com/VS6HdKS0VfIhv8Ct/arcgis/rest/services/COVID19_Indonesia_per_Provinsi/FeatureServer/0/query?where=1%3D1&outFields=*&outSR=4326&f=json")
import json
page_json = page.json()
feature = page_json['features']
#print(page_json)

data_corona = []

for i in feature:
    corona = dict()
    corona['provinsi'] = i['attributes']['Provinsi']
    corona['positif'] = i['attributes']['Kasus_Posi']
    corona['sembuh'] = i['attributes']['Kasus_Semb']
    corona['meninggal'] = i['attributes']['Kasus_Meni']

    data_corona.append(corona)

data_corona_ascending = sorted(data_corona, key= lambda x:x['provinsi'], reverse=False)

app = Flask(__name__)
@app.route("/")
def index():
    return render_template("index.html", corona=data_corona_ascending)

@app.route("/about")
def about():
    return render_template('about.html')
if __name__ == "__main__":
   app.run(debug=True)

