import controllers.userController as userController

userController.findSort()
userController.insert("Giovana", "000.000.000-00")
userController.findQuery("Giovana")
userController.update("Giovana", "Thais")
userController.findQuery("Thais")
userController.delete("Thais")
userController.findSort()