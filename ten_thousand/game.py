

from ten_thousand.game_logic import GameLogic
# from game_logic import GameLogic



calculater = GameLogic.calculate_score

dice_roller = GameLogic.roll_dice
cheat= GameLogic.validate_keepers
scores = GameLogic.get_scorers
rounds = 0
flage=False


"""
This module implements a game called Ten Thousand. The game consists of several rounds, and in each round, a player rolls six dice. The objective of the game is to accumulate as many points as possible across the rounds.

The game is started by calling the `play` function. If the player chooses to play, the function enters a loop that starts each round. In each round, the player is prompted to select some dice to keep and roll the remaining dice. The player can then choose to keep rolling or bank their accumulated points for the round. If the player scores no points on a roll, they lose their accumulated points for the round.

The module contains the following functions:
"""


def play (roller = GameLogic.roll_dice,num_rounds=2):

    """
    this function starts the game when called
    """
    '''
    to get the numbers that inside .txt to use it in the test cases
    '''
    global flage
    global rounds 
    rounds = num_rounds
    global dice_roller
    dice_roller = roller

    print("Welcome to Ten Thousand")
    print("(y)es to play or (n)o to decline")

    input_user = input('> ')
    if input_user == "n":
        end_game()
    if input_user  == 'y':
           
           print(f'Starting round 1')
           start_round(round = 1 ,total=0, dice = 6 , point=0)
        
def end_game ():
        """
        this function return a answer once the user wrote n in the beganing of runing this code
        """
        
        return print('OK. Maybe another time') 



def start_round(round = 1 , total = 0 ,point = 0 , dice = 6):
    global flage
    '''
    this function will start the game once the plyer enterd y 
    '''
    first_roll = dice_roller(dice) 
    random_num = ''
    for i in first_roll:
         random_num += str(i)+" "

   
    print(f'Rolling {dice} dice...')
    print(f'*** {random_num}***')

    if calculater(first_roll) == 0:
              print("****************************************")
              print("**        Zilch!!! Round over         **")
              print("****************************************")
              print(f"You banked 0 points in round {round}")
              print(f"Total score is {total} points")
              round +=1
              print(f'Starting round {round}')
              point = 0
              return start_round(round,total,dice=6)
    print('Enter dice to keep, or (q)uit:')
    user_choices = input ('> ').replace(" ","")

    if user_choices =='q':
        quit_game(total)

    else :
         
         dice_to_keep = tuple(int(x) for x in user_choices) 
         cheat_test =cheat(first_roll,dice_to_keep)
         while cheat_test ==False:
              print("Cheater!!! Or possibly made a typo...")
              print(f'*** {random_num}***')
              print('Enter dice to keep, or (q)uit:')
              user_choices = input ('> ').replace(" ","")
              if user_choices =='q':
                return quit_game(total)
              else:
                   dice_to_keep = tuple(int(x) for x in user_choices)
                   cheat_test =cheat(first_roll,dice_to_keep)
         hot_dice =scores(dice_to_keep)
              

                 

         new_dice = dice - len(dice_to_keep) 
         point += calculater(dice_to_keep) 

         if len(hot_dice) == 6:
              return hot_dice2(round,total,point,new_dice)
         


         print(f'You have {point} unbanked points and {new_dice} dice remaining')
         print('(r)oll again, (b)ank your points or (q)uit:')
         user_choices = input ('> ')

         if user_choices =='q':
          #   flage=True
          #   x=banked_choice(round , total ,point)


          #   quit_game(x)
             return quit_game(total)

         if user_choices =='b':
            #   print (total)
              banked_choice(round , total ,point)
         if user_choices == 'r':
             if new_dice > 0 :
                start_round(round , total ,point,new_dice)
             else :
                #   round +=1
                  print('you dont have any more dices play again')
                  start_round(round,total,point,dice=6)   
           

def banked_choice(round , total ,point):
     '''
     will banked the total score 
     '''
    #  print (total)
     total += point
     if flage:
          return total
     print(f'You banked {point} points in round {round}')
     print(f'Total score is {total} points')
    
     
     if  rounds == 1:
           quit_game(total)
           return 
     
     round +=1
     print(f'Starting round {round}')
     start_round(round,total)
      

def quit_game(total):
     '''
     this will quit the game if the plyer enterd q 
     '''
     print(f'Thanks for playing. You earned {total} points')
  


def hot_dice2(round,total,point,new_dice):
     print(f'You have {point} unbanked points and 6 dice remaining')
     print('(r)oll again, (b)ank your points or (q)uit:')
     user_choices = input ('> ')

     if user_choices =='q':
        quit_game(total)

     if user_choices =='b':
            
            banked_choice(round , total ,point)
     if user_choices == 'r':
        if new_dice > 0 :
            start_round(round , total ,point,new_dice)
        else :
            start_round(round,total,point,dice=6)





