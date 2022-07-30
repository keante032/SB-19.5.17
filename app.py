from boggle import Boggle
from flask import Flask, request, render_template, session

boggle_game = Boggle()
game_board = boggle_game.make_board()

@app.route('/')
def homepage():
    """Show the game board."""

    return render_template('homepage.html', board=game_board)