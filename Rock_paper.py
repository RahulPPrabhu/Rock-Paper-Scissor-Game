from random import randint

print("One to score 5 points first will win ✨")
System_Score = 0
User_Score = 0

while True:
    user_int = input("Enter Rock, Paper or Scissor: ")
    print("------------------------------")
    user_input = user_int.capitalize()

    l1 = ["Rock", "Paper", "Scissor"]
    num = randint(0, 2)

    if user_input not in l1:
        print("Sorry!! Please Enter either Rock, Paper or Scissor")
        print("------------------------------")
        continue

    print("System Input: ", l1[num])
    print("User Input: ", user_input)

    if user_input == l1[num]:
        print("Opps!!! It's draw 💪")
    elif l1[num] == "Rock":
        if user_input == "Paper":
            print("You Caught Me 💀")
            User_Score += 1
        elif user_input == "Scissor":
            print("Smashed You 😂")
            System_Score += 1
    elif l1[num] == "Paper":
        if user_input == "Rock":
            print("Caught You 😎")
            System_Score += 1
        elif user_input == "Scissor":
            print("You cut me into pieces 😢")
            User_Score += 1
    elif l1[num] == "Scissor":
        if user_input == "Rock":
            print("Ouch!! You smashed me 😒")
            User_Score += 1
        elif user_input == "Paper":
            print("haha!!! Ripped into pieces 😈")
            System_Score += 1

    print("------------------------------")
    print("Your Score: ", User_Score)
    print("System Score: ", System_Score)
    print("------------------------------")

    if User_Score == 2:
        print("Congratulation!!! You Won 🥳")
        break
    elif System_Score == 2:
        print("Sorry Mate!!! You lost😂💪")
        break

