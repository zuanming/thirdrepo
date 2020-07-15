from flask import Flask, render_template, request, redirect, url_for, flash
import pymongo
from dotenv import load_dotenv
from bson import ObjectId
import os
import datetime

# load in the variables in the .env file into our operating system environment
load_dotenv()

app = Flask(__name__)

# connect to mongo
client = pymongo.MongoClient(os.environ.get('MONGO_URI'))

CLOUD_NAME=os.environ.get('CLOUD_NAME')
UPLOAD_PRESET=os.environ.get('UPLOAD_PRESET')

# define my db_name
DB_NAME = "dating_profiles"

# read in the SESSION_KEY variable from the operating system environment
# SESSION_KEY = os.environ.get('SESSION_KEY')

# # set the session key
# app.secret_key = SESSION_KEY

# START OF CODE
@app.route('/')
def index():
    return 'Home'

@app.route('/show_all')
def show_all():
    all_profiles=client[DB_NAME].users.find()
    return render_template('show_all.template.html',all_profiles=all_profiles)

@app.route('/create_new')
def show_create_new():
    return render_template('create_new.template.html',cloud_name=CLOUD_NAME,upload_preset=UPLOAD_PRESET)

@app.route('/create_new',methods=['POST'])
def process_create_new():
    # first_name=request.form.get('first_name')
    # last_name=request.form.get('last_name')
    # gender=request.form.get('gender')
    # dob=request.form.get('dob')
    # religion=request.form.get('religion')
    # height=request.form.get('height')
    # languages=request.form.getlist('language')
    # self_summary=request.form.get('summary')
    # picture=request.form.get('uploaded_file_url')

    return redirect(url_for('show_all'))

    # datetime.datetime.strptime(due_date, "%Y-%m-%d")




# "magic code" -- boilerplate
if __name__ == '__main__':
    app.run(host='0.0.0.0',
            port=8080,
            debug=True)
