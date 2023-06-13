print('Begin Quiz')
questions = ['is 2+2 = 4?', 'is 1+1=3', 'is 4+6 = 10']

answers = ['yes','no','yes']



def quizGame():
    score = 0 
    for i in range(len(questions)):
        print(questions[i])
        ans = input('Please answer \n')
        if ans == answers[i]:
            print('Correct')
            score +=1 
        else:
            print('incorrect')

    print(f'Final Score: {score}')

quizGame()           
print('Well done quiz complete')