from pymongo import MongoClient

def connect():
    client = MongoClient("mongodb+srv://<user>:<password>@<url>")
    mydb = client.MercadoLivre
    return mydb