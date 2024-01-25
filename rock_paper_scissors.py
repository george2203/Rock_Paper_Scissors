import random

player_move = input("Choose Rock (r), Paper (p), or Scissors (s): ")
rock = 'Rock'
paper = 'Paper'
scissors = 'Scissors'

if player_move == 'r':
    player_move = 'Rock'
elif player_move == 'p':
    player_move = 'Paper'
elif player_move == 's':
    player_move = 'Scissors'
else:
    raise SystemExit("Invalid Input. Try again...")

computer_move = random.choice([rock,paper,scissors])
print(f"Computer chose: {computer_move}")

if player_move == computer_move:
    print("*** T H E  R E S U L T  I S  A  T I E ***")
elif player_move == 'Rock' and computer_move == 'Scissors':
    print('*** P L A Y E R : W I N S ! ***')
elif player_move == 'Scissors' and computer_move == 'Rock':
    print('*** C O M P U T E R : W I N S ! ***')

elif player_move == 'Scissors' and computer_move == 'Paper':
    print('*** P L A Y E R : W I N S ! ***')
elif player_move == 'Paper' and computer_move == 'Scissors':
    print('*** C O M P U T E R : W I N S ! ***')

elif player_move == 'Paper' and computer_move == 'Rock':
    print('*** P L A Y E R : W I N S ! ***')
elif player_move == 'Rock' and computer_move == 'Paper':
    print('*** C O M P U T E R : W I N S ! ***')
