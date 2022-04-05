import connectBD as connectDB
from pprint import pprint

def findSort():
    mydb = connectDB.connect()
    mycol = mydb.vendedor
    print("\n=============================")
    print("==== TODOS OS VENDEDORES ====") 
    print("=============================\n")
    mydoc = mycol.find().sort("nome")
    for x in mydoc:
        pprint(x)

def insert(name, cpf):
    mydb = connectDB.connect()
    mycol = mydb.vendedor
    print("\n=========================")
    print("=== VENDEDOR INSERIDO ===") 
    print("=========================\n")
    mydict = { "nome": name, "cpf": cpf }
    x = mycol.insert_one(mydict)
    pprint(x.inserted_id)
    print("Vendedor cadastrado com sucesso.")

def findQuery(name):
    mydb = connectDB.connect()
    mycol = mydb.vendedor
    print("\n==========================")
    print("==== VENDEDOR BUSCADO ====") 
    print("==========================\n")
    myquery = { "nome": name }
    mydoc = mycol.find(myquery)
    for x in mydoc:
        pprint(x)

def update(name, newName):
    mydb = connectDB.connect()
    mycol = mydb.vendedor
    print("\n=============================")
    print("==== VENDEDOR ATUALIZADO ====") 
    print("=============================\n")
    myquery = { "nome": name }
    newvalues = { "$set":   { "nome": newName } }
    mycol.update_one(myquery, newvalues)
    pprint("Vendedor atualizado com sucesso.")

def delete(name):
    mydb = connectDB.connect()
    mycol = mydb.vendedor
    print("\n===========================")
    print("==== VENDEDOR DELETADO ====") 
    print("===========================\n")
    myquery = { "nome": name }
    mycol.delete_one(myquery)
    pprint("Vendedor deletado com sucesso.")