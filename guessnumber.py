import random


def guess_num():
    secret_number = random.randint(1,10)
    
    print("Welcome to the guess number game !")
    print("I have selected a number betweem 1 and 10 can you guess it")
    attempts = 0
    max_attempts = 3
    
    while attempts < max_attempts:
        
        user_guess = int(input('Enter your number here! '))
        attempts +=1
        
        if user_guess == secret_number:
            print('You guessed Correctly')
            break
        
        elif user_guess > secret_number:
            print('Too high! try again...')
            
        else:
            print('Too low ! try again')  
         
    
    if attempts == max_attempts and user_guess != secret_number:
     print(f'sorry you have reached the maximum number of attempts  the correct number was{secret_number}')
    
guess_num()