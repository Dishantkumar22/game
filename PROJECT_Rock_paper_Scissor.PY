import random
print("|=======================|")
print("| SCISSOR, PAPER & Rock |")
print("|=======================|")
cpu_Choice = ["S", "P", "R"]  # CPu picks randomly any choice from the list.
user_score = 0  # user score ,this will be updated each round
cpu_score = 0  # cpu score ,this will be updated each round
i = 1
chance = int(input("Enter number of Rounds: "))  # taks input from the user
while i <= chance:  # while loop running for number of rounds
    cpu = str(random.choice(cpu_Choice))  # cpu choice is randomly choosen
    # user choice
    user = input("Enter Scissor, Paper or Rock (key to press: S,P,R): ").upper()
    print(f"Round no:[{i}]")
    print("Computer Enter: ", cpu)
    if user == cpu:
        print("<Tie Round>")
    elif user == "R":
        # print("Computer Enter: ", cpu)
        if cpu == "P":
            print("> You lose! Paper covers Rock")
            cpu_score += 1
        else:
            print("> You win! Rock smashes Scissor")
            user_score += 1
    elif user == "P":
        if cpu == "S":
            print("> You lose! Scissor cuts Paper")
            cpu_score += 1
        else:
            print("> You win! Paper covers Rock")
            user_score += 1
    elif user == "S":
        if cpu == "R":
            print("> You lose! Rock smashes Scissors")
            cpu_score += 1
        else:
            print("> You win! Scissor cuts Paper")
            user_score += 1
    else:
        print("Enter valid choice. Play again, All the best.")
        exit()

    print("\n\t******ScoreBoard******")
    print(f"\t You: {user_score} | Computer: {cpu_score}")
    print("\t**********************")
    print("________________________________________________________")
    i += 1
print("\n||||||||||||| GAME OVER ||||||||||||||")
print("______________________________________")
if user_score == cpu_score:
    print("Game is Tie. Play Again")
elif user_score < cpu_score:
    print("Sorry You lost the game\nCPU won the game with score:", cpu_score)
else:
    print("You Won the Game with score:", user_score)

print("\n\t======Final Scorecard======")
print(f" \t    You: {user_score} | Computer: {cpu_score}")
print("\t===========================")
