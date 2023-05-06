import random

while True:
    player_options = {1: 'Red', 2: 'Blue', 3: 'Green', 4: 'Yellow'}
    computer_choice = random.choice(list(player_options.values()))

    
    print('choose a color... \n\t1-> Red \n\t2-> Blue \n\t3-> Green \n\t4-> Yellow')
    option = input('choose a number ')

    player_choice = player_options[int(option)]

    print(f'player\'s option{player_choice} computer_option: {computer_choice}')

    if computer_choice == player_choice:
        print('You Won!')

    res = input("play again? y/n")
    if res.lower() == 'n':
        print("GAME OVER!!!")
        break