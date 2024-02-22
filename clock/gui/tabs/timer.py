import PyQt6.QtWidgets as qt
import PyQt6.QtGui as qt1
import PyQt6.QtCore as qt2
import winsound
class Timer (qt.QWidget):
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
        self.duration=0
        self.UserDuration=0
        self.progress=qt.QProgressBar()
        self.progress.setRange(0,100)
        self.progress.setValue(0)
        self.label=qt.QLabel()
        layout=qt.QVBoxLayout(self)
        layout.addWidget(self.start)
        layout.addWidget(self.pause)
        layout.addWidget(self.stop)
        layout.addWidget(self.label)
        layout.addWidget(self.progress)
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
        self.duration+=1
        self.progress.setValue(int((self.duration/self.UserDuration)*100))
        if self.duration==self.UserDuration:
            self.on_stop()
            winsound.PlaySound("data/sounds/1.wav",1)
    def on_start(self):
        if self.duration==0:
            StartTimer(self).exec()
        if not self.UserDuration==0:
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
        self.duration=0
        self.UserDuration=0
        self.progress.setValue(0)
        self.stop.setDisabled(True)
        self.pause.setDisabled(True)
        self.start.setDisabled(False)
class StartTimer(qt.QDialog):
    def __init__(self,p):
        super ().__init__(p)
        self.setWindowTitle(_("start timer"))
        self.hour=qt.QSpinBox()
        self.hour.setRange(0,100)
        self.hour.setValue(0)
        self.minut=qt.QSpinBox()
        self.minut.setRange(0,59)
        self.minut.setValue(0)
        self.second=qt.QSpinBox()
        self.second.setRange(1,59)
        self.second.setValue(5)
        self.star=qt.QPushButton(_("start"))
        self.star.clicked.connect(self.on_start)
        layout=qt.QFormLayout(self)
        layout.addRow(_("hours"),self.hour)
        layout.addRow(_("ninutes"),self.minut)
        layout.addRow(_("seconds"),self.second)
        layout.addWidget(self.star)
        self.p=p
    def on_start(self):
        minute=self.minut.value()*60
        hours=self.hour.value()*60*60
        self.p.UserDuration=self.second.value()+minute+hours
        self.close()