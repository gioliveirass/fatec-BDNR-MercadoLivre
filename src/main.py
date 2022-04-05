import controllers.userController as userController
import controllers.sellerController as sellerController

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