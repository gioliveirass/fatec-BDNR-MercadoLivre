import connectBD as connectDB
from pprint import pprint

def findSort():
    mydb = connectDB.connect()
    mycol = mydb.produto
    print("\n=============================")
    print("==== TODOS OS PRODUTOS ======") 
    print("=============================\n")
    mydoc = mycol.find().sort("nome")
    for x in mydoc:
        pprint(x)

def insert(name, description):
    mydb = connectDB.connect()
    mycol = mydb.produto
    print("\n========================")
    print("=== PRODUTO INSERIDO ===") 
    print("========================\n")
    mydict = { "nome": name, "descricao": description }
    x = mycol.insert_one(mydict)
    pprint(x.inserted_id)
    print("Produto cadastrado com sucesso.")

def findQuery(name):
    mydb = connectDB.connect()
    mycol = mydb.produto
    print("\n=========================")
    print("==== PRODUTO BUSCADO ====") 
    print("=========================\n")
    myquery = { "nome": name }
    mydoc = mycol.find(myquery)
    for x in mydoc:
        pprint(x)

def update(name, newName):
    mydb = connectDB.connect()
    mycol = mydb.produto
    print("\n============================")
    print("==== PRODUTO ATUALIZADO ====") 
    print("============================\n")
    myquery = { "nome": name }
    newvalues = { "$set":   { "nome": newName } }
    mycol.update_one(myquery, newvalues)
    pprint("Produto atualizado com sucesso.")

def delete(name):
    mydb = connectDB.connect()
    mycol = mydb.produto
    print("\n==========================")
    print("==== PRODUTO DELETADO ====") 
    print("==========================\n")
    myquery = { "nome": name }
    mycol.delete_one(myquery)
    pprint("Produto deletado com sucesso.")