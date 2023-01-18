import os, time

print('\033[?25l', end="") # deletes cursor

# words are from https://www.pinhok.com/kb/slovak/272/100-basic-slovak-vocabularies/


slovak_words_list = ["ja", "ty", "on", "ona", "ono", "my", "vy", "oni / ony",
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

reverse_slovak_words_list = slovak_words_list[::-1]
number_of_slovak_words = len(slovak_words_list)


english_words_list = ["I", "you", "he", "she", "it", "we", "you", "they",
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

reverse_english_words_list = english_words_list[::-1]
number_of_english_words = len(english_words_list)

def colour_change(colour):
    if colour=="red":
        return ("\033[31m")
    elif colour=="blue":
        return ("\033[34m")
    elif colour=="yellow":
        return ("\033[33m")
    elif colour == "green":
        return ("\033[32m")
    elif colour == "purple":
        return ("\033[35m")
    elif colour=="none":
        return ("\033[0m")

#Subroutines are starting from the beginning of the list, asking item by item, comparing answers with other language list. If wrong, then using reverse list to restart questioning. If wrong, subroutine retarts from first list.


def asking_for_slovak_words():
    for i in range(len(english_words_list)):
        answer_to_question_SK = input(f"What is slovak for {colour_change('blue')}{english_words_list[i]}{colour_change('none')}:\n ")
        if answer_to_question_SK == slovak_words_list[i]:
            print("Correct")
            time.sleep(0.5)
            os.system("clear")
            continue
        else:
            print(f"Wrong. Right answer is {colour_change('yellow')}{slovak_words_list[i]}{colour_change('none')}")
            time.sleep(1)
            os.system("clear")
            asking_reverse_slovak_words()
            

def asking_reverse_slovak_words():
    for i in range(len(reverse_english_words_list)):
        reverse_answer_to_question_SK = input(f"What is Slovak for {colour_change('blue')}{reverse_english_words_list[i]}{colour_change('none')}:\n ")
        if reverse_answer_to_question_SK == reverse_slovak_words_list[i]:
            print("Correct")
            time.sleep(0.5)
            os.system("clear")
            continue
        else:
            print(f"Wrong. Right answer is {colour_change('yellow')}{reverse_slovak_words_list[i]}{colour_change('none')}")
            print()
            time.sleep(1)
            os.system("clear")
            asking_for_slovak_words()



def asking_for_english_words():
    for i in range(len(slovak_words_list)):
        print()
        answer_to_question_ENG = input(f"What is English for {colour_change('blue')}{slovak_words_list[i]}{colour_change('none')}:\n\n          ")
        if answer_to_question_ENG == english_words_list[i]:
            print()
            print("Correct")
            time.sleep(0.5)
            os.system("clear")
            continue
        else:
            print()
            print(f"Wrong. Right answer is {colour_change('yellow')}{english_words_list[i]}{colour_change('none')}")
            time.sleep(1)
            os.system("clear")
            asking_reverse_english_words()
            time.sleep(2)
            os.system("clear")

        
def asking_reverse_english_words():
    for i in range(len(reverse_slovak_words_list)):
        reverse_answer_to_question_ENG = input(f"\nWhat is English for {colour_change('blue')}{reverse_slovak_words_list[i]}{colour_change('none')}:\n\n          ")
        if reverse_answer_to_question_ENG == reverse_english_words_list[i]:
            print("Correct")
            time.sleep(0.5)
            os.system("clear")
            continue
        else:
            print()
            print(f"Wrong. Right answer is {colour_change('yellow')}{reverse_english_words_list[i]}{colour_change('none')}")
            print()
            time.sleep(2)
            os.system("clear")
            time.sleep(1)
            os.system("clear")
            asking_for_english_words()


# tarkista tästä ideaa myös https://www.youtube.com/watch?v=bIjJVKmAz98&t=606s

# 2 lewrning progress is stores in ?

#if and else to ask a word, if right do this, else do this
# 3 loop of saying word in slovak / eng and asking for translation, informing if right / wrong and saving in data if right / wrong. Showing right answer if wrong was given / saying it was right

# select_language = input("Choose Slovak (1) or English (2): ")


print("""  Welcome back great learner.
    This programs is meant for learning
    English and Slovak words by repetition, 
    until you show mastery.""")
print()
print()
print(f"Currently our total lists contain {number_of_slovak_words} Slovak words and {number_of_english_words} English words.") #This acts as a quality check: do numbers match?
print()

#tarvitaanko while true looppia? 
user_choice = input("Do you want to translate \nSlovak words to English (press 1), \n\nor English words to Slovak (press 2). \n\n\t >>> ")
print()
print("Words shown and used are written without special letters. Only ä / ö / å are used.")
print()
print("This is due to program creator's mother tongue using these letters, so they are already familiar to him")


if user_choice == "1":
    asking_for_english_words()
elif user_choice == "2":
    asking_for_slovak_words()
#else: