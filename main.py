import sys
from PyQt5 import QtWidgets
from PyQt5.QtWidgets import QDialog, QApplication, QFileDialog
from PyQt5.uic import loadUi
from PyQt5.QtCore import pyqtSignal, pyqtSlot
from PyQt5.QtGui import QPixmap



class Login(QDialog):
    def __init__(self):
        super(Login, self).__init__()
        loadUi("login.ui", self)
        self.loginbutton.clicked.connect(self.gotologin)
        self.password.setEchoMode(QtWidgets.QLineEdit.Password)
        self.createaccbutton.clicked.connect(self.gotocreate)

    def gotologin(self):
        username = self.username.text()
        password = self.password.text()
        print("successfully logged in with username: ", username, "and password: ", password)

        main = MainPage()
        widget.addWidget(main)
        widget.resize(main.size())
        widget.setCurrentIndex(widget.currentIndex() + 1)

    def gotocreate(self):
        acc = CreateAcc()
        widget.addWidget(acc)
        widget.setCurrentIndex(widget.currentIndex() + 1)


class CreateAcc(QDialog):
    def __init__(self):
        super(CreateAcc, self).__init__()
        loadUi("signup.ui", self)
        self.signupbutton.clicked.connect(self.signupfunction)
        self.password.setEchoMode(QtWidgets.QLineEdit.Password)
        self.confirmpass.setEchoMode(QtWidgets.QLineEdit.Password)

    def signupfunction(self):
        username = self.username.text()
        if self.password.text() == self.confirmpass.text():
            password = self.password.text()
            print("successfully created an Account with username: ", username, "and password: ", password)
            login = Login()
            widget.addWidget(login)
            widget.setCurrentIndex(widget.currentIndex() + 1)
        else:
            print("The password is not equal")


class MainPage(QDialog):
    def __init__(self):
        super(MainPage, self).__init__()
        loadUi("boardpage.ui", self)
        self.accountbutton.clicked.connect(self.gotoaccountfunction)
        self.namedboardbutton.clicked.connect(self.namingboardfunction)
        self.deleteboardbutton.clicked.connect(self.deleteboardfunction)


    def namingboardfunction(self):
        namingboardtitle = NamingBoard()
        widget.addWidget(namingboardtitle)
        widget.resize(namingboardtitle.size())
        widget.setCurrentIndex(widget.currentIndex() + 1)

    def deleteboardfunction(self):
        board = self.boardlist.currentRow()
        item = self.boardlist.item(board)
        if item is None:
            return
        else:
            item = self.boardlist.takeItem(board)
            del item

    def gotoaccountfunction(self):
        account = Account()
        widget.addWidget(account)
        widget.resize(account.size())
        widget.setCurrentIndex(widget.currentIndex() + 1)


class NamingBoard(QDialog):
    def __init__(self):
        super(NamingBoard, self).__init__()
        loadUi("boardname.ui", self)
        self.okboardbutton.clicked.connect(self.addboardname)
        self.addmemberbutton.clicked.connect(self.addmembertolist)
        self.removememberbutton.clicked.connect(self.removememberfunction)

    def removememberfunction(self):
        member = self.memberlist.currentRow()
        item = self.memberlist.item(member)
        if item is None:
            return
        else:
            item = self.memberlist.takeItem(member)
            del item

    def addboardname(self):
        boardname = self.enterboardname.text()
        self.textEntered.emit(boardname)
        if boardname is not None:
            self.accept()

    def addmembertolist(self):
        member = self.memberlist.currentRow()
        item = self.addmember.text()
        if item is not None:
            self.memberlist.insertItem(member, item)
        self.addmember.clear()


class Account(QDialog):
    def __init__(self):
        super(Account, self).__init__()
        loadUi("account.ui", self)
        self.backtomainpagebutton.clicked.connect(self.gotomainpage)
        self.login = Login()
        self.usernamelabel.setText(self.login.username)
        self.passwordlabel.setText(self.login.username)

    def gotomainpage(self):
        main = MainPage()
        widget.addWidget(main)
        widget.resize(main.size())
        widget.setCurrentIndex(widget.currentIndex() + 1)


class Board(QDialog):
    def __init__(self):
        super(Board, self).__init__()
        loadUi("board.ui", self)
        self.addcolumnbutton.clicked.connect(self.addcolumnfunction)




class Card(QDialog):
    def __init__(self):
        super(Card, self).__init__()
        loadUi("card.ui", self)
        self.uploadIMGbutton.clicked.connect(self.uploadimagefunction)

    @pyqtSlot()
    def uploadimagefunction(self):
        # Open a file dialog and get the path to the selected image file
        filepath, _ = QFileDialog.getOpenFileName(self, "Open Image", "", "Image Files (*.png *.jpg *.jpeg *.bmp)")

        # Create a QPixmap object from the image file
        pixmap = QPixmap(filepath)

        # Set the pixmap to the label
        self.label.setPixmap(pixmap)

app = QApplication(sys.argv)
widget = QtWidgets.QStackedWidget()
trello = Login()
widget.addWidget(trello)
widget.resize(trello.size())
widget.show()
app.exec_()
