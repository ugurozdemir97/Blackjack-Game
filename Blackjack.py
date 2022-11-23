from PyQt5.QtWidgets import QApplication, QMainWindow, QLabel
from PyQt5.QtMultimedia import QMediaContent, QMediaPlayer
from PyQt5.QtCore import QUrl
from jack import Screen
from random import shuffle, choice
import sys
import os
import source


class App(QMainWindow):
    def __init__(self):
        super(App, self).__init__()

        self.ui = Screen()
        self.ui.setupUi(self)
        self.ui.stackedWidget.setCurrentIndex(0)

        # ----------------------- ALL CARDS ------------------------ #

        self.cards = []
        path = "./Card Images"
        cards = [os.path.join(path, f) for f in os.listdir(path) if f.endswith('.png')]
        for i in cards:
            if os.path.basename(i) != "Hidden.png":
                self.cards.append(os.path.basename(i))
        shuffle(self.cards)

        # Dealer's and Player's cards

        self.player_cards = []
        self.dealer_cards = []

        # Dealer's and Player's total points

        self.total_dealer = 0
        self.total_player = 0

        self.game_end = False  # A variable to keep track of the game status. It will show/hide the hidden card.

        # ----------- FOR GAME MUSIC ---------- #

        path = "./Sounds/card_sound.mp3"
        url = QUrl.fromLocalFile(path)
        self.card_sound = QMediaContent(url)

        self.music = QMediaPlayer()
        self.music.setMedia(self.card_sound)

        # ------------------ NAVIGATION BUTTONS -------------------- #

        self.ui.about.clicked.connect(self.about)
        self.ui.rules.clicked.connect(self.rules)
        self.ui.play.clicked.connect(self.play)
        self.ui.about_back.clicked.connect(self.main)
        self.ui.rules_back.clicked.connect(self.main)
        self.ui.play_back.clicked.connect(self.main)

        # --------------------- TEXT LABEL ---------------------- #

        self.transparent = "background-color: rgba(0, 0, 0, 0);\ncolor: rgb(255, 255, 0);"
        self.dark = "background-color: rgba(0, 0, 0, 180);\ncolor: rgb(255, 255, 0);"

        # -------------------- HIT / STAND / PLAY AGAIN -------------------- #

        self.ui.hit.clicked.connect(self.hit)
        self.ui.stand.clicked.connect(self.end)
        self.ui.again.clicked.connect(self.again)
        self.ui.again.hide()

    # ------------------------- NAVIGATION --------------------------- #

    def main(self):
        self.ui.stackedWidget.setCurrentIndex(0)

        # --------  If any game is played clear all cards -------- #

        self.game_end = False
        self.player_cards.clear()
        self.dealer_cards.clear()

        self.ui.show_winner.setStyleSheet(self.transparent)
        self.ui.show_winner.setText("")

        self.ui.hidden_card.setStyleSheet("image: url(:/HiddenCard/Card Images/Hidden.png);}")

        self.ui.hit.show()
        self.ui.stand.show()
        self.ui.again.hide()

    def rules(self):
        self.ui.stackedWidget.setCurrentIndex(1)

    def about(self):
        self.ui.stackedWidget.setCurrentIndex(2)

    def play(self):
        self.ui.stackedWidget.setCurrentIndex(3)
        self.get_card()

    # ------------------------------------------- SOUND -------------------------------------------------- #

    def sound(self):
        self.music.stop()  # Stopping will give a nice effect when calling multiple times
        self.music.play()

    # -------------------------------------------- GAME -------------------------------------------------- #

    def get_card(self):

        # ---------------- GET THE FIRST CARDS ------------------- #

        if self.ui.checkBox.isChecked():  # If card counting is allowed pop cards so that they won't repeat.
            self.dealer_cards.append(self.cards.pop())
            self.dealer_cards.append(self.cards.pop())
            self.player_cards.append(self.cards.pop())
            self.player_cards.append(self.cards.pop())
        else:
            self.dealer_cards.append(choice(self.cards))
            self.dealer_cards.append(choice([i for i in self.cards if i != self.dealer_cards[0]]))
            self.player_cards.append(choice(self.cards))
            self.player_cards.append(choice([i for i in self.cards if i != self.player_cards[0]]))

        # Gives sound
        self.sound()

        self.calculate_points()

    def calculate_points(self):

        # --------------- CHANGE THE POINTS LABEL -------------------- #

        self.total_player = 0
        self.total_dealer = 0

        # ---------- PLAYER's POINTS ---------- #

        for i in self.player_cards:
            if i[0] == "K" or i[0] == "Q" or i[0] == "J" or i[0] == "T":  # 10 points for special cards
                self.total_player += 10
            elif i[0] != "A":  # If it's not special or Ace, it's as much point as its name
                self.total_player += int(i[0])
            else:
                if self.total_player + 11 > 21:  # If it's Ace, then it is 11 point if less than 21 points.
                    self.total_player += 1
                else:
                    self.total_player += 11

        # ---------- DEALER's POINTS ---------- #

        for i in self.dealer_cards:

            if not self.game_end and i == self.dealer_cards[0]:
                continue  # Don't take the hidden card into calculation if game is not done yet

            if i[0] == "K" or i[0] == "Q" or i[0] == "J" or i[0] == "T":  # 10 points for special cards
                self.total_dealer += 10
            elif i[0] != "A":  # If it's not special or Ace, it's as much point as its name
                self.total_dealer += int(i[0])
            else:
                if self.total_dealer + 11 > 21:  # If it's Ace, then it is 11 point if less than 21 points.
                    self.total_dealer += 1
                else:
                    self.total_dealer += 11

        self.ui.hands.setText(f"Dealer\'s hand:   ({self.total_dealer})\nPlayer\'s hand:   ({self.total_player})")

        self.clear()  # Clear the current cards
        self.game()  # Add all cards

    def game(self):

        # ----------------- ADD ALL CARDS DYNAMICALLY ------------------ #

        for i in range(1, len(self.dealer_cards)):
            dealer_card = QLabel(self.ui.horizontalLayoutWidget_2)
            dealer_card.setStyleSheet(f"image: url(:/Cards/Card Images/{self.dealer_cards[i]});")
            self.ui.dealer_deck.addWidget(dealer_card)

        for i in range(len(self.player_cards)):
            player_card = QLabel(self.ui.horizontalLayoutWidget)
            player_card.setStyleSheet(f"image: url(:/Cards/Card Images/{self.player_cards[i]});")
            self.ui.player_deck.addWidget(player_card)

        if self.game_end:  # If game ends show the hidden card
            self.ui.hidden_card.setStyleSheet(f"image: url(:/Cards/Card Images/{self.dealer_cards[0]});")

    def hit(self):

        self.sound()  # Give a sound effect

        # ------------------------ ADD ONE CARD ------------------------- #

        if self.ui.checkBox.isChecked():
            self.player_cards.append(self.cards.pop())
        else:
            self.player_cards.append(choice(self.cards))

        player_card = QLabel(self.ui.horizontalLayoutWidget)
        player_card.setStyleSheet(f"image: url(:/Cards/Card Images/{self.player_cards[-1]});")
        self.ui.player_deck.addWidget(player_card)

        self.calculate_points()
        if self.total_player > 21 or self.total_player == 21:
            self.end()

    def dealer_hit(self):  # Dealer takes a card if he has less than 16 at the end of the game.

        self.sound()  # Give sound

        if self.ui.checkBox.isChecked():
            self.dealer_cards.append(self.cards.pop())
        else:
            self.dealer_cards.append(choice(self.cards))

        dealer_card = QLabel(self.ui.horizontalLayoutWidget)
        dealer_card.setStyleSheet(f"image: url(:/Cards/Card Images/{self.dealer_cards[-1]});")
        self.ui.dealer_deck.addWidget(dealer_card)

        self.calculate_points()

        if self.total_dealer < 16:
            self.dealer_hit()

    def end(self):

        self.ui.show_winner.setStyleSheet(self.dark)
        self.ui.hit.hide()
        self.ui.stand.hide()
        self.game_end = True
        self.ui.again.show()
        self.calculate_points()

        # --------------- GAME RULES ----------------- #

        if self.total_dealer < 16:
            self.dealer_hit()
        if self.total_player > 21:
            self.ui.show_winner.setText("PLAYER\nBUSTED!")
        elif self.total_player == 21:
            self.ui.show_winner.setText("BLACKJACK!")
        elif self.total_player == self.total_dealer:
            self.ui.show_winner.setText("DRAW!")
        elif self.total_dealer > 21:
            self.ui.show_winner.setText("DEALER\nBUSTED!")
        elif self.total_dealer == 21:
            self.ui.show_winner.setText("DEALER\nHIT\nBLACKJACK!")
        elif self.total_dealer > self.total_player:
            self.ui.show_winner.setText("DEALER\nWON!")
        else:
            self.ui.show_winner.setText("PLAYER\nWON!")

    def clear(self):

        # ---------- Clear all card images if there is any -------- #

        for i in reversed(range(1, self.ui.dealer_deck.count())):
            self.ui.dealer_deck.itemAt(i).widget().deleteLater()

        for i in reversed(range(self.ui.player_deck.count())):
            self.ui.player_deck.itemAt(i).widget().deleteLater()

    def again(self):
        self.ui.again.hide()
        self.main()
        self.play()


def application():
    win = QApplication(sys.argv)
    window = App()
    window.show()
    sys.exit(win.exec_())


application()
