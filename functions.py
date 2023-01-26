#testing and building for future improvements

score = 0

words_sv = ["ja", "ty", "on", "ona", "ono", "my", "vy", "oni / ony",
                     "co", "kto", "kde", "preco", "ako", "ktory", "kedy",
                     "potom", "ak", "naozaj", "ale", "pretoze", "nie",
                     "toto", "to", "vsetko", "alebo", "a", "vediet",
                     "mysliet", "prist", "polozit", "vziat", "najst",
                     "pocuvat", "pracovat", "rozpravat", "dat", "mat rad",
                     "pomoct", "milovat", "volat", "cakat", "nula", "jeden",
                     "dva", "tri", "styri", "pät", "sest", "sedem", "osem",
                     "devät", "desat", "jedenast", "dvanast", "trinast",
                     "strnast", "pätnast", "sestnast", "sedemnast", "osemnast",
                     "devätnast", "dvadsat", "novy", "stary", "malo", "vela",
                     "nespravny", "spravny", "zly", "dobry", "stastny", "kratky",
                     "dlhy", "maly", "velky", "tam", "tu", "vpravo", "vlavo",
                     "krasny", "mlady", "stary", "ahoj", "ok", "samozrejme",
                     "cau", "dovidenia", "ospravedlnte ma", "prepac", "dakujem",
                     "prosim", "teraz", "hodina", "minuta", "sekunda", "den",
                     "tyzden", "mesiac", "rok", "vecer", 
                      ]


words_eng = ["I", "you", "he", "she", "it", "we", "you", "they",
                      "what", "who","where", "why", "how", "which", "when",
                      "then", "if", "really", "but", "because", "not", "this",
                      "that", "all", "or", "and", "to know", "to think",
                      "to come", "to put", "to take", "to find", "to listen",
                      "to work", "to talk", "to give", "to like", "to help",
                      "to love", "to call", "to wait", "0", "1", "2", "3", "4",
                      "5", "6", "7", "8", "9", "10", "11", "12", "13", "14",
                      "15", "16", "17", "18", "19", "20", "new", "old", "few",
                      "many", "wrong", "correct", "bad", "good", "happy",
                      "short", "long", "small", "big", "there", "here",
                      "right", "left", "beautiful", "young", "old", "hello",
                      "ok", "of course", "bye", "good bye", "excuse me",
                      "sorry", "thank you", "please", "now", "hour", "minute", 
                      "second", "day", "week", "month", "year", "evening",
                      ]



def translate_to_slovak_from_start(index=""):

    #Right now code does not react accordingly to reaching maximum index
    if index == "":
        index = 0
        #need to add a WIN option when all words are cleared
        eng_word = words_eng[index]
        sv_word = words_sv[index]
        return(eng_word, sv_word, index)
    else: 
        index = int(index)
        index += 1
        eng_word = words_eng[index]
        sv_word = words_sv[index]
        return(eng_word, sv_word, index)



def translate_to_slovak_from_end(index=""):
    if index == "":
        index = len(words_sv) -1
        eng_word = words_eng[index]
        sv_word = words_sv[index]
        return(eng_word, sv_word, index)
    else: 
        index = int(index)
        index -= 1
        eng_word = words_eng[index]
        sv_word = words_sv[index]
        return(eng_word, sv_word, index)



def right_or_wrong(correct_word, user_answer):
    if correct_word == user_answer:
        return ("Correct")
    else:
        return ("Ahaa! A mistake to learn from!")

#mistakes need to be saved so those can be returned to



"""

def asking_for_slovak_words():
    for i in range(len(english_words_list)):
        answer_to_question_SK = english_words_list[i]
        if answer_to_question_SK == slovak_words_list[i]:
            print("Correct")
            continue
        else:
            print(f"Wrong {slovak_words_list[i]}")
            asking_reverse_slovak_words()


def ask_question(question, correct_answer):
    answer = input(question)
    if answer.lower() == correct_answer.lower():
        print("Correct")
        return True
    else:
        print(f"Wrong. Right answer is {correct_answer}")
        return False

def shuffle_questions():
    #random.shuffle(words)
    for index, (english, slovak) in enumerate(words):
        correct = ask_question(f"What is Slovak for {english}: ", slovak)
        if correct:
            score += 1
            
            """