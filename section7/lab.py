from IPython.display import clear_output
def display_board():
  
  clear_output()

  print('  |   |')
  print('__|___|__')
  print('  |   |')

  marker = ''
  while not (marker == 'O' or marker == 'X'):
    marker = input('Player 1: Do you want to be X or O?').upper()

  if (marker == 'X'):
    print('X')
  else:
    print('O')

display_board()
