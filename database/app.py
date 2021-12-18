from PyQt5 import QtWidgets, uic              # loading the packages
import sys

class UI(QtWidgets.QMainWindow):              # Custom Class UI extends QMainWindow
    def __init__(self):                       # A no argument Constructor
        super(UI,self).__init__()             # required code to super class
        uic.loadUi('database/app.ui',self)             # load the UI designed from address
        self.show()                           # if successful, show the UI

app = QtWidgets.QApplication(sys.argv)        # Code to Activate the Application 
window = UI()                                 # a new object UI class we created above
app.exec_()                                   # create an infinite loop, so you can see the app 
                                              # window until you close it yourself