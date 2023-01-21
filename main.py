from flask import Flask, redirect, render_template, session, request, session
import os


app = Flask(__name__)

words_sv = ["pes", "mačka", "dom", "auto"]
words_eng = ["dog", "cat", "house", "car"]
app.secret_key = os.environ['session_key']

def print_word(value=""):
    if value == "":
        index = 0
        session["latest_slovak_word"] = words_sv[index]
        return words_eng[index]
    # elif 


def right_or_wrong(correct_word, user_answer):
    if correct_word == user_answer:
        return "Correct"
    else:
        return "Ahaa! A mistake!"

@app.route("/")
def index():
     return render_template("page.html", word_to_translate = print_word())

                            
@app.route("/words", methods=["POST"])
def word_page():
    word = request.form
    user_answer = word["user_answer"]
    correct_word = session["latest_slovak_word"]
    return render_template("page.html", 
                           word_to_translate = print_word(),
                           correct_or_wrong = right_or_wrong(correct_word, user_answer)
                          )

#need the correct answer ok
#need the users answer ok
#need to compare if correct and return correct/wrong ok
#need to return next word from the list

app.run(host="0.0.0.0", port=81)

"""Extract the common logic of displaying the correct and wrong answers into a separate function. This will make the code more readable and easier to maintain.

Use a while loop instead of a for loop and a recursive function call to keep the program running until the user wants to exit.

The use of the os.system("clear") function is not portable across different operating systems. You can use the subprocess library to call the appropriate command for different operating systems.

Instead of using time.sleep() to pause the program, use the built-in input function with a prompt to pause the program until the user is ready to continue.

It would be good to add some comments in the code to explain the purpose of each function and the process flow of the program.

Use a dictionary data structure to store the English and Slovak words in pairs, it will make it easier to match the answers and keep track of the score.

You can also add some functionalities like keeping a score, displaying the score at the end, and giving the option to repeat the words that were answered incorrectly.

Use a single list for both English and Slovak words and store them in tuple format."""



