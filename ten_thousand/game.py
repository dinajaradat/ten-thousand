# from game_logic import GameLogic
from ten_thousand.game_logic import GameLogic


def play(roller = GameLogic.roll_dice ,round_number=3):  #roller: A function that rolls dice and returns a list of values, round_number (int): The number of rounds to play.
    # global dice_roller
    # dice_roller = roller
    score = 0
    dic_round = 0
    Total_score = 0 
    
    print("Welcome to Ten Thousand")
    input1 = input("(y)es to play or (n)o to decline\n> ")
    if input1 == "n":
        print ("OK. Maybe another time")
        return 
    elif input1 != "y":
        return ("Invalid input. Please try again.")

    while round_number > 0:
     #    print(f"Your current score is {str(score)} points.")
        dic_round +=1
        round_number -=1
        print(f"Starting round {str(dic_round)}")

     #    dices = GameLogic.roll_dice(6)
        #print (dices)
     #    dice_str = " ".join(str(num) for num in dice_roller(6))
        #print (dice_str)
        print(f"Rolling 6 dice...")
        formatted_roll = format_roller(roller(6))
        print (formatted_roll)
        
   
        print("Enter dice to keep, or (q)uit:") # selecting a subset to keep for points OR quit

        input2 = input("> ")
        rem_input2 = input2.replace("> ", "").strip()    # replace() to remove the string "> " from the beginning , strip() method to remove any leading or trailing whitespace characters
        if rem_input2 == "q":
               print(f"Thanks for playing. You earned {str(score)} points")  # bank the current points and end the round.
               return
        else:
            dice_remaining = 6 - (len(input2))
            #print (dice)
            if len(input2) == 1:
                    banked = GameLogic.calculate_score((int(input2),))
            else :
                    dice_list = [int(d) for d in input2]
                    #print(dice_list)
                    dice_tuple = tuple(dice_list)
                    #print(dice_tuple)
                    banked = GameLogic.calculate_score(dice_tuple)
                   
              
            print ("You have "+ str(banked) +" unbanked points and "+ str(dice_remaining) +" dice remaining")
            Total_score += banked



        print("(r)oll again, (b)ank your points or (q)uit:")
        input3 = input("> ")
        rem_input3 = input3.replace("> ", "").strip()
        if rem_input3 == "q":
               print(f"Thanks for playing. You earned {str(score)} points")
               return
            
        elif rem_input3 == "b":
             print("You banked "+ str(banked) +" points in round "+str(dic_round))
             print("Total score is "+ str(Total_score) +" points")   # total score is the sum of scores from each round.
             score += banked
            
            
        
def format_roller(dice_roller): # function takes a list of integers representing a roll of dice as input and returns a formatted string that displays the values of the dice
    as_string = [str(value) for value in dice_roller]
    format_roll = " ".join(as_string)
    return f"*** {format_roll} ***"   

if __name__ =="__main__":
    print(play())         
#     pass  


              
              
              




