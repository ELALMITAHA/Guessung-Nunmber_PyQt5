#=================================
# @author :EL ALMI Taha
# Date    : 26/12/2021
#================================== 
import sys 
import random
from PyQt5.QtWidgets import (QApplication,QWidget,QLabel,QVBoxLayout,QGridLayout,
	QLineEdit,QGroupBox,QPushButton,QHBoxLayout,QCalendarWidget)
from PyQt5.QtCore import Qt 
from PyQt5.QtGui  import QFont 


class GuessNumberGui(QWidget): 
	""" Guessing Game with  PyQt5  """  
	def __init__(self) : 
		super().__init__()
		self.intializeUI() 

	def intializeUI(self) : 
		self.setWindowTitle(" Guessing game Number ")
		win_xposition = 100
		win_yposition = 100
		win_largeur   = 450
		win_longueur  = 400		 
		self.setGeometry(win_xposition,win_yposition,win_largeur, win_longueur)
		self.setWidget()

		self.show()

	def setWidget(self) : 

		

		# Set and custumize Title for Gui 
		title_lbl = QLabel("Guessing Game")
		font = QFont('Times',20)
		title_lbl.setFont(font)
		title_lbl.setAlignment(Qt.AlignCenter)
		
		# Input and output groupe 
		input_grp = QGroupBox()
		# To get number from user 
		input_liedit = QLineEdit()
		# To test if the answer of user is correct 
		gues_btn = QPushButton("Guess")

		# Input group layout 
		input_grp_layout = QHBoxLayout() 
		input_grp_layout.addStretch(1)
		input_grp_layout.addWidget(input_liedit)
		input_grp_layout.addWidget(gues_btn)
		input_grp_layout.addStretch(1)
		input_grp.setLayout(input_grp_layout)

		# Label to give information to user 
		text_to_user = "Click on Play to start a new game "
		txt_to_user_lbl = QLabel(text_to_user)
		font = QFont('Times',15)
		font.setBold(True)
		font.setItalic(True)
		txt_to_user_lbl.setFont(font)
		txt_to_user_lbl.setAlignment(Qt.AlignCenter)

		# Button to begin and stop playing 
		playexit_gbp = QGroupBox()
		# To get number from user 
		play_btn = QPushButton(" Play Game ")
		exit_btn = QPushButton(" Exit Game ")

		# To test if the answer of user is correct 
		playexit_gbp_layout = QHBoxLayout()
		playexit_gbp_layout.addStretch(1)
		playexit_gbp_layout.addWidget(play_btn)
		playexit_gbp_layout.addWidget(exit_btn)
		playexit_gbp_layout.addStretch(1)
		playexit_gbp.setLayout(playexit_gbp_layout)


		# Set global layout 
		win_layout = QVBoxLayout()
		win_layout.addWidget(title_lbl)
		win_layout.addWidget(input_grp)
		win_layout.addWidget(txt_to_user_lbl)
		win_layout.addWidget(playexit_gbp)

		self.setLayout(win_layout)


if __name__ == "__main__": 
	app = QApplication([])
	test = GuessNumberGui()
	#app.setStyleSheet(style_sheet)
	app.exec_()