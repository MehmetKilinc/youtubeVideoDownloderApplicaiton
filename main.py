import sys
from PyQt5 import QtWidgets,QtGui

class pencere(QtWidgets.QWidget):

	def __init__(self):
		super().__init__()
		self.init_ui()

	def init_ui(self):
		self.link_alani = QtWidgets.QLineEdit()
		self.temizle = QtWidgets.QPushButton("temizle")
		self.indir = QtWidgets.QPushButton("indir")
		self.yazi_alani = QtWidgets.QLabel("")
		self.tanitim = QtWidgets.QLabel("indrime istediğiniz videonun linkini giriniz : ")

		vbox = QtWidgets.QVBoxLayout()
		vbox.addStretch()
		vbox.addWidget(self.tanitim)
		vbox.addWidget(self.link_alani)
		vbox.addWidget(self.temizle)
		vbox.addWidget(self.indir)
		vbox.addWidget(self.yazi_alani)
		vbox.addStretch()

		self.setLayout(vbox)
		self.temizle.clicked.connect(self.tikla)
		self.indir.clicked.connect(self.tikla)
		self.setGeometry(300,300,600,600)
		self.show()

	def tikla(self):

		sender = self.sender()
		if sender.text() == "temizle":
			self.link_alani.clear()
			self.yazi_alani.setText("")

		else:
			self.yazi_alani.setText("indiriliyor.......")
			from pytube import YouTube
			nesne = YouTube(self.link_alani.text())
			nesne = nesne.streams.get_highest_resolution()
			nesne.download()
			self.yazi_alani.setText("indirme tamamlandı")

app = QtWidgets.QApplication(sys.argv)
pencere = pencere()
sys.exit(app.exec_())

