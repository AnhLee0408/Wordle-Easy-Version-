import random
from flask import Flask, render_template, request, redirect
from cs50 import SQL
import re
## THE WORDLE EASY VERSION
app = Flask(__name__)

guessed_word = ""
guessed_word_length = 0
player_1 = ""
score_1 = 0

score_2 = 0
player_2 = ""

announcement = ""
announcement_2 = ""

go_first = None
@app.route("/")
def index():
    global announcement
    return render_template("index.html", announcement=announcement)

@app.route("/word", methods=["POST", "GET"])
def add_word():
    global announcement, player_1, player_2, announcement_2, go_first
    if request.method == "POST":
        player1_name = request.form.get("player1")
        player2_name = request.form.get("player2")
        if (not player1_name or not player2_name) or (not player1_name and not player2_name):
            announcement = "Name fields mustn't be left empty"
            return redirect("/")

        player1_name = player1_name.strip().title()
        player2_name = player2_name.strip().title()
        if player1_name == player2_name:
            announcement = "Names shouldn't be the same"
            return redirect("/")

        player_1 = player1_name
        player_2 = player2_name

        go_first = random.choice([player_1, player_2])



    return render_template("word.html", announcement_2=announcement_2)

@app.route("/play", methods=["POST", "GET"])
def play():
    global announcement_2, guessed_word, score_1, score_2, player_1, player_2, guessed_word_length, random_first, go_first
    if request.method == "POST":
        word = request.form.get("word")
        if not word:
            announcement_2 = "The field cannot be empty"
            return redirect("/word")
        if not re.match(r"^[a-zA-Z]+$", word.strip(), flags=0):
            announcement_2 = "Invalid input"
            return redirect("/word")

        guessed_word = word.lower()
        guessed_word_length = len(guessed_word)

    return render_template("play.html", guessed_word=guessed_word, score_1=score_1, score_2=score_2, player_1=player_1, player_2=player_2, guessed_word_length=guessed_word_length, go_first=go_first)