if __name__ == "__main__":
    play()


# # from ten_thousand.game_logic import GameLogic
# from game_logic import GameLogic

# calculater = GameLogic.calculate_score

# dice_roller = GameLogic.roll_dice

# validate = GameLogic.validate_keepers

# def play (roller = GameLogic.roll_dice):

#     """
#     this function starts the game when called
#     """
#     '''
#     to get the numbers that inside .txt to use it in the test cases
#     '''
#     global dice_roller
#     dice_roller = roller

#     print("Welcome to Ten Thousand")
#     print("(y)es to play or (n)o to decline")

#     input_user = input('> ')
#     if input_user == "n":
#         end_game()
#     if input_user  == 'y':
#         start_round(round = 1 ,total=0, dice = 6 , point=0)

# def end_game ():
#         """
#         this function return a answer once the user wrote n in the beganing of runing this code
#         """
        
#         return print('OK. Maybe another time') 



# def start_round(round = 1 , total = 0 ,point = 0 , dice = 6):
#     '''
#     this function will start the game once the plyer enterd y 
#     '''
#     first_roll = dice_roller(dice) 


#     random_num = ''
#     for i in first_roll:
#          random_num += str(i)+" "

#     print(f'Starting round {round}')
#     print(f'Rolling {dice} dice...')
#     print(f'*** {random_num}***')
    

#     if calculater(first_roll) == 0:
#               print("****************************************")
#               print("**        Zilch!!! Round over         **")
#               print("****************************************")
#               print(f"You banked 0 points in round {round}")
#               print(f"Total score is {total} points")
#               round +=1
#               print(total)
#             #   print(f'Starting round {round}')
#             #   point = 0
#               return start_round(round,total,dice=6)
#     print('Enter dice to keep, or (q)uit:')

    
#     user_choices = input ('> ')
#     if user_choices =='q':
#         quit_game(total)

    

#     else :
#          dice_to_keep = tuple(int(x) for x in user_choices) 

#         #  print (first_roll,dice_to_keep)
#         #  print (validate(first_roll,dice_to_keep))
          
#          if  validate(first_roll,dice_to_keep) == False:
#                    while validate(first_roll,dice_to_keep) == False:
#                           print ("Cheater!!! Or possibly made a typo...")
#                           print(f'*** {random_num}***')
#                           print('Enter dice to keep, or (q)uit:')

#                           user_choices1 = input ('> ')
             

#                           if user_choices1 =='q':
#                                quit_game(total)
           
#                           dice_to_keep = tuple(int(x) for x in user_choices1) 
     

         
#          new_dice = dice - len(dice_to_keep) # we get the dice that we enterd in the function (6) and subtract it from the length of inputs that the plyer enterd (user_choices)


#          point += calculater(dice_to_keep) # point was 0 so we should add the points regarding the input that the users entered (using calculate score function)

#          total += point

#          print(f'You have {point} unbanked points and {new_dice} dice remaining')
#          print('(r)oll again, (b)ank your points or (q)uit:')
#          user_choices = input ('> ')

#          if user_choices =='q':
#              quit_game(total)

#          if user_choices =='b':
#               banked_choice(round , total ,point)
#          if user_choices == 'r':
#              if new_dice > 0 :
#                 # point += point
#                 start_round(round , total ,point,new_dice)
#              else :
#                   round +=1
#                   print('you dont have any more dices play again')
#                   start_round(round,total,point,dice=6)   
           

# def banked_choice(round , total ,point):
#      '''
#      will banked the total score 
#      '''
#      print(f'You banked {point} points in round {round}')
#      total += point
#      print(f'Total score is {total} points')
#      round +=1
#      start_round(round,total)
      

# def quit_game(total):
#      '''
#      this will quit the game if the plyer enterd q 
#      '''
#      print(f'Thanks for playing. You earned {total} points')



# # def cheat(values, dice_to_keep,random_num,total):
# #      while validate(values,dice_to_keep) == False:
# #         print ("Cheater!!! Or possibly made a typo...")
# #         print(f'*** {random_num}***')
# #         print('Enter dice to keep, or (q)uit:')

# #         user_choices1 = input ('> ')
             

# #         if user_choices1 =='q':
# #              quit_game(total)
        
# #         dice_to_keep1 = tuple(int(x) for x in user_choices1) 
# #         new_dice_to_keep = dice_to_keep1
# #      return new_dice_to_keep
     

     





# if __name__ == "__main__":
#     play()