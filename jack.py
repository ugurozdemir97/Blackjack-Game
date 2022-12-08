from PyQt5 import QtCore, QtGui, QtWidgets


class Screen(object):
    def __init__(self):
        self.dealer_deck = None
        self.horizontalLayoutWidget_2 = None
        self.hidden_card = None
        self.hands = None
        self.player_deck = None
        self.show_winner = None
        self.horizontalLayoutWidget = None
        self.play_page = None
        self.play_back = None
        self.about_back = None
        self.about_page = None
        self.rules_back = None
        self.checkBox = None
        self.rules_page = None
        self.stand = None
        self.again = None
        self.hit = None
        self.about = None
        self.rules = None
        self.play = None
        self.button_holder = None
        self.verticalLayoutWidget_2 = None
        self.main_page = None
        self.stackedWidget = None
        self.centralwidget = None

    def setupUi(self, Window):
        Window.setObjectName("Window")
        Window.resize(840, 649)
        Window.setFixedSize(840, 649)
        Window.setWindowIcon(QtGui.QIcon('cards.png'))
        self.centralwidget = QtWidgets.QWidget(Window)
        self.centralwidget.setStyleSheet("")
        self.centralwidget.setObjectName("centralwidget")
        self.stackedWidget = QtWidgets.QStackedWidget(self.centralwidget)
        self.stackedWidget.setGeometry(QtCore.QRect(0, 0, 841, 651))
        self.stackedWidget.setObjectName("stackedWidget")
        self.main_page = QtWidgets.QWidget()
        self.main_page.setStyleSheet("#main_page {image: url(:/MenuImages/Menu Images/MainMenu.png);}")
        self.main_page.setObjectName("main_page")
        self.verticalLayoutWidget_2 = QtWidgets.QWidget(self.main_page)
        self.verticalLayoutWidget_2.setGeometry(QtCore.QRect(70, 340, 161, 251))
        self.verticalLayoutWidget_2.setObjectName("verticalLayoutWidget_2")
        self.button_holder = QtWidgets.QVBoxLayout(self.verticalLayoutWidget_2)
        self.button_holder.setContentsMargins(0, 0, 0, 0)
        self.button_holder.setSpacing(35)
        self.button_holder.setObjectName("button_holder")
        self.play = QtWidgets.QPushButton(self.verticalLayoutWidget_2)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.play.sizePolicy().hasHeightForWidth())
        self.play.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setFamily("Georgia")
        font.setPointSize(14)
        font.setBold(True)
        font.setWeight(75)
        self.play.setFont(font)
        self.play.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.play.setStyleSheet("QPushButton {border-radius: 10px; background-color:  rgb(0, 160, 240); "
                                "border: 2px solid yellow; color: rgb(0, 0, 50);}\n"
                                "QPushButton:hover {border-radius: 10px; background-color: rgb(0, 180, 255); "
                                "border: 1px solid white;}")
        self.play.setObjectName("play")
        self.button_holder.addWidget(self.play)
        self.rules = QtWidgets.QPushButton(self.verticalLayoutWidget_2)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.rules.sizePolicy().hasHeightForWidth())
        self.rules.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setFamily("Georgia")
        font.setPointSize(14)
        font.setBold(True)
        font.setWeight(75)
        self.rules.setFont(font)
        self.rules.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.rules.setStyleSheet("QPushButton {border-radius: 10px; background-color: rgb(180, 0, 0); "
                                 "border: 1px solid rgb(195, 0, 0); color: white;}\n\n"
                                 "QPushButton:hover {border-radius: 10px; background-color: rgb(220, 0, 0); "
                                 "border: 1px solid white;}")
        self.rules.setObjectName("rules")
        self.button_holder.addWidget(self.rules)
        self.about = QtWidgets.QPushButton(self.verticalLayoutWidget_2)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.about.sizePolicy().hasHeightForWidth())
        self.about.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setFamily("Georgia")
        font.setPointSize(14)
        font.setBold(True)
        font.setWeight(75)
        self.about.setFont(font)
        self.about.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.about.setStyleSheet("QPushButton {border-radius: 10px; background-color: rgb(255, 179, 0); "
                                 "border: 1px solid yellow; color: rgb(0, 0, 127);}\n"
                                 "QPushButton:hover {border-radius: 10px; background-color: rgb(255, 234, 0); "
                                 "border: 1px solid white;}")
        self.about.setObjectName("about")
        self.button_holder.addWidget(self.about)
        self.checkBox = QtWidgets.QCheckBox(self.main_page)
        self.checkBox.setGeometry(QtCore.QRect(70, 290, 201, 31))
        font = QtGui.QFont()
        font.setFamily("Georgia")
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.checkBox.setFont(font)
        self.checkBox.setStyleSheet("color: rgb(255, 255, 255);\n")
        self.checkBox.setObjectName("checkBox")
        self.stackedWidget.addWidget(self.main_page)
        self.rules_page = QtWidgets.QWidget()
        self.rules_page.setStyleSheet("#rules_page {image: url(:/MenuImages/Menu Images/HowToPlayMenu.png);}\n")
        self.rules_page.setObjectName("rules_page")
        self.rules_back = QtWidgets.QPushButton(self.rules_page)
        self.rules_back.setGeometry(QtCore.QRect(30, 540, 81, 81))
        font = QtGui.QFont()
        font.setFamily("Georgia")
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.rules_back.setFont(font)
        self.rules_back.setStyleSheet("QPushButton {\n"
                                      "border-radius: 40px;\n"
                                      "color: white;\n"
                                      "background-color: rgb(180, 0, 0);\n"
                                      "border: 5px solid rgb(120, 0, 0);}\n"
                                      "QPushButton:hover {\n"
                                      "background-color: rgb(200, 0, 0);\n"
                                      "border: 5px solid rgb(255, 0, 0);}")
        self.rules_back.setObjectName("rules_back")
        self.stackedWidget.addWidget(self.rules_page)
        self.about_page = QtWidgets.QWidget()
        self.about_page.setStyleSheet("#about_page {image: url(:/MenuImages/Menu Images/AboutMenu.png);}\n")
        self.about_page.setObjectName("about_page")
        self.about_back = QtWidgets.QPushButton(self.about_page)
        self.about_back.setGeometry(QtCore.QRect(30, 540, 81, 81))
        font = QtGui.QFont()
        font.setFamily("Georgia")
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.about_back.setFont(font)
        self.about_back.setStyleSheet("QPushButton {\n"
                                      "border-radius: 40px;\n"
                                      "color: white;\n"
                                      "background-color: rgb(180, 0, 0);\n"
                                      "border: 5px solid rgb(120, 0, 0);}\n"
                                      "QPushButton:hover {\n"
                                      "background-color: rgb(200, 0, 0);\n"
                                      "border: 5px solid rgb(255, 0, 0);}")
        self.about_back.setObjectName("about_back")
        self.stackedWidget.addWidget(self.about_page)
        self.play_page = QtWidgets.QWidget()
        self.play_page.setStyleSheet("#play_page {image: url(:/MenuImages/Menu Images/PlayMenu.png);}")
        self.play_page.setObjectName("play_page")
        self.play_back = QtWidgets.QPushButton(self.play_page)
        self.play_back.setGeometry(QtCore.QRect(30, 540, 81, 81))
        font = QtGui.QFont()
        font.setFamily("Georgia")
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.play_back.setFont(font)
        self.play_back.setStyleSheet("QPushButton {\n"
                                     "border-radius: 40px;\n"
                                     "color: white;\n"
                                     "background-color: rgb(180, 0, 0);\n"
                                     "border: 5px solid rgb(120, 0, 0);}\n"
                                     "QPushButton:hover {\n"
                                     "background-color: rgb(200, 0, 0);\n"
                                     "border: 5px solid rgb(255, 0, 0);}")
        self.play_back.setObjectName("play_back")
        self.horizontalLayoutWidget = QtWidgets.QWidget(self.play_page)
        self.horizontalLayoutWidget.setGeometry(QtCore.QRect(50, 270, 741, 211))
        self.horizontalLayoutWidget.setObjectName("horizontalLayoutWidget")
        self.player_deck = QtWidgets.QHBoxLayout(self.horizontalLayoutWidget)
        self.player_deck.setContentsMargins(0, 0, 0, 0)
        self.player_deck.setObjectName("player_deck")
        self.horizontalLayoutWidget_2 = QtWidgets.QWidget(self.play_page)
        self.horizontalLayoutWidget_2.setGeometry(QtCore.QRect(50, 50, 741, 211))
        self.horizontalLayoutWidget_2.setObjectName("horizontalLayoutWidget_2")
        self.dealer_deck = QtWidgets.QHBoxLayout(self.horizontalLayoutWidget_2)
        self.dealer_deck.setContentsMargins(0, 0, 0, 0)
        self.dealer_deck.setObjectName("dealer_deck")
        self.hidden_card = QtWidgets.QLabel(self.horizontalLayoutWidget_2)
        self.hidden_card.setStyleSheet("#hidden_card {image: url(:/HiddenCard/Card Images/Hidden.png);}")
        self.hidden_card.setText("")
        self.hidden_card.setObjectName("hidden_card")
        self.dealer_deck.addWidget(self.hidden_card)
        self.hands = QtWidgets.QLabel(self.play_page)
        self.hands.setGeometry(QtCore.QRect(250, 490, 321, 111))
        font = QtGui.QFont()
        font.setFamily("Georgia")
        font.setPointSize(17)
        font.setBold(True)
        font.setWeight(75)
        self.hands.setFont(font)
        self.hands.setStyleSheet("color: rgb(255, 255, 255);")
        self.hands.setAlignment(QtCore.Qt.AlignRight | QtCore.Qt.AlignTrailing | QtCore.Qt.AlignVCenter)
        self.hands.setObjectName("hands")
        self.show_winner = QtWidgets.QLabel(self.play_page)
        self.show_winner.setGeometry(QtCore.QRect(0, 0, 841, 651))
        font = QtGui.QFont()
        font.setFamily("Georgia")
        font.setPointSize(65)
        font.setBold(True)
        font.setWeight(75)
        self.show_winner.setFont(font)
        self.show_winner.setAlignment(QtCore.Qt.AlignCenter)
        self.show_winner.setObjectName("show_winner")
        self.stand = QtWidgets.QPushButton(self.play_page)
        self.stand.setGeometry(QtCore.QRect(690, 530, 119, 42))
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.stand.sizePolicy().hasHeightForWidth())
        self.stand.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setFamily("Georgia")
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.stand.setFont(font)
        self.stand.setStyleSheet("QPushButton {border-radius: 10px; background-color: "
                                 "rgb(0, 160, 240); border: 2px solid yellow; color: rgb(0, 0, 50);}\n"
                                 "QPushButton:hover {border-radius: 10px; background-color: rgb(0, 180, 255); "
                                 "border: 1px solid white;}")
        self.stand.setObjectName("stand")
        self.hit = QtWidgets.QPushButton(self.play_page)
        self.hit.setGeometry(QtCore.QRect(690, 580, 119, 41))
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.hit.sizePolicy().hasHeightForWidth())
        self.hit.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setFamily("Georgia")
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.hit.setFont(font)
        self.hit.setStyleSheet("QPushButton {border-radius: 10px; background-color: rgb(255, 179, 0);"
                               "border: 1px solid yellow; color: rgb(0, 0, 127);}\n"
                               "QPushButton:hover {border-radius: 10px; background-color: rgb(255, 234, 0);"
                               "border: 1px solid white;}")
        self.hit.setObjectName("hit")
        self.again = QtWidgets.QPushButton(self.play_page)
        self.again.setGeometry(QtCore.QRect(30, 30, 81, 81))
        font = QtGui.QFont()
        font.setFamily("Georgia")
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.again.setFont(font)
        self.again.setStyleSheet("QPushButton {\n"
                                 "border-radius: 40px;\n"
                                 "color: black;\n"
                                 "background-color: rgb(231, 127, 0);\n"
                                 "border: 5px solid rgb(255, 170, 0);}\n"
                                 "QPushButton:hover {\n"
                                 "background-color: rgb(255, 170, 0);\n"
                                 "border: 5px solid rgb(255, 255, 0);}")
        self.again.setObjectName("again")
        self.horizontalLayoutWidget.raise_()
        self.horizontalLayoutWidget_2.raise_()
        self.hands.raise_()
        self.show_winner.raise_()
        self.play_back.raise_()
        self.again.raise_()
        self.stand.raise_()
        self.hit.raise_()
        self.stackedWidget.addWidget(self.play_page)
        Window.setCentralWidget(self.centralwidget)

        self.retranslateUi(Window)
        self.stackedWidget.setCurrentIndex(3)
        QtCore.QMetaObject.connectSlotsByName(Window)

    def retranslateUi(self, Window):
        _translate = QtCore.QCoreApplication.translate
        Window.setWindowTitle(_translate("Window", "Blackjack"))
        self.play.setText(_translate("Window", "PLAY"))
        self.rules.setText(_translate("Window", "RULES"))
        self.about.setText(_translate("Window", "ABOUT"))
        self.checkBox.setText(_translate("Window", "   Card counting"))
        self.rules_back.setText(_translate("Window", "BACK"))
        self.about_back.setText(_translate("Window", "BACK"))
        self.play_back.setText(_translate("Window", "BACK"))
        self.hands.setText(_translate("Window", "Dealer\'s hand:   (0)\nPlayer\'s hand:   (0)"))
        self.show_winner.setText(_translate("Window", ""))
        self.stand.setText(_translate("Window", "STAND"))
        self.hit.setText(_translate("Window", "HIT"))
        self.again.setText(_translate("Window", "PLAY"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Window = QtWidgets.QMainWindow()
    ui = Screen()
    ui.setupUi(Window)
    Window.show()
    sys.exit(app.exec_())
