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

CLOUD_NAME = os.environ.get('CLOUD_NAME')
UPLOAD_PRESET = os.environ.get('UPLOAD_PRESET')

# define my db_name
DB_NAME = "food_reviews"

# read in the SESSION_KEY variable from the operating system environment
SESSION_KEY = os.environ.get('SESSION_KEY')

# # set the session key
app.secret_key = SESSION_KEY

# START OF CODE


@app.route('/')
def index():
    return render_template('index.template.html')


@app.route('/show_all')
def show_all():
    all_restaurants = client[DB_NAME].restaurants.find()
    return render_template('show_all.template.html', all_restaurants=all_restaurants)


@app.route('/create_new')
def create_new():
    return render_template('create_new.template.html', cloud_name=CLOUD_NAME, upload_preset=UPLOAD_PRESET)


@app.route('/create_new', methods=['POST'])
def process_create_new():
    restaurant_name = request.form.get('restaurant_name')
    address_street = request.form.get('address_street')
    address_unit = request.form.get('address_unit')
    postcode = request.form.get('postcode')
    # dob = request.form.get('dob')
    # dob = datetime.datetime.strptime(dob, "%Y-%m-%d")
    halal_cert = request.form.get('halal_cert')
    restaurant_type = request.form.get('restaurant_type')
    cuisines = []
    if request.form.get('japanese') == 'on':
        cuisines.append('Japanese')
    if request.form.get('english') == 'on':
        cuisines.append('English')
    if request.form.get('french') == 'on':
        cuisines.append('French')
    if request.form.get('italian') == 'on':
        cuisines.append('Italian')
    website = request.form.get('website')
    picture_url = request.form.get('uploaded_file_url')

    new_restaurant = {
        'restaurant_name': restaurant_name,
        'address_street': address_street,
        'address_unit': address_unit,
        'postcode': postcode,
        'halal_cert': halal_cert,
        'restaurant_type': restaurant_type,
        'cuisines': cuisines,
        'website': website,
        'picture_url': picture_url,
    }
    client[DB_NAME].restaurants.insert_one(new_restaurant)

    return redirect(url_for('show_all'))


@app.route('/<id>')
def show_restaurant(id):
    selected_restaurant = client[DB_NAME].restaurants.find_one({
        '_id': ObjectId(id)
    })
    return render_template('show_restaurant.template.html', restaurant=selected_restaurant)


@app.route('/update/<id>')
def update_restaurant(id):
    selected_restaurant = client[DB_NAME].restaurants.find_one({
        '_id': ObjectId(id)
    })
    return render_template('update_restaurant.template.html', restaurant=selected_restaurant, cloud_name=CLOUD_NAME, upload_preset=UPLOAD_PRESET)


@app.route('/update/<id>', methods=['POST'])
def process_update_restaurant(id):
    restaurant_name = request.form.get('restaurant_name')
    address_street = request.form.get('address_street')
    address_unit = request.form.get('address_unit')
    postcode = request.form.get('postcode')
    # dob = request.form.get('dob')
    # dob = datetime.datetime.strptime(dob, "%Y-%m-%d")
    halal_cert = request.form.get('halal_cert')
    restaurant_type = request.form.get('restaurant_type')
    cuisines = []
    if request.form.get('japanese') == 'on':
        cuisines.append('Japanese')
    if request.form.get('english') == 'on':
        cuisines.append('English')
    if request.form.get('french') == 'on':
        cuisines.append('French')
    if request.form.get('italian') == 'on':
        cuisines.append('Italian')
    website = request.form.get('website')
    picture_url = request.form.get('uploaded_file_url')

    client[DB_NAME].restaurants.update_one({
        '_id': ObjectId(id)
    }, {
        '$set': {
            'restaurant_name': restaurant_name,
            'address_street': address_street,
            'address_unit': address_unit,
            'postcode': postcode,
            'halal_cert': halal_cert,
            'restaurant_type': restaurant_type,
            'cuisines': cuisines,
            'website': website,
            'picture_url': picture_url,
        }
    })

    return redirect(url_for('show_all'))


