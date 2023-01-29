#Создайте программу для игры в ""Крестики-нолики"".

import emoji

fields = [1,2,3,
         4,5,6,
         7,8,9]

victories = [[0,1,2],
              [3,4,5],
              [6,7,8],
              [0,3,6],
              [1,4,7],
              [2,5,8],
              [0,4,8],
              [2,4,6]]

def print_fields():
     print(fields[0], end = " ")
     print(fields[1], end = " ")
     print(fields[2])

     print(fields[3], end = " ")
     print(fields[4], end = " ")
     print(fields[5])

     print(fields[6], end = " ")
     print(fields[7], end = " ")
     print(fields[8])    

def step_fields(step,symbol):
     ind = fields.index(step)
     fields[ind] = symbol

def get_result():
     win = ""

     for i in victories:
         if fields[i[0]] == "X" and fields[i[1]] == "X" and fields[i[2]] == "X":
             win = "Игрок 1"
         if fields[i[0]] == "O" and fields[i[1]] == "O" and fields[i[2]] == "O":
             win = "Игрок 2"   

     return win

game_over = False
player1 = True

while game_over == False:

     print_fields()

     if player1 == True:
         symbol = "X"
         print(emoji.emojize(':backhand_index_pointing_down:'))
         step = int(input("Игрок 1, ваш ход: "))
     else:
         symbol = "O"
         print(emoji.emojize(':backhand_index_pointing_down_light_skin_tone:'))
         step = int(input("Игрок 2, ваш ход: "))

     step_fields(step,symbol) 
     win = get_result() 
     if win != "":
         game_over = True
     else:
         game_over = False

     player1 = not(player1)        
      
print_fields()
print("Победил", win)
print(emoji.emojize('Поздравляем! :1st_place_medal:'))