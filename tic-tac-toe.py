1
import random

board = [
    [1,2,3],
    [4,5,6],
    [7,8,9]
]

turn = 0 #0 is for computer, 1 is for human


board_positions = {
    1 : (0,0),
    2 : (0,1),
    3 : (0,2),
    4 : (1,0),
    5 : (1,1),
    6 : (1,2),
    7 : (2,0),
    8 : (2,1),
    9 : (2,2)
}

#If the first selection is for the computer 
first_time = True

#Show the board
def display_board(board):
  row = 0
  for i in range (0,3):
    drawLine()
    print()
    drawColumns(board[i])
  drawLine()

  print()

'''
Draw a line like this: 
+-------+-------+-------+
'''
def drawLine():
  for i in range(0,4):
    print("+",end = "")
    if i != 3:
      for j in range(0,7):
        print("-",end="")

'''
Draw a column like this: 

|       |       |       |
|   1   |   2   |   3   |
|       |       |       |

'''
def drawColumns(row):
  for i in range(0,3):
    if i != 1:
      print('|       |       |       |')
    else:
      print(f'|   {row[0]}   |   {row[1]}   |   {row[2]}   |')

#Function for the person
def enter_move(Board):
  free_fields = make_list_of_free_fields(Board)
  while True:
    try:
      choice = int(input("\nEnter your movement: "))
      if choice > 0 and choice<10:
        if board_positions[choice] in free_fields:
          board[board_positions[choice][0]][board_positions[choice][1]] = 'O'
          display_board(board)
          return
        else:
          print("\nNo valid position, choose another.")
      else:
        print("\nYour number must be between 1 and 10")
    except:
      print("\nInvalid entry")


#Function to determine the free_fields on the board
def make_list_of_free_fields(board):
  free_fields = []
  for i in range(0,3):
    for j in range(0,3):
      if board[i][j] != 'X' and board[i][j] != 'O':
        free_fields.append((i,j))
  return free_fields

#Function for the computer
def draw_move(board):
  if first_time:
    board[1][1] = 'X'
    display_board(board)
    return

  while True:
    free_fields = make_list_of_free_fields(board)
    position = random.randint(1, 9)
    if board_positions[position] in free_fields:
          board[board_positions[position][0]][board_positions[position][1]] = 'X'
          display_board(board)
          return

#Function that determines if a player will won (or draw) or continue
def victory_for(board):
  # 0 represents win player
  # 1 represents win computer
  # 2 represents draw
  # 3 represents continue
  free_fields = make_list_of_free_fields(board)
  values_list = []

  #Verify victory in rows
  for i in range(0,3):
    for j in range(0,3):
      values_list.append(board[i][j])

    are_equal = all(element == values_list[0] for element in values_list)
    if are_equal:
      return 1 if values_list[0] == 'X' else 0
    else:
      values_list.clear()

  #Verify victory in columns
  for i in range(0,3):
    for j in range(0,3):
      values_list.append(board[j][i])

    are_equal = all(element == values_list[0] for element in values_list)
    if are_equal:
      return 1 if values_list[0] == 'X' else 0
    else:
      values_list.clear()

  #Verify victory in diagonal 1
  for i in range(0,3):
      values_list.append(board[i][i])
  are_equal = all(element == values_list[0] for element in values_list)
  if are_equal:
      return 1 if values_list[0] == 'X' else 0
  else:
      values_list.clear()


  #Verify victory in diagonal 2
  j = 2
  for i in range(0,3):
      values_list.append(board[i][j])
      j -= 1
  are_equal = all(element == values_list[0] for element in values_list)
  if are_equal:
      return 1 if values_list[0] == 'X' else 0
  else:
      values_list.clear()


  if free_fields == []:
    return 2

  return 3

#Start game code 


turn = random.randint(0,1)
display_board(board)
while True:
  victory = victory_for(board)
  if victory != 3: #If we have a winner
    break
  if turn == 0:
    draw_move(board)
    if first_time:
      first_time = False
    turn = 1
  else:
    enter_move(board)
    if first_time:
      first_time = False
    turn = 0

if victory == 0:
  print("\nVictory is for you!")
elif victory == 1:
  print("\nYou lose!")
else:
  print("\nIt's a draw!")