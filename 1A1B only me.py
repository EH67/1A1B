import random
num = random.sample('0123456789', 4)

while num[0] == '0': #this loop ensures the first number isn't 0
    num = random.sample('0123456789', 4)

outfile = open('1A1B_data', 'a')

answer = ''.join(num)
guess = int(input('enter four digits: '))
guesslist = [*(str(guess))]
j = 1
A = 0
B = 0
outfile.write('the correct answer is {}\n'.format(''.join(num)))
outfile.write('guess {}: {}'.format(j, guess))
while int(answer) != int(guess):
    hello = set(guesslist)
    while len(hello) != 4: #this tiny while loop checks if user enters duplicates
        guess = int(input('invalid. enter four digits: '))
        guesslist = [*(str(guess))]
        hello = set(guesslist)
    for i in range(4):
        if guesslist[i] == answer[i]:
            A += 1
        elif guesslist[i] in answer:
            B += 1
        else:
            pass
    outfile.write('\t{}A{}B\n'.format(A,B))
    print('You guessed {}. {}A{}B'.format(guess, A, B))
    if int(answer) == int(guess):
        break
    guess = int(input('enter four digits: '))
    guesslist = [*str(guess)]
    j += 1
    outfile.write('guess {}: {}'.format(j, guess))
    A = 0
    B = 0

print('Congrats! You guessed the right number! This took you {} tries!'.format(j))

outfile.write('\n\ttook a total of {} tries\n\n\n'.format(j))
outfile.close()