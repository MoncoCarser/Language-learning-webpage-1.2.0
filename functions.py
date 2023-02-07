
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

#Mistake should include correct translation
#mistakes need to be saved so those can be returned to





swe_words = ["vecka", "år", "idag", "imorgon", "igår",
             "kalender", "sekund", "timme", "minut", "klockan",
             "klocka", "en timme", "kan", "använda", "göra",
             "gå", "komma", "skratta", "göra", "se",
             "långt", "liten", "bra", "vacker", "ful",
             "svår", "lätt", "dålig", "nära", "Trevligt att träffas",
             "hej", "god morgon", "goddag"," god kväll",
             "godnatt", "Hur mår du?", "tack", "nej", "utsökt",
             "jag är", "hej då", "ja", "måndag", "tisdag",
             "onsdag", "torsdag", "fredag", "lördag", "söndag",
             "maj", "januari", "februari", "mars", "april",
             "juni", "juli", "augusti", "september", "oktober",
             "november", "december", "noll", "ett / en", "två",
             "tre", "fyre", "fem", "sex", "sju",
             "åtta", "nio", "tio", "coffee", "öl",
             "té", "vin", "vatten", "biff", "fläsk",
             "kyckling", "lamm", "fisk", "fot", "ben",
             "huvud", "arm", "hand", "finger", "kropp",
             "mage", "rygg", "bröst", "sjuksköterska", "anställd",
             "poliskonstapel", "kock", "ingenjör", "doktor", "föreståndare",
             "lärare", "programmerare", "försäljare", "snälla"
            ]

eng_swe_words = ["week", "year", "today", "tomorrow", "yesterday",
                 "calendar", "second", "hour", "minute", "o'clock",
                 "clock", "one hour", "can", "use",
                 "do", "go", "come", "laugh", "make",
                 "see", "far", "small", "good", "beautiful",
                 "ugly", "difficult", "easy", "bad", "near",
                 "Nice to meet you", "hello", "good morning","good afternoon",
                 "good evening", "good night", "How are you?", "thank you", "no",
                 "delicious", "I'm..", "goodbye", "yes", "Monday",
                 "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday",
                 "Sunday", "May", "January", "February", "March",
                 "April", "June", "July", "August", "September",
                 "October", "November", "December", "zero", "one",
                 "two", "three", "four", "five", "six",
                 "seven", "eight","nine", "ten", "coffee",
                 "beer", "tea", "wine", "water", "beef",
                 "pork", "chicken", "lamb", "fish", "foot",
                 "leg", "head", "arm", "hand", "finger",
                 "body", "stomach", "back", "chest", "nurse",
                 "employee", "police officer", "cook", "engineer",
                 "doctor", "manager", "teacher", "programmer", "salesman", "please"
                ]

def translate_to_swedish_from_start(index=""):

    #Right now code does not react accordingly to reaching maximum index
    
    if index == "":
        index = 0
        #need to add a WIN option when all words are cleared
        eng_word = eng_swe_words[index]
        swe_word = swe_words[index]
        return(eng_word, swe_word, index)
    else: 
        index = int(index)
        index += 1
        eng_word = eng_swe_words[index]
        swe_word = swe_words[index]
        return(eng_word, swe_word, index)



def translate_to_swedish_from_end(index=""):
    if index == "":
        index = len(words_sv) -1
        eng_word = eng_swe_words[index]
        swe_word = swe_words[index]
        return(eng_word, swe_word, index)
    else: 
        index = int(index)
        index -= 1
        eng_word = eng_swe_words[index]
        swe_word = swe_words[index]
        return(eng_word, swe_word, index)





