from PyQt5 import QtWidgets, QtCore, QtGui
from PyQt5.QtWidgets import QMainWindow, QApplication
from Ui_Splash import Ui_SplashWindow
from login import Giris

counter = 0
#yüklenme sayfasını tanımla
class Splash(QMainWindow):
    def __init__(self):
        super(Splash, self).__init__()
        self.ui = Ui_SplashWindow()
        self.ui.setupUi(self)
        self.show()

        #köşeleri kaldır
        self.setWindowFlag(QtCore.Qt.FramelessWindowHint)
        self.setAttribute(QtCore.Qt.WA_TranslucentBackground)
        #gölge efekti
        self.shadow = QtWidgets.QGraphicsDropShadowEffect(self)
        self.shadow.setBlurRadius(20)
        self.shadow.setXOffset(0)
        self.shadow.setYOffset(0)
        self.shadow.setColor(QtGui.QColor(0,0,0,68))
        self.ui.dropShadowFrame.setGraphicsEffect(self.shadow)
        #zamanlayıcı başlatma
        self.timer = QtCore.QTimer()
        self.timer.timeout.connect(self.progressBar)
        #milisaniyelik zaman ayarı
        self.timer.start(35)
        
        #inital text
        
        #yazilari değiş
        QtCore.QTimer.singleShot(15000, lambda: self.ui.lbl_spTitle_2.setText("Try connect to cloud"))
        QtCore.QTimer.singleShot(1500, lambda: self.ui.lbl_spTitle_2.setText("Installing values"))
        QtCore.QTimer.singleShot(1600, lambda: self.ui.lbl_spTitle_2.setText("Collecting data"))
        QtCore.QTimer.singleShot(2000, lambda: self.ui.lbl_spTitle_2.setText("Runing..."))

        #yüklenme barını ayarla
    def progressBar(self):
        global counter
        self.ui.progressBar.setValue(counter)

        #close timer
        if counter > 1:
            self.timer.stop()
            #login sayfasını aç
            self.giris = Giris()
            self.giris.show()

            #close splash window
            self.close()
        #INCREASE COUNTER
        counter += 1


if __name__ == "__main__":
    import sys
    uygulama = QApplication(sys.argv) 
    splash = Splash()
    splash.show()
    uygulama.exit(uygulama.exec_())
