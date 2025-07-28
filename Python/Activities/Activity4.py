while(True):
    player1 = input("Player1, enter choice (rock/paper/scissors): ").lower()
    player2 = input("Player2, enter choice (rock/paper/scissors): ").lower()

    if (player1 != "rock" and player1 != "paper" and player1 != "scissors") or (player2 != "rock" and player2 != "paper" and player2 != "scissors"):
        print("Invalid input")
    else:
        if player1 == player2:
            print("Tie")
        elif (player1 == "rock" and player2 == "scissors") or (player1 == "scissors" and player2 == "paper") or (player1 == "paper" and player2 == "rock"):
            print("Player 1 wins!")
        else:
            print("Player 2 wins!")
    again = input("Do you want to play again(yes/no): ").lower()
    if(again=="yes"):
        continue
    else:
        break
