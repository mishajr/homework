# Завдання 1 


# def delitel(a,b):

#     if b == 0:
#         return a
#     else:
#         return delitel(b,a % b)
    
# num = 42
# num1 = 56

# print(delitel(num,num1))

# =====================================================================================================


# Завдання 2





# def compare_numbers(secret_num, guess, attempt=1):
#     bulls = 0
#     cows = 0

#     if len(secret_num) != len(guess):
#         print("Будь ласка, введіть чотиризначне число.")
#         return compare_numbers(secret_num, input("Спроба №" + str(attempt) + ": "), attempt)

#     for i in range(len(secret_num)):
#         if secret_num[i] == guess[i]:
#             bulls += 1
#         elif secret_num[i] in guess:
#             cows += 1

#     if bulls == len(secret_num):
#         print(f"Вітаю! Ви вгадали число {secret_num} за {attempt} спроб.")
#     else:
#         print(f"Бики: {bulls}, Корови: {cows}")
#         return compare_numbers(secret_num, input("Спроба №" + str(attempt + 1) + ": "), attempt + 1)

# def play_game():
#     secret_number = '2345'
#     print("Вгадайте чотиризначне число. Після кожної спроби вам буде сказано кількість биків і корів.")
#     user_guess = input("Спроба №1: ")
#     compare_numbers(secret_number, user_guess)

# play_game()



# ===========================================================================================================================


# Завдання 3

# def is_valid_move(board, x, y):

#     if x >= 0 and y >= 0 and x < len(board) and y < len(board) and board[x][y] == -1:
#         return True
#     return False

# def print_board(board):

#     for row in board:
#         print(" ".join(map(str, row)))
#     print("\n")

# def knight_tour(n):

#     board = [[-1 for _ in range(n)] for _ in range(n)]  # Створення дошки n x n
#     move_x = [2, 1, -1, -2, -2, -1, 1, 2]
#     move_y = [1, 2, 2, 1, -1, -2, -2, -1]
#     board[0][0] = 0  # Початкова позиція коня
#     pos = 1

#     if not knight_tour_util(n, board, 0, 0, move_x, move_y, pos):
#         print("Розв'язок не знайдено.")
#     else:
#         print_board(board)

# def knight_tour_util(n, board, curr_x, curr_y, move_x, move_y, pos):

#     if pos == n**2:
#         return True

#     for i in range(8):
#         new_x = curr_x + move_x[i]
#         new_y = curr_y + move_y[i]
#         if is_valid_move(board, new_x, new_y):
#             board[new_x][new_y] = pos
#             if knight_tour_util(n, board, new_x, new_y, move_x, move_y, pos + 1):
#                 return True
#             board[new_x][new_y] = -1  

#     return False


# board_size = 8
# knight_tour(board_size)

# ====================================================================================================

#  завдання 4
 
# import random

# def print_board(board):

#     for row in board:
#         print(" ".join(map(str, row)))
#     print("\n")

# def find_blank(board):

#     for i in range(len(board)):
#         for j in range(len(board[i])):
#             if board[i][j] == 0:
#                 return i, j
#     return -1, -1

# def is_valid_move(board, row, col):

#     blank_row, blank_col = find_blank(board)
#     return (row == blank_row and abs(col - blank_col) == 1) or (col == blank_col and abs(row - blank_row) == 1)

# def shuffle_board(board, moves=100):

#     for _ in range(moves):
#         blank_row, blank_col = find_blank(board)
#         possible_moves = []
#         if blank_row > 0:
#             possible_moves.append((blank_row - 1, blank_col))
#         if blank_row < len(board) - 1:
#             possible_moves.append((blank_row + 1, blank_col))
#         if blank_col > 0:
#             possible_moves.append((blank_row, blank_col - 1))
#         if blank_col < len(board[0]) - 1:
#             possible_moves.append((blank_row, blank_col + 1))
#         move_row, move_col = random.choice(possible_moves)
#         board[blank_row][blank_col], board[move_row][move_col] = board[move_row][move_col], board[blank_row][blank_col]

# def fifteen_game():

#     board = [[0, 1, 2, 3], [4, 5, 6, 7], [8, 9, 10, 11], [12, 13, 14, 15]]
#     shuffle_board(board)

#     while not is_game_over(board):
#         print_board(board)
#         row, col = map(int, input("Введіть рядок та стовпчик числа, яке хочете змістити (через пробіл): ").split())
#         if is_valid_move(board, row, col):
#             blank_row, blank_col = find_blank(board)
#             board[blank_row][blank_col], board[row][col] = board[row][col], board[blank_row][blank_col]
#         else:
#             print("Недопустимий хід! Спробуйте ще раз.")

#     print("Ви перемогли! Гра завершена.")

# def is_game_over(board):

#     num = 1
#     for i in range(len(board)):
#         for j in range(len(board[i])):
#             if board[i][j] != num % 16:
#                 return False
#             num += 1
#     return True

# fifteen_game()
