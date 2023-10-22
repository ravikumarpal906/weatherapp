from flask import Flask, render_template,request
import requests

app=Flask(__name__)

@app.route("/")
def hompage():
    return render_template("index.html")

@app.route("/weatherapp",methods=['POST','GET'])
def get_weatherdata():
    url = "https://api.openweathermap.org/data/2.5/weather"
    params = {
        'q':request.form.get("city"),
        'appid':request.form.get("appid"),
        'units':'units'
        }
    respose = requests.get(url,params=params)
    city = data["city"]
    data = respose.json()
    return f"data:{data}, city: {city}"
    

if __name__=='__main__':
    app.run(host="0.0.0.0")