import random
def game_reasult(user,computer):
    if user == computer:
       return("its a draw")
    if((user == 'snake' and computer == 'water')or
       (user == 'gun' and computer== 'snake')or
       (user == 'water' and computer=='gun')):
        return 'user win'
    else:
        return "computer wins"
print("Welcome to snake water gun  game")

choices = ['snake','water','gun']
def score_board(user_score,computer_score,ties):
    print(f"user score is : {user_score}")
    print(f"computer score is ; {computer_score}")
    print(f"total ties is : {ties}")

user_score = 0
computer_score =0
ties=0
while True:
    user_choice= input("Choose one : snake \ water \ gun::").lower()
    if user_choice not in choices:
        print("invalid choice :pleasr choose one ")
        continue
    computer_choice = random.choice(choices)
    print(f"computer choose:{computer_choice}")
    winner = game_reasult(user_choice,computer_choice)

     
    if winner == "user win":
        print("You win this round")
        user_score = user_score+1
    elif winner == "computer wins":
        print("You lose this round")
        computer_score=computer_score+1
    else:
        print("Its a draw")
        ties = ties+1
    print(f"   \SCOREBOARD\n   Your score:{user_score} \n   Computer score:{computer_score} \n   Total ties:{ties}")
    again = input("play again ??(y/n)").lower()  
    if again!="y":
        print("Thanks for playing")
        break