@app.route('/delete/<id>')
def confirm_delete(id):
    selected_restaurant = client[DB_NAME].restaurants.find_one({
        '_id': ObjectId(id)
    })
    return render_template('confirm_delete.template.html', restaurant=selected_restaurant)


@app.route('/delete/<id>', methods=['POST'])
def process_confirm_delete(id):
    client[DB_NAME].restaurants.remove({
        '_id': ObjectId(id)
    })
    return redirect(url_for('show_all'))


@app.route('/<id>/review/new')
def create_review(id):
    selected_restaurant = client[DB_NAME].restaurants.find_one({
        '_id': ObjectId(id)
    })
    return render_template('create_review.template.html', restaurant=selected_restaurant)


@app.route('/<id>/review/new', methods=['POST'])
def process_create_review(id):
    selected_restaurant = client[DB_NAME].restaurants.find_one({
        '_id': ObjectId(id)
    })
    id = selected_restaurant['_id']

    review_name = request.form.get('review_name')
    review_food = request.form.get('review_food')
    review_text = request.form.get('review_text')

    client[DB_NAME].restaurants.update_one({
        '_id': ObjectId(id)
    }, {
        '$push': {
            'reviews': {
                '_id': ObjectId(),
                'review_name': review_name,
                'review_food': review_food,
                'review_text': review_text,
            }
        }
    })
    flash("Review added!")
    return redirect(url_for('show_restaurant', restaurant=selected_restaurant, id=id))


@app.route('/review/update/<review_id>')
def update_review(review_id):
    selected_restaurant = client[DB_NAME].restaurants.find_one({
        'reviews._id': ObjectId(review_id)
    })

    all_reviews = client[DB_NAME].restaurants.find_one({
        'reviews._id': ObjectId(review_id)
    }, {
        'reviews': {
            '$elemMatch': {
                '_id': ObjectId(review_id)
            }
        }
    })
    selected_review = all_reviews['reviews'][0]
    return render_template('update_review.template.html', restaurant=selected_restaurant, review=selected_review)


@app.route('/review/update/<review_id>', methods=['POST'])
def process_update_review(review_id):
    selected_restaurant = client[DB_NAME].restaurants.find_one({
        'reviews._id': ObjectId(review_id)
    })
    id=selected_restaurant['_id']
    review_name = request.form.get('review_name')
    review_food = request.form.get('review_food')
    review_text = request.form.get('review_text')
    client[DB_NAME].restaurants.update_one({
        'reviews._id': ObjectId(review_id)
    }, {
        '$set': {
            'reviews.$.review_name': review_name,
            'reviews.$.review_food': review_food,
            'reviews.$.review_text': review_text,
        }
    })
    return redirect(url_for('show_restaurant', id=id))

@app.route('/delete/review/<review_id>')
def confirm_delete_review(review_id):
    selected_restaurant = client[DB_NAME].restaurants.find_one({
        'reviews._id': ObjectId(review_id)
    })
    id=selected_restaurant['_id']
    return render_template('confirm_delete_review.template.html',id=id)


@app.route('/delete/review/<review_id>', methods=['POST'])
def process_confirm_delete_review(review_id):
    selected_restaurant = client[DB_NAME].restaurants.find_one({
        'reviews._id': ObjectId(review_id)
    })
    id=selected_restaurant['_id']
    client[DB_NAME].restaurants.update_one({
        'reviews._id': ObjectId(review_id)
    }, {
        '$pull': {
            'reviews':{
                '_id': ObjectId(review_id)
            }
        }
    })
    flash("Review deleted!")
    return redirect(url_for('show_restaurant',id=id))

# "magic code" -- boilerplate
if __name__ == '__main__':
    app.run(host=os.environ.get('IP'),
            port=int(os.environ.get('PORT')),
            debug=True)
    # app.run(host='0.0.0.0',
    #         port=8080,
    #         debug=True)
