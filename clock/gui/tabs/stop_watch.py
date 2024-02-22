import PyQt6.QtWidgets as qt
import PyQt6.QtGui as qt1
import PyQt6.QtCore as qt2
class StopWatch (qt.QWidget):
    def __init__(self,p):
        super().__init__()
        self.start=qt.QPushButton(_("start"))
        self.start.setDefault(True)
        self.start.clicked.connect(self.on_start)
        self.stop=qt.QPushButton(_("stop"))
        self.stop.setDefault(True)
        self.stop.clicked.connect(self.on_stop)
        self.pause=qt.QPushButton(_("pause"))
        self.pause.setDefault(True)
        self.pause.clicked.connect(self.on_pause)
        self.stop.setDisabled(True)
        self.pause.setDisabled(True)
        self.hours=0
        self.minutes=0
        self.seconds=0
        self.label=qt.QLabel()
        layout=qt.QVBoxLayout(self)
        layout.addWidget(self.start)
        layout.addWidget(self.pause)
        layout.addWidget(self.stop)
        layout.addWidget(self.label)
        self.timer=qt2.QTimer(self)
        self.timer.timeout.connect(self.timing)
    def timing(self):
        self.seconds+=1
        if self.seconds==60:
            self.minutes+=1
            self.seconds=0
            if self.minutes==60:
                self.minutes=0
                self.hours+=1
        self.label.setText(_("hours : {} menutes : {} secondes {}").format(str(self.hours),str(self.minutes),str(self.seconds)))
    def on_start(self):
        self.timer.start(1000)
        self.start.setDisabled(True)
        self.stop.setDisabled(False)
        self.pause.setDisabled(False)
    def on_pause(self):
        self.timer.stop()
        self.start.setDisabled(False)
        self.pause.setDisabled(True)
    def on_stop(self):
        self.timer.stop()
        self.seconds=0
        self.minutes=0
        self.hours=0
        self.stop.setDisabled(True)
        self.pause.setDisabled(True)
        self.start.setDisabled(False)