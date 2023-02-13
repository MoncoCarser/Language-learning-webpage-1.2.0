#we need to create a bare bones python version to test all functionality more easily and to build from that onwards

#list of words

spanish_list = (
            ("hola", "hello"), ("buenas", "hi"), ("buenos dias", "good morning"), ("Dondé está el hospital?", "Where is the hospital?"), ("Necesito llamar a la policia", "I need to call the police"), ("Necesito llamar a la ambulancia", "I need to call the ambulance")
              )


#print(spanish_list[1][0])

#function to get a word from the list
def spanish_eng_translation(start=True, index=""):
        if start:
            if index == "":
                index = 0
            else: 
                index = int(index)
                index += 1
        else:
            if index == "":
                index = len(spanish_list) -1
            else: 
                index = int(index)
                index -= 1
                
        eng_word = spanish_list[index][1]
        es_word = spanish_list[index][0]
        return eng_word, es_word, index

    
"""    if index == "":
        index = 0
        #need to add a WIN option when all words are cleared
        eng_word = spanish_eng_words[index]
        es_word = spanish_words[index]
        return(eng_word, es_word, index)
    else: 
        index = int(index)
        index += 1
        eng_word = spanish_eng_words[index]
        es_word = spanish_words[index]
        return(eng_word, es_word, index)"""



def translate_to_spanish_from_end(index=""):
    if index == "":
        index = len(spanish_words) -1
        eng_word = spanish_eng_words[index]
        es_word = spanish_words[index]
        return(eng_word, es_word, index)
    else: 
        index = int(index)
        index -= 1
        eng_word = spanish_eng_words[index]
        es_word = spanish_words[index]
        return(eng_word, es_word, index)


#function to check if answer is right
        
def check_answer(correct_word, user_answer):
    if correct_word == user_answer:
        return ("Correct")
    else:
        return ("Ahaa! A mistake to learn from!")

#user is asked a word
index = ""
answer_and_index = spanish_eng_translation(True, '')
answer = input(f"Translate: {answer_and_index[0]}\n")
print(answer)

for index in range(len())

"""index = 0
while True:
    if answer == answer_and_index[1]:
        print("Es correcto")
        while True:
            answer_and_index = spanish_eng_translation(True, index)
            answer = input(f"Translate: {answer_and_index[0]}\n")
            if answer == answer_and_index[1]:
                print("Es correcto")
                index += 1

    else: 
        print("Eeeeee")"""
        
        

#user gives answer


#next word is given




