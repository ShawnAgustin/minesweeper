from project2 import Minesweeper
game = Minesweeper()
wins = 0
losses = 0
while True:
    game.start()
    if game.checkStatus() == "Win":
        wins += 1
    elif game.checkStatus() == "Lose":
        losses += 1
    again = input("Do you want to play again? ((y)es or (n)o)\n").strip()
    again = again.casefold()
    if again == 'y' or again == 'yes': 
        continue
    else:
        print("\nThank you for playing! \n Final Score:\n")
        print("Wins:", wins, "Losses:", losses)
        break
    
        