spanish_words = ["hola", "testi lauseke", "buenas", "buenos dias", "buenas tardes", "buenas noches",
                 "chao", "adios", "hasta luego", "hasta pronto", "hasta mañana", "nos vemos",
                 "Que tengas un buen día", "por favor", "gracias", "muchas gracias", "de nada", 
                 "con permiso", "disculpe / perdón", "me llamo", "Mi nombre es..",
                 "Cúal es tu nombre?", "Cómo te llamas?", "mucho gusto", "igualmente",
                 "quien?", "qué?", "dónde?", "cuando?", "por qué?", "cómo?", "cuánto cuesta?",
                 "a qué hora?", "Cómo estás?", "Qué tal?", "Como te va?", "Como te vas?",
                 "Qué pasa", "Estoy bien", "Estoy mal", "De dónde eres?", "Soy de..",
                 "Lost Estados Unidos", "China", "Japón", "Alemania", "Francia",
                 "Inglaterra", "Polonia", "uno", "dos", "tres", "quatro", "cinco",
                 "seis", "siete", "ocho", "nueve", "diez", "viente", "treinta",
                 "cuarenta", "cincuenta", "sesenta", "setenta", "ochenta", "noventa",
                 "cien", "la tienda", "Dónde está la tienda?", "Me gusta..", "Esta camisa",
                 "Estos pantalones", "Este suéter", "Este abrigo", "Esta billetera",
                 "Este bolso", "Estos zapatos", "Puedo probarmelo?", "Tienes esto en otro tamaño",
                 "restaurante", "desayuno", "almuerzo", "comida", "cena",
                 "My gustaria pedir", "Me gustaria comer", "le pidor por",
                 "por favor me da", "cerveza", "vino tinto", "vino blanco", "agua",
                 "jugo", "zumo", "té", "café", "sopa", "carne", "pescado", "pan",
                 "queso", "helado", "chocolate", "Dónde está este restaurante?",
                 "Puedes traerme la cuenta, por favor?", "Me trae la cuenta, por favor?",
                 "tren", "avión", "bilete", "boleto", "Adónde va este autobús?",
                 "el hotel", "el hostel", "la playa", "el supermercado",
                 "el centro commercial", "sigue recto", "gira a la derecha",
                 "gira a la izquierda", "A qué distancia está..", "Puedes ayudarme, por favor?",
                 "Estoy perdido", "Necesito ayuda", "Me siento enfermo",
                 "Dondé está el hospital?", "Necesito llamar a la policia",
                 "Necesito llamar a la ambulancia",
                ]


spanish_eng_words = ["hello", "hi", "good morning", "good afternoon", "good night",
                     "goodbye", "goodbye", "see you later", "see you soon", "see you tomorrow", "see you",
                     "Have a great day", "please", "thank you", "thank you very much", "you're welcome", "excuse me", 
                     "sorry", "My name is..", "My name is..", "What is your name?", "What is your name?",
                     "Nice to meet you", "likewise", "who?", "what?", "where?", "when?",
                     "why?", "how?", "how much?", "at what time?", "How are you?", "How are you?",
                     "How's it going?", "How are you doing?", "What's up?", "I'm good",
                     "I'm bad", "Where are you from?", "I'm from..", "The US", "China",
                     "Japan", "Germany", "France", "England", "Poland", "1", "2", "3",
                     "4", "5", "6", "7", "8", "9", "10", "20", "30", "40", "50", "60",
                     "70", "80", "90", "100", "the store", "Where is the store?",
                     "I like..", "This shirt", "These pants", "That sweater", "That coat",
                     "That wallet", "That purse", "These shoes", "Can I try it on?",
                     "Do you have this in another size?", "restaurant", "breakfast",
                     "lunch", "lunch", "dinner", "I would like to order",
                     "I would like to eat", "I ask you for", "please give me",
                     "beer", "red wine", "white wine", "water", "juice", "juice", "tea",
                     "coffee", "soup", "meat", "fish", "bread", "cheese", "ice cream",
                     "chocolate", "Where is this restaurant?", "Can you bring me the bill, please?",
                     "Can you bring me the bill, please?", "train", "airplane", "ticket",
                     "ticket", "Where does this bus go?", "the hotel", "the hostel",
                     "the beach", "the supermarket", "the shopping mall", "continue straight",
                     "turn right", "turn left", "How far is..", "Can you help me, please?",
                     "I'm lost", "I need help", "I feel sick", "Where is the hospital?",
                     "I need to call the police", "I need to call the ambulance",
                    ]


def translate_to_spanish_from_start(index=""):

    #Right now code does not react accordingly to reaching maximum index
    
    if index == "":
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
        return(eng_word, es_word, index)



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
