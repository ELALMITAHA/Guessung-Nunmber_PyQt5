#=================================
# @author :EL ALMI Taha
# Date    : 26/12/2021
#================================== 
import sys 
import random
from PyQt5.QtWidgets import (QApplication,QWidget,QLabel,QVBoxLayout,QGridLayout,
	QLineEdit,QGroupBox,QPushButton,QHBoxLayout,QListWidget,QListWidgetItem)
from PyQt5.QtCore import Qt 
from PyQt5.QtGui  import QFont 

class GuessNumberGui(QWidget): 
	""" Guessing Game with  PyQt5  """  
	def __init__(self) : 
		super().__init__()
		self.intializeUI() 

	def intializeUI(self) : 
		self.setWindowTitle(" Guessing game Number ")
		self.tentative_number = 0
		self.live_number  = 10
		self.max = 1000
		self.niveau_vie   = []
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
		self.vie_nbr_lbl = QLabel("")
		self.input_liedit = QLineEdit()
		# To test if the answer of user is correct 
		self.gues_btn = QPushButton("Guess")
		self.gues_btn.clicked.connect(self.guess)
		self.gues_btn.setEnabled(False)

		# Input group layout 
		input_grp_layout = QHBoxLayout() 
		input_grp_layout.addStretch(1)
		input_grp_layout.addWidget(self.input_liedit)
		input_grp_layout.addWidget(self.gues_btn)
		input_grp_layout.addStretch(1)
		input_grp.setLayout(input_grp_layout)

		# Label to give information to user 
		text_to_user = "Click on Play to start a new game "
		self.txt_to_user_lbl = QLabel(text_to_user)
		font = QFont('Times',15)
		font.setBold(True)
		font.setItalic(True)
		self.txt_to_user_lbl.setFont(font)
		self.txt_to_user_lbl.setAlignment(Qt.AlignCenter)
		self.hint_lbl = QLabel("")
		self.hint_lbl.setFont(font)
		self.hint_lbl.setAlignment(Qt.AlignCenter)

		# Button to begin and stop playing 
		playexit_gbp = QGroupBox()
		# To get number from user 
		self.play_btn = QPushButton(" Play Game ")
		self.play_btn.clicked.connect(self.play)
		exit_btn = QPushButton(" Exit Game ")
		exit_btn.clicked.connect(self.exit)

		# Récapulative de toutes les tentative 
		self.list_tentative = QListWidget()


		# To begin and stop game 
		playexit_gbp_layout = QHBoxLayout()
		playexit_gbp_layout.addStretch(1)
		playexit_gbp_layout.addWidget(self.play_btn)
		playexit_gbp_layout.addWidget(exit_btn)
		playexit_gbp_layout.addStretch(1)
		playexit_gbp.setLayout(playexit_gbp_layout)

		# Set global layout 
		win_layout = QVBoxLayout()
		win_layout.addWidget(title_lbl)
		win_layout.addWidget(self.vie_nbr_lbl)
		win_layout.addWidget(input_grp)
		win_layout.addWidget(self.txt_to_user_lbl)
		win_layout.addWidget(self.hint_lbl)
		win_layout.addWidget(self.list_tentative)
		win_layout.addWidget(playexit_gbp)

		self.setLayout(win_layout)

	def play(self): 
		self.gues_btn.setEnabled(True)
		self.txt_to_user_lbl.setText(f" Guess a number beteween 1 and {self.max} ")
		self.target = random.randint(1, self.max)
		self.niveau_vie = ["*"]*self.live_number
		self.vie_nbr_lbl.setText(" ".join(str(x) for x in self.niveau_vie))
		
	def exit(self) : 
		self.gues_btn.setEnabled(False)
		self.txt_to_user_lbl.setText(" Click on Play to start a new game ")
		self.hint_lbl.clear()
		self.input_liedit.clear()
		self.tentative_number = 0
		self.play_btn.setEnabled(True)

	def guess(self): 

		self.niveau_vie.remove("*")
		self.vie_nbr_lbl.setText("Nombre de vies restantes : "+" ".join(str(x) for x in self.niveau_vie))
		listWidgetItem = QListWidgetItem(" ")

		if len(self.niveau_vie) >= 0 :
			self.play_btn.setEnabled(False)
			try : 
				choice  = int(self.input_liedit.text())			
				if self.target != choice : 
					self.txt_to_user_lbl.setText(" Wrong Guess ! Try Again ")
					self.tentative_number += 1
					self.input_liedit.clear()

					if self.target > choice :
						self.hint_lbl.setText(" C'est plus  ! ") 
						self.list_tentative.addItem(f"c'est plus grand que :{choice}")
					else : 
						self.hint_lbl.setText(" C'est moins ! ")
						self.list_tentative.addItem(f"c'est plus petit que :{choice}")
				else :
					self.txt_to_user_lbl.setText(f"Bravo !! ")
					self.hint_lbl.setText(f"Vous avez trouvé en {self.tentative_number} tentatives ")
			except ValueError : 
				self.txt_to_user_lbl.setText(" Your value is not a number  ")
		else : 
			self.txt_to_user_lbl.setText("Dommage vous avez perdu !  ")
			self.hint_lbl.setText(f"Le nombre à deviner était :{self.target}") 


if __name__ == "__main__": 
	app = QApplication([])
	test = GuessNumberGui()
	#app.setStyleSheet(style_sheet)
	app.exec_()