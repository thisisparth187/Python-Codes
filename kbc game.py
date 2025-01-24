# Create a program capable of displaying questions to the user like KBC Use list data type to store the questions and their correct answers.Display the correct amount the user is taking home after playing the game.
import random

questions = [
    'Who is known as the "Father of the Nation" in India?\na) Jawaharlal Nehru\nb) Mahatma Gandhi\nc) Subhas Chandra Bose\nd) Sardar Vallabhbhai Patel', 
    'What is the capital of France?\nOptions: \na) Rome \nb) Berlin \nc) Paris \nd) Madrid', 
    'Which planet is known as the "Red Planet"? \nOptions: \na) Earth \nb) Mars \nc) Jupiter \nd) Venus', 
    'What is the chemical symbol for water? \nOptions: \na) O2 \nb) H2O \nc) CO2 \nd) NaCl', 
    'Who wrote the epic "Mahabharata"? \nOptions: \na) Valmiki \nb) Ved Vyasa \nc) Kalidasa \nd) Tulsidas'
    ]

answers = ['b', 'c', 'b', 'b', 'b']


i = 1

ch = int(input('Welcome to the game of KBC!!\nHere for each correct answer you will win 100$\nThere will be 5 questions!!Best of LUCK!!!!\nPress 1 to begin Press 0 to surrender:'))

if ch == 1:
    win_money = 0
    correct_ans = 0
    while questions:
        question = random.choice(questions)
        print(f'\n{i})',question)
        choice = input('Enter your choice: ')
        que_index = questions.index(question)
        if choice == answers[que_index]:
            correct_ans += 1
            print('Correct')
        else:
            print('GALAT JAWAB')
            break
        questions.remove(question)
        i = i + 1

    print(f'You got total {correct_ans} correct answer so you have earned total {correct_ans*100}$')

else:
    print('Lol noob kid!!')