
from PyQt4 import QtCore, QtGui
from walk import *
import sys, re

try:
    _fromUtf8 = QtCore.QString.fromUtf8
except AttributeError:
    def _fromUtf8(s):
        return s

try:
    _encoding = QtGui.QApplication.UnicodeUTF8
    def _translate(context, text, disambig):
        return QtGui.QApplication.translate(context, text, disambig, _encoding)
except AttributeError:
    def _translate(context, text, disambig):
        return QtGui.QApplication.translate(context, text, disambig)



class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName(_fromUtf8("MainWindow"))
        MainWindow.setEnabled(True)
        MainWindow.resize(800, 600)
        MainWindow.setCursor(QtGui.QCursor(QtCore.Qt.ArrowCursor))
        MainWindow.setTabShape(QtGui.QTabWidget.Rounded)

        self.centralwidget = QtGui.QWidget(MainWindow)
        self.centralwidget.setObjectName(_fromUtf8("centralwidget"))

        self.lineEdit = QtGui.QLineEdit(self.centralwidget)
        self.lineEdit.setGeometry(QtCore.QRect(10, 10, 400, 20))
        self.lineEdit.setMinimumSize(QtCore.QSize(113, 20))
        font = QtGui.QFont()
        self.lineEdit.setFont(font)
        self.lineEdit.setObjectName(_fromUtf8("lineEdit"))
        self.lineEdit.returnPressed.connect(self.search_path)

        self.listWidget = QtGui.QListWidget(self.centralwidget)
        self.listWidget.setGeometry(QtCore.QRect(10, 50, 256, 501))
        self.listWidget.setObjectName(_fromUtf8("listWidget"))
        self.listWidget.itemClicked.connect(self.dir_click)

        self.listWidget_2 = QtGui.QListWidget(self.centralwidget)
        self.listWidget_2.setGeometry(QtCore.QRect(270, 50, 256, 501))
        self.listWidget_2.setObjectName(_fromUtf8("listWidget_2"))
        self.listWidget_2.itemClicked.connect(self.file_click)

        self.listView = QtGui.QListView(self.centralwidget)
        self.listView.setGeometry(QtCore.QRect(530, 50, 256, 501))
        self.listView.setObjectName(_fromUtf8("listView"))
        self.model = QtGui.QStandardItemModel()
        self.listView.setModel(self.model)

        self.label = QtGui.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(100, 30, 71, 20))
        self.label.setObjectName(_fromUtf8("label"))

        self.label_2 = QtGui.QLabel(self.centralwidget)
        self.label_2.setGeometry(QtCore.QRect(380, 30, 41, 16))
        self.label_2.setObjectName(_fromUtf8("label_2"))

        self.label_3 = QtGui.QLabel(self.centralwidget)
        self.label_3.setGeometry(QtCore.QRect(640, 30, 46, 13))
        self.label_3.setObjectName(_fromUtf8("label_3"))

        MainWindow.setCentralWidget(self.centralwidget)
        self.statusbar = QtGui.QStatusBar(MainWindow)
        self.statusbar.setLocale(QtCore.QLocale(QtCore.QLocale.English, QtCore.QLocale.UnitedStates))
        self.statusbar.setObjectName(_fromUtf8("statusbar"))
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(_translate("MainWindow", "Simple Dir Buster", None))
        self.lineEdit.setText(_translate("MainWindow", "Enter Path To Walk Through", None))
        self.label.setText(_translate("MainWindow", "Directories", None))
        self.label_2.setText(_translate("MainWindow", "Files", None))
        self.label_3.setText(_translate("MainWindow", "File Stats", None))

    def search_path(self):
        self.path = str(self.lineEdit.text())
        self.root_dirs, self.root_files = get_data(self.path)
        self.update_list()

    def dir_click(self, item):
        self.model.removeRows(0, self.model.rowCount())
        new_path = str(item.text())
        new_path = os.path.join(self.path, new_path)
        self.listWidget_2.clear()
        self.listWidget.clear()
        self.update_list(new_path)
        self.lineEdit.setText(new_path)
        

    def file_click(self, item):
        self.model.removeRows(0, self.model.rowCount())
        file_name = str(item.text())
        file_path = os.path.join(self.path, file_name)
        stats = os.stat(file_path)
        content = re.search(r'\((.*?)\)', str(stats)).group(1)
        rows = content.split(',')
        for row in rows:
            item = QtGui.QStandardItem(row)
            self.model.appendRow(item)

    def update_list(self, path=None):
        if path:
            self.path = path
        if self.root_dirs:
            for directory in self.root_dirs[self.path]:
                dir_item = QtGui.QListWidgetItem(directory)
                self.listWidget.addItem(dir_item)
        if self.root_files:
            for file in self.root_files[self.path]:
                file_item = QtGui.QListWidgetItem(file)
                self.listWidget_2.addItem(file_item)

if __name__ == "__main__":
    
    app = QtGui.QApplication(sys.argv)
    MainWindow = QtGui.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())

