import sys
import json
from PyQt5.QtWidgets import *
from PyQt5.QtGui import QIcon, QPixmap
import login_window
submit_msg = ""
from chat_utils import *
error = False

class register(QWidget):

    def __init__(self, socket):
        super().__init__()

        self.socket = socket
        #called on our next method which adds everything to the window
        self.register_window()

    def register_window(self):
        global submit_error
        global submit_msg

        #create title and dimensions
        self.title = 'ET CHAT'
        self.left = 500
        self.top = 200
        self.width = 250
        self.height = 150

        #create widgets to display
        greeting = QLabel('Please Register Your New Account Below' + '\n')
        user_label = QLabel('New Username:')
        self.user_input = QLineEdit()
        pw_label = QLabel('New Password:')
        self.pw_input = QLineEdit()
        self.pw_input.setEchoMode(self.pw_input.Password)
        cpw_label = QLabel('Confirm New Password:')
        self.cpw_input = QLineEdit()
        self.cpw_input.setEchoMode(self.cpw_input.Password)
        return_button = QPushButton('back to login')
        submit_button = QPushButton('submit')
        self.submit_msg = ""

        #add widgets and buttons to our layout
        self.layout = QFormLayout()
        self.layout.addRow(greeting)
        self.layout.addRow(user_label, self.user_input)
        self.layout.addRow(pw_label, self.pw_input)
        self.layout.addRow(cpw_label, self.cpw_input)
        self.layout.addRow(return_button, submit_button)

        #what to do if buttons clicked
        return_button.clicked.connect(self.back_to_login)
        submit_button.clicked.connect(self.submitlogin)

        #set the layout the window and display it
        self.setLayout(self.layout)
        self.setWindowTitle(self.title)
        self.setGeometry(self.left, self.top, self.width, self.height)
#        self.show()

    def back_to_login(self):
        self.l = login_window.login(self.socket)
        self.l.show()
        self.hide()

    def send(self,msg):
        mysend(self.socket,msg)

    def recv(self) :
        return myrecv(self.socket)

    def submitlogin(self):
        global submit_msg
        global error

        register_info = json.dumps({"action":"register","name":self.user_input.text(), "password":self.pw_input.text(), "cpassword": self.cpw_input.text()})
        self.send(register_info)
        response = json.loads(self.recv())

        if response["status"] == "success":
            if len(self.submit_msg) == 0 or self.submit_msg != response["msg"]:
                self.submit_msg = response["msg"]
                submit_btn_response = QLabel(self.submit_msg)
                submit_btn_response.setStyleSheet("color: green;")
                self.layout.addRow(submit_btn_response)

        elif response["status"] == "error":
            if len(self.submit_msg) == 0 or self.submit_msg != response["errormsg"]:
                self.submit_msg = response["errormsg"]
                submit_btn_response = QLabel(self.submit_msg)
                submit_btn_response.setStyleSheet("color: red;")
                self.layout.addRow(submit_btn_response)

if __name__ == '__main__':
    register_app = QApplication(sys.argv)
    start_registration = register()
    start_registration.show()
    sys.exit(register_app.exec_())
