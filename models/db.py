from pymongo import MongoClient

client = MongoClient("mongodb://localhost:27017/")
db = client["ecommerce"]

def add_product(product):
    return db.products.insert_one(product)

def get_products():
    return db.products.find()

def recommend_products(category):
    return db.products.find({"category": category})
