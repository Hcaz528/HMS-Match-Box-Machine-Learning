import random

print("THIS IS MATCH BOX ML DEMO")

# First Round
box1 = ["Rock"]*10 + ["Paper"]*10 + ["Scissors"]*10

# Second Round given First move
box2 = [box1] + [box1] + [box1]

# Third Round give First and Second move
box3 = [box2] + [box2] + [box2]

boxes = [box1] + [box2] + [box3]

# Function to check which input won
def checkIfWon(x,y):
    if (x.lower() == "rock" and y.lower() == "paper"):
        return False
    elif (x.lower() == "rock" and y.lower() == "scissors"):
        return True
    elif (x.lower() == "paper" and y.lower() == "scissors"):
        return False
    elif (x.lower() == "paper" and y.lower() == "rock"):
        return True
    elif (x.lower() == "scissors" and y.lower() == "rock"):
        return False
    elif (x.lower() == "scissors" and y.lower() == "paper"):
        return True

# Function to convert from index to label
# Rock index = 0, Paper index = 1, Scissors index = 2
def convert2label(x):
    if (x == 0):
          out = "rock"
    elif (x == 1):
          out = "paper"
    else:
          out = "scissors"
    return out

# Number of games played
EPOCHS = 10

for epoch in range(EPOCHS):
    # Current Round
    rounds = 0
    # Current Number of User Wins
    p_wins = 0
    # Current Number of Computer Wins
    r_wins = 0

    # Save spots for answers
    p_answer = ""
    r_answer = ""
    r1_answer = ""
    r2_answer = ""
    r3_answer = ""

    while(p_wins < 2 and r_wins < 2):
        rounds = rounds + 1
        p_answer = ""
        r_answer = ""
    
        # Plays Round 1, Round 2, and Round 3
        if (rounds == 1):
            while (p_answer.lower() == r_answer.lower()):
                print("\n\nRound 1\n")
                p_answer = input("Rock, Paper, or Scissors: ")
                r_answer = boxes[0].pop(random.randrange(0,len(boxes[0])))
                print("\n||| " + r_answer + " |||")

            if (checkIfWon(p_answer,r_answer)):
                print("\n-> You Won!")
                p_wins = p_wins + 1
            else:
                print("\n-> You Lost!")
                r_wins = r_wins + 1

            if (r_answer.lower() == "rock"):
                r1_answer = 0
            elif (r_answer.lower() == "paper"):
                r1_answer = 1
            elif (r_answer.lower() == "scissors"):
                r1_answer = 2
            
        elif (rounds == 2):
            while (p_answer.lower() == r_answer.lower()):
                print("\n\nRound 2\n")
                p_answer = input("Rock, Paper, or Scissors: ")
                r_answer = boxes[1][int(r1_answer)].pop(random.randrange(0,len(boxes[1][int(r1_answer)])))
                print("\n||| " + r_answer + " |||")

            if (checkIfWon(p_answer,r_answer)):
                print("\n-> You Won!")
                p_wins = p_wins + 1
            else:
                print("\n-> You Lost!")
                r_wins = r_wins + 1

            if (r_answer.lower() == "rock"):
                r2_answer = 0
            elif (r_answer.lower() == "paper"):
                r2_answer = 1
            elif (r_answer.lower() == "scissors"):
                r2_answer = 2
            
        elif (rounds == 3):
            while (p_answer.lower() == r_answer.lower()):
                print("\n\nRound 3\n")
                p_answer = input("Rock, Paper, or Scissors: ")
                r_answer = boxes[2][int(r1_answer)][int(r2_answer)].pop(random.randrange(0,len(boxes[2][int(r1_answer)][int(r2_answer)])))
                print("\n||| " + r_answer + " |||")

            if (checkIfWon(p_answer,r_answer)):
                print("\n-> You Won!")
                p_wins = p_wins + 1
            else:
                print("\n-> You Lost!")
                r_wins = r_wins + 1

            if (r_answer.lower() == "rock"):
                r3_answer = 0
            elif (r_answer.lower() == "paper"):
                r3_answer = 1
            elif (r_answer.lower() == "scissors"):
                r3_answer = 2
            
    if(p_wins > r_wins):
        print("Trial " + str(epoch))
        print("\n\nYou Won Game!")
        print(str(p_wins) + "-" + str(r_wins))
    else:
        print("Trial " + str(epoch))
        print("\n\nComputer Won Game!")
        print(str(p_wins) + "-" + str(r_wins))
        # Adds winning answers to box
        for i in range(5):
            boxes[0].append(convert2label(r1_answer))
        for i in range(5):
            boxes[1][int(r1_answer)].append(convert2label(r2_answer))
        for i in range(5):
            boxes[2][int(r1_answer)][int(r2_answer)].append(convert2label(r3_answer))

