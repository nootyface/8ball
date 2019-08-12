import random
import time
import sys


def response(i):
    response = ["Yes, most definitely!", "The chances are high!", "Not likely!", "May the odds be ever in your favor.",
                "You got no shot, kid.", "Try it out and see!", "23% of working", "99.9% success rate",
                "Congratulations, yes!", "Ask a probably question," "Ask again later", "Better not tell you now",
                "Cannot predict now", "Concentrate and ask again", "Don't count on it"]
    return response[i]

while True:
    userInput = input('Type \'ask\' to ask a question or \'quit\' to quit ')
    if userInput == 'quit':
        sys.exit()
    elif userInput == 'ask':
        input('What is your question? ')
        print('Thinking', end='')
        for i in range(4):
            time.sleep(1)
            if i == 3:
                print('.')
                break
            print('.', end='')
        print(response(random.randint(0, 14)))
        time.sleep(2)
        continue
    else:
        continue
    
