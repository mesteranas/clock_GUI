import guiTools
import datetime
import pytz
from gui import jsonContorl
import PyQt6.QtWidgets as qt
import PyQt6.QtGui as qt1
import PyQt6.QtCore as qt2
class Clocks(qt.QWidget):
    def __init__(self,p):
        super().__init__()
        self.list=qt.QListWidget()
        self.list.setContextMenuPolicy(qt2.Qt.ContextMenuPolicy.CustomContextMenu)
        self.list.customContextMenuRequested.connect(self.context)
        qt1.QShortcut("delete",self).activated.connect(self.delete)
        self.tz=jsonContorl.get()
        self.add=qt.QPushButton(_("add new clock"))
        self.add.setDefault(True)
        self.add.clicked.connect(lambda:AddNewClock(self).exec())
        layout=qt.QVBoxLayout(self)
        layout.addWidget(self.list)
        layout.addWidget(self.add)
        self.config()
    def context(self):
        menu=qt.QMenu(self)
        delete=qt1.QAction(_("delete"),self)
        menu.addAction(delete)
        delete.triggered.connect(self.delete)
        menu.exec()
    def delete(self):
        try:
            del(self.tz[self.list.currentItem().text().split(" : ")[0]])
            jsonContorl.save(self.tz)
            self.config()
            guiTools.speak(_("deleted"))
        except Exception as e:
            guiTools.speak(_("error"))
    def config(self):
        self.list.clear()
        for key,value in self.tz.items():
            time=datetime.datetime.now(pytz.timezone(value)).strftime("%H : %M : %S %p")
            self.list.addItem("{} : {}".format(key,time))
class AddNewClock(qt.QDialog):
    def __init__(self,p):
        super().__init__(p)
        self.setWindowTitle(_("add new clock"))
        layout=qt.QVBoxLayout(self)
        self.choose=qt.QComboBox()
        self.choose.setAccessibleName(_("choose"))
        self.choose.addItems(pytz.common_timezones)
        layout.addWidget(self.choose)
        self.add=qt.QPushButton(_("add"))
        self.add.clicked.connect(self.on_add)
        self.p=p
        layout.addWidget(self.add)
    def on_add(self):
        self.p.tz[self.choose.currentText()]=self.choose.currentText()
        self.p.config()
        jsonContorl.save(self.p.tz)
        self.close()