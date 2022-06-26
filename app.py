"""Imports"""
from flask import Flask, render_template, request, jsonify

from secure import USDA_API

# Flask constructor
app = Flask(__name__)

# Home page
@app.route('/', methods = ['POST', 'GET'])
def home_page():
    return render_template('homepage.html')

# Find page
@app.route('/find', methods = ['POST', 'GET'])
def market_search():
    if request.method == 'GET':
        return render_template('findfarms.html')

    else:
        location = request.form['location_search']
        location = location.replace(" ", "%20")

        # send request to USDA API to get list of farm markets in that area
        # based on radius, example: 
        # https://www.usdalocalfoodportal.com/api/agritourism/?apikey=APIKEY&x=-84&y=42&radius=30

        # markets_json = 

# Run App
if __name__=='__main__':
   app.run(debug=True)