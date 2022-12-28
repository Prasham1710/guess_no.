print('Welcome to  Quiz')
answer=input('Are you ready to play the Quiz ? (yes/no) :')
score=0
total_questions = 3
 
if answer.lower()=='yes':
    answer=input('Question 1: What is capital of india ?')
    if answer.lower()=='New Delhi':
        score += 1
        print('correct')
    else:
        print('Wrong Answer')
 
 
    answer=input('Question 2: what is full form of css? ')
    if answer.lower()=='Cascading style Sheets':
        score += 1
        print('correct')
    else:
        print('Wrong Answer')
 
    answer=input('Question 3: What is the React ?')
    if answer.lower()=='Framework':
        score += 1
        print('correct')
    else:
        print('Wrong Answer')
 
print('Thank you for playing quiz, you attempted',score,"questions correctly!")
mark=(score/total_questions)*100
print('Marks obtained:',mark)
