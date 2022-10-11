from Repository import Repo

# controller with CRUD operation

class Controller():

    def __init__(self):
        self.ControllerRepo=Repo()

    def ReadData(self):    #update with parameter
        return self.ControllerRepo.GetAll()
    
    def CreateData(self, fname, lname):
        self.ControllerRepo.InsertRow(fname,lname) 

    def DeleteData(self):  # update with parameter
        self.ControllerRepo.DeleteAll()


# test code
myController = Controller()
#myController.DeleteData()
myController.CreateData("Hans", "Hansen")
for r in myController.ReadData():
    print(r)