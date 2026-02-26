from typing import List
from flask import Flask, render_template
from pymongo.mongo_client import MongoClient
from pymongo.server_api import ServerApi

app = Flask(__name__)
URI = "mongodb+srv://adrian2718:iGcAvdsbzxhhW7VE@library-db.njhmomj.mongodb.net/?appName=library-db"

client = MongoClient(URI, server_api=ServerApi('1'))

db = client["library"]
collection = db["books"]


data = [
    {
        "name": "Intro to Linear Algebra",
        "description": "An introductory linear algebra book " +
        "presents the fundamental concepts of vectors, matrices, and linear " +
        "transformations, building the mathematical framework used to solve systems of "+
        "equations and model real-world phenomena."
    },
    {
        "name": "Advanced Python",
        "description": "An advanced Python book explores high-level topics such as "+
        "object-oriented design, concurrency, performance optimization, metaprogramming,"+
        "and best practices for building scalable, production-ready applications."
    }
]

@app.route("/")
def home():
    return render_template("index.html")


@app.route("/welcome")
def welcome():
    return "Hello World!"

@app.route("/search/<query>")
def search_books(query):
    return [{
        "name": entry["name"],
        "description": entry["description"],
        "authors": entry["authors"],
        "cover_url": entry["cover_url"]
        } for entry in collection.find() if query_in_book_result(query, entry)]

def query_in_book_result(query: str, book_entry: dict):
    # return query.lower() in book_entry["name"].lower() or query.lower() in book_entry["description"].lower()
    attributes = ["name", "description", "authors"]
    return any([query.lower() in book_entry[attr].lower() for attr in attributes])
    


app.run(host="0.0.0.0", port="5050")