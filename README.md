# The Wordle Game
#### Video Demo:  <https://www.youtube.com/watch?v=2w7kET2u4Cs>
#### Description:
This project is pretty much similar to the famous game: wordle but with a few slight changes in how we play the game

*In general the project has two folders: static and templates, one file: app.py*
Now let's dive into all the files of the project
# Static folder
## styles.css
This file contains the CSS code that styles my application's HTML pages

# Templates
## layout.html
This is the layout.html file, which serves as the base template for all other HTML files in the project. It includes links to an external stylesheet and the Bootstrap library. The {% block body %}{% endblock %} is a Jinja2 template tag that indicates where the content of each individual page will be inserted.

## index.html
This is the index.html file which extends the layout.html file.

The body block is defined and contains the HTML content for the main page. It includes a background image and a form for entering player names, along with a button to submit the form.

If there is an announcement message, it is displayed as a centered heading above the form.

## word.html
The main content of this page is a form that allows the user to enter a word for the game. The form is submitted using the HTTP POST method to the "/play" endpoint. The input field for the word is of type "password", which hides the entered characters from view.

If there is a non-empty announcement message, it is displayed in a centered heading with red text.

## play.html
This file creates a page where two players can guess a hidden word with one player providing hints to the other.

The extends keyword in the first line indicates that this HTML file inherits from a base layout template named layout.html. This is a common technique used in web development to avoid repeating common HTML elements in multiple pages.

The block body is used to define a section of the page that will be replaced with content specific to this page. The content of the body block will be inserted into the corresponding block in the base template.

The div with background-image CSS property sets the background image of the page with a wooden texture.

The h1 element with id="invalid_guess" displays a message "Invalid input" in red color at the center of the page.

The div with display: flex property creates a horizontal row containing three elements:

The first h1 element displays the name of the first player and their current score.
The second div element contains a loop that generates guessed_word_length number of hidden letter placeholders for the word to be guessed. The placeholders are hidden by default and their id attribute is set to the index of the letter position. The loop.index0 variable starts the index from zero.
The third h1 element displays the name of the second player and their current score.
The div with class="btn btn-light custom" id="hints" displays the length of the word to be guessed.

The div with class="btn btn-light custom" id="bigger_hints" style="display: none;" is a larger hint that is initially hidden.

The div with id="guesses-box" is a container for displaying the guessed letters. It contains a loop that generates a grid of boxes with the same number of rows and columns as the length of the word to be guessed. The id attribute of each box is set to its position in the grid.

The div with id="guess_box" is a container for the input field and the "Guess" button. It contains two sub-divs:

The first div with id="guess_box_1" contains a label and an input field for the first player's guess.
The second div with id="guess_box_2" is similar to the first one, but is hidden by default and will be displayed when it is the second player's turn to guess.

### app.py
This is a Python Flask app that has three routes: "/", "/word", and "/play".

The "/" route renders an HTML template named "index.html" and passes a variable "announcement" to the template.

The "/word" route renders an HTML template named "word.html" and sets some variables based on form input. It also generates a random value to determine which player goes first.

The "/play" route renders an HTML template named "play.html" and sets some variables based on form input. It also passes in some global variables that are set in the "/word" route.