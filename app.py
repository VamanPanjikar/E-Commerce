from flask import Flask, render_template, request, redirect, url_for, jsonify
from flask_pymongo import PyMongo
from bson.json_util import dumps

app = Flask(__name__)

# MongoDB Configuration
app.config["MONGO_URI"] = "mongodb://localhost:27017/ecommerce"
mongo = PyMongo(app)

# Homepage
@app.route("/")
def home():
    products = mongo.db.products.find()
    return render_template("index.html", products=products)

# Add Product
@app.route("/add-product", methods=["POST"])
def add_product():
    data = request.form
    mongo.db.products.insert_one({
        "name": data.get("name"),
        "price": float(data.get("price")),
        "category": data.get("category"),
    })
    return redirect(url_for("home"))

# Recommend Products (Dummy Example)
@app.route("/recommend/<category>")
def recommend(category):
    recommended = mongo.db.products.find({"category": category})
    return render_template("recommend.html", products=recommended)

# API Endpoint to Fetch Products (JSON)
@app.route("/api/products")
def api_products():
    products = mongo.db.products.find()
    return dumps(products)

if __name__ == "__main__":
    app.run(debug=True)
