#testing and building for future improvements

words = [("dog", "pes"), ("cat", "mačka"), ("house", "dom"), ("car", "auto")]
score = 0

def ask_question(question, correct_answer):
    answer = input(question)
    if answer.lower() == correct_answer.lower():
        print("Correct")
        return True
    else:
        print(f"Wrong. Right answer is {correct_answer}")
        return False

def main():
    #random.shuffle(words)
    for index, (english, slovak) in enumerate(words):
        correct = ask_question(f"What is Slovak for {english}: ", slovak)
        if correct:
            score += 1