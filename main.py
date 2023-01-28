from flask import Flask, redirect, render_template, request, session
import os
from functions import translate_to_slovak_from_start, translate_to_slovak_from_end, right_or_wrong
from functions import translate_to_swedish_from_start, translate_to_swedish_from_end
from functions import translate_to_spanish_from_start, translate_to_spanish_from_end


#Tasks
#Using database / sessions to track learning
#Using database to re-ask mistakes
#Show on screen correct answer and user's answer when there is a mistake
#Using CSS make website nicer to look at 
#Using CSS to make website fit on screens
#Add stats on main page
#Add more Slovak words
#In future learning about JS and React etc and seeing how those can be used to benefit this project


app = Flask(__name__)
app.secret_key = os.environ['session_key']


@app.route("/")
def index():
    return render_template("mainpage.html")



@app.route("/slovak_words", methods=["POST"])
def straight_sv():
    form_data = request.form
    user_answer = form_data["user_answer"]
    
    correct_word = form_data["correct_answer"]
    if correct_word == "":
        right_wrong = ""
    else:    
        right_wrong = right_or_wrong(correct_word, user_answer)

    index = form_data["index_number"]

    words = translate_to_slovak_from_start(index)
    
    return render_template("sv_words.html", 
                            word_to_translate = words[0], 
                            correct_answer = words[1],
                            index_follow_up = words[2], 
                            correct_or_wrong = right_wrong )


@app.route("/slovak_words_rev", methods=["POST"])
def reverse_sv():
    form_data = request.form
    user_answer = form_data["user_answer"]
    
    correct_word = form_data["correct_answer"]
    if correct_word == "":
        right_wrong = ""
    else:    
        right_wrong = right_or_wrong(correct_word, user_answer)

    index = form_data["index_number"]

    words = translate_to_slovak_from_end(index)
    
    return render_template("sv_words_reverse.html", 
                            word_to_translate = words[0], 
                            correct_answer = words[1],
                            index_follow_up = words[2], 
                            correct_or_wrong = right_wrong )




@app.route("/swedish_words", methods=["POST"])
def straight_swe():
    form_data = request.form
    user_answer = form_data["user_answer"]
    
    correct_word = form_data["correct_answer"]
    if correct_word == "":
        right_wrong = ""
    else:    
        right_wrong = right_or_wrong(correct_word, user_answer)

    index = form_data["index_number"]

    words = translate_to_swedish_from_start(index)
    
    return render_template("swe_words.html", 
                            word_to_translate = words[0], 
                            correct_answer = words[1],
                            index_follow_up = words[2], 
                            correct_or_wrong = right_wrong )

    
@app.route("/swedish_words_rev", methods=["POST"])
def reverse_swe():
    form_data = request.form
    user_answer = form_data["user_answer"]
    
    correct_word = form_data["correct_answer"]
    if correct_word == "":
        right_wrong = ""
    else:    
        right_wrong = right_or_wrong(correct_word, user_answer)

    index = form_data["index_number"]

    words = spanish_words(index)
    
    return render_template("swe_words_reverse.html", 
                            word_to_translate = words[0], 
                            correct_answer = words[1],
                            index_follow_up = words[2], 
                            correct_or_wrong = right_wrong )




@app.route("/spanish_words", methods=["POST"])
def straight_es():
    form_data = request.form
    user_answer = form_data["user_answer"]
    
    correct_word = form_data["correct_answer"]
    if correct_word == "":
        right_wrong = ""
    else:    
        right_wrong = right_or_wrong(correct_word, user_answer)

    index = form_data["index_number"]

    words = translate_to_spanish_from_start(index)
    
    return render_template("es_words.html", 
                            word_to_translate = words[0], 
                            correct_answer = words[1],
                            index_follow_up = words[2], 
                            correct_or_wrong = right_wrong )

    
@app.route("/spanish_words_rev", methods=["POST"])
def reverse_es():
    form_data = request.form
    user_answer = form_data["user_answer"]
    
    correct_word = form_data["correct_answer"]
    if correct_word == "":
        right_wrong = ""
    else:    
        right_wrong = right_or_wrong(correct_word, user_answer)

    index = form_data["index_number"]

    words = translate_to_spanish_from_end(index)
    
    return render_template("es_words_reverse.html", 
                            word_to_translate = words[0], 
                            correct_answer = words[1],
                            index_follow_up = words[2], 
                            correct_or_wrong = right_wrong )


app.run(host="0.0.0.0", port=81)





