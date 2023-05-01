# from ten_thousand.game_logic import GameLogic
from game_logic import GameLogic

calculater = GameLogic.calculate_score

dice_roller = GameLogic.roll_dice

validate = GameLogic.validate_keepers

def play (roller = GameLogic.roll_dice):

    """
    this function starts the game when called
    """
    '''
    to get the numbers that inside .txt to use it in the test cases
    '''
    global dice_roller
    dice_roller = roller

    print("Welcome to Ten Thousand")
    print("(y)es to play or (n)o to decline")

    input_user = input('> ')
    if input_user == "n":
        end_game()
    if input_user  == 'y':
        start_round(round = 1 ,total=0, dice = 6 , point=0)

def end_game ():
        """
        this function return a answer once the user wrote n in the beganing of runing this code
        """
        
        return print('OK. Maybe another time') 



def start_round(round = 1 , total = 0 ,point = 0 , dice = 6):
    '''
    this function will start the game once the plyer enterd y 
    '''
    first_roll = dice_roller(dice) 


    random_num = ''
    for i in first_roll:
         random_num += str(i)+" "

    print(f'Starting round {round}')
    print(f'Rolling {dice} dice...')
    print(f'*** {random_num}***')
    

    if calculater(first_roll) == 0:
              print("****************************************")
              print("**        Zilch!!! Round over         **")
              print("****************************************")
              print(f"You banked 0 points in round {round}")
              print(f"Total score is {total} points")
              round +=1
              print(total)
            #   print(f'Starting round {round}')
            #   point = 0
              return start_round(round,total,dice=6)
    print('Enter dice to keep, or (q)uit:')

    
    user_choices = input ('> ')
    if user_choices =='q':
        quit_game(total)

    

    else :
         dice_to_keep = tuple(int(x) for x in user_choices) 

        #  print (first_roll,dice_to_keep)
        #  print (validate(first_roll,dice_to_keep))
          
         if  validate(first_roll,dice_to_keep) == False:
                   while validate(first_roll,dice_to_keep) == False:
                          print ("Cheater!!! Or possibly made a typo...")
                          print(f'*** {random_num}***')
                          print('Enter dice to keep, or (q)uit:')

                          user_choices1 = input ('> ')
             

                          if user_choices1 =='q':
                               quit_game(total)
           
                          dice_to_keep = tuple(int(x) for x in user_choices1) 
     

         
         new_dice = dice - len(dice_to_keep) # we get the dice that we enterd in the function (6) and subtract it from the length of inputs that the plyer enterd (user_choices)


         point += calculater(dice_to_keep) # point was 0 so we should add the points regarding the input that the users entered (using calculate score function)

         total += point

         print(f'You have {point} unbanked points and {new_dice} dice remaining')
         print('(r)oll again, (b)ank your points or (q)uit:')
         user_choices = input ('> ')

         if user_choices =='q':
             quit_game(total)

         if user_choices =='b':
              banked_choice(round , total ,point)
         if user_choices == 'r':
             if new_dice > 0 :
                # point += point
                start_round(round , total ,point,new_dice)
             else :
                  round +=1
                  print('you dont have any more dices play again')
                  start_round(round,total,point,dice=6)   
           

def banked_choice(round , total ,point):
     '''
     will banked the total score 
     '''
     print(f'You banked {point} points in round {round}')
     total += point
     print(f'Total score is {total} points')
     round +=1
     start_round(round,total)
      

def quit_game(total):
     '''
     this will quit the game if the plyer enterd q 
     '''
     print(f'Thanks for playing. You earned {total} points')



# def cheat(values, dice_to_keep,random_num,total):
#      while validate(values,dice_to_keep) == False:
#         print ("Cheater!!! Or possibly made a typo...")
#         print(f'*** {random_num}***')
#         print('Enter dice to keep, or (q)uit:')

#         user_choices1 = input ('> ')
             

#         if user_choices1 =='q':
#              quit_game(total)
        
#         dice_to_keep1 = tuple(int(x) for x in user_choices1) 
#         new_dice_to_keep = dice_to_keep1
#      return new_dice_to_keep
     

     





if __name__ == "__main__":
    play()