import connectBD as connectDB
from pprint import pprint

def findSort():
    mydb = connectDB.connect()
    mycol = mydb.compra
    print("\n============================")
    print("==== TODAS AS COMPRAS =======") 
    print("=============================\n")
    mydoc = mycol.find().sort("data")
    for x in mydoc:
        pprint(x)

def insert(user, sellerName, date, price):
    mydb = connectDB.connect()
    mycol = mydb.compra
    print("\n=======================")
    print("=== COMPRA INSERIDA ===") 
    print("=======================\n")
    mydict = { "usuario": user, "vendedor": {"nome": sellerName}, "data": date, "precoTotal": price }
    x = mycol.insert_one(mydict)
    pprint(x.inserted_id)
    print("Compra cadastrada com sucesso.")

def findQuery(id):
    mydb = connectDB.connect()
    mycol = mydb.compra
    print("\n========================")
    print("==== COMPRA BUSCADA ====") 
    print("========================\n")
    myquery = { "_id": id }
    mydoc = mycol.find(myquery)
    for x in mydoc:
        pprint(x)

def update(id, newPrice):
    mydb = connectDB.connect()
    mycol = mydb.compra
    print("\n===========================")
    print("==== COMPRA ATUALIZADA ====") 
    print("===========================\n")
    myquery = { "_id": id }
    newvalues = { "$set":   { "preco_total": newPrice } }
    mycol.update_one(myquery, newvalues)
    pprint("Compra atualizada com sucesso.")

def delete(id):
    mydb = connectDB.connect()
    mycol = mydb.compra
    print("\n=========================")
    print("==== COMPRA DELETADA ====") 
    print("=========================\n")
    myquery = { "_id": id }
    mycol.delete_one(myquery)
    pprint("Compra deletado com sucesso.")