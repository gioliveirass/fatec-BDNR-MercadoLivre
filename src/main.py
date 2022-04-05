from bson.objectid import ObjectId
import controllers.userController as userController
import controllers.sellerController as sellerController
import controllers.productController as productController
import controllers.purchaseController as purchaseController

# USUÁRIO
userController.findSort()
userController.insert("Marta", "000.000.000-00")
userController.findQuery("Marta")
userController.update("Marta", "Thais")
userController.findQuery("Thais")
userController.delete("Thais")
userController.findSort()

# VENDEDOR
sellerController.findSort()
sellerController.insert("Mariana", "111.111.111-11")
sellerController.findQuery("Mariana")
sellerController.update("Mariana", "Roberta")
sellerController.findQuery("Roberta")
sellerController.delete("Roberta")

# PRODUTO
productController.findSort()
productController.insert("Tablet", "Cor: Rosa")
productController.findQuery("Tablet")
productController.update("Tablet", "Microfone")
productController.findQuery("Microfone")
productController.delete("Microfone")

# COMPRA
purchaseController.findSort()
purchaseController.insert(ObjectId('62288cf1357558f69302d8e2'), "Rosa", "2022-04-05T07:55:00.000+00:00", 1200)
purchaseController.update(ObjectId('622891b93575b5f69302d8ea'), 1500)
purchaseController.findQuery(ObjectId('622891b93575b5f69302d8ea'))
purchaseController.delete(ObjectId('624c5554c9638d1d3848deea'))