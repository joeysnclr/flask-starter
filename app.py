from flask import Flask, render_template, flash, redirect, url_for, session, request, logging
import json
import os
import dotenv
import pymongo

# load .env file
if not os.path.exists('.env'):
    os.system("touch .env")
dotenv.load_dotenv()


# init MongoDB connection

client = pymongo.MongoClient(os.environ.get("mongodb_url"))
db = client['db-name']
collection = db['collection-name']


app = Flask(__name__)
port = int(os.environ.get('PORT', 5000))


@app.route('/')
def index():
    return render_template('index.html')


app.run(host='0.0.0.0', port=port, debug=True)
