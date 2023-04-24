# random qoute generator
# project status = Basic.version 0.0.1 
# advanced version of this code is coming

#import the random and sys module
import random
import sys
# create the qoutes list

qoutes = ['Be the change that you wish to see in the world.',
     'In three words I can sum up everything I\'ve learned about life: it goes on.',
     'The only way to do great work is to love what you do.',
     'Believe you can and you\'re halfway there.',
     'The future belongs to those who believe in the beauty of their dreams.',
     'Don\'t judge each day by the harvest you reap but by the seeds that you plant.',
     'The best way to predict your future is to create it.',
     'It does not matter how slowly you go as long as you do not stop.',
     'You miss 100% of the shots you don\'t take.',
     'Life is 10% what happens to you and 90% how you react to it.',
     'The greatest glory in living lies not in never falling, but in rising every time we fall.',
     'The only person you are destined to become is the person you decide to be.',
     'Success is not final, failure is not fatal: It is the courage to continue that counts.',
     'You can\'t blame gravity for falling in love.',
     'It always seems impossible until it\'s done.',
     'I have not failed. I\'ve just found 10,000 ways that won\'t work.',
     'If you don\'t stand for something you will fall for anything.',
     'It is during our darkest moments that we must focus to see the light.',
     'The greatest glory in living lies not in never falling, but in rising every time we fall.',
     'Happiness is not something ready made. It comes from your own actions.',
     'Your time is limited, don\'t waste it living someone else\'s life.',
     'If you want to live a happy life, tie it to a goal, not to people or things.',
     'The way to get started is to quit talking and begin doing.',
     'If you really look closely, most overnight successes took a long time.',
     'I can\'t change the direction of the wind, but I can adjust my sails to always reach my destination.',
     'Keep your face always toward the sunshine - and shadows will fall behind you.',
     'The only thing we have to fear is fear itself.',
     'Life is like riding a bicycle. To keep your balance, you must keep moving.',
     'Not everything that is faced can be changed, but nothing can be changed until it is faced.',
     'The best and most beautiful things in the world cannot be seen or even touched - they must be felt with the heart.',
     'The two most important days in your life are the day you are born and the day you find out why.',
     'It\'s not whether you get knocked down, it\'s whether you get up.',
     'Whatever you do, do it well.',
     'Success is stumbling from failure to failure with no loss of enthusiasm.',
     'To be yourself in a world that is constantly trying to make you something else is the greatest accomplishment.',
     'Believe in yourself and all that you are. Know that there is something inside you that is greater than any obstacle.',
     'Our lives begin to end the day we become silent about things that matter.',
     'The greatest wealth is to live content with little.',
     'Spread love everywhere you go. Let no one ever come to you without leaving happier.',
     'You can never cross the ocean until you have the courage to lose sight of the shore.',
     'I would rather die of passion than of boredom.',
     'Success is not how high you.']
# create a var that asks the user if he want a random qoute
print_qoute = input('do you want a random qoute ? ')
# create a while true loop 
while True:
# create a var that has the value of a random choice of the qoutes list in the while true loop to create different qoute every time 
    random_qoute = random.choice(qoutes)
# create in if statment to check if the user wants random qoute
    if print_qoute.lower() == 'yes':
        print(random_qoute)
# change the print_qoute var so that asks the user if he wants another qoute.
        print_qoute = input('want another qoute ? ')
# create a elif statment to check if the new user answer to the new value of the var print_qoute is equal to 'yes'
# and don't forget to use ths .lower() func to convert whatever the user typed into small charcters
    elif print_qoute.lower() == 'yes':
            print(random_qoute)
            break
# create a sys.exit()  func to close the program instead of only the current loop       
    else:
        print('ok bye')
        break
        sys.exit()
             
