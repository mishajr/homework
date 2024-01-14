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

# def is_solvable(board):
#     inversions = 0
#     flatten_board = [num for row in board for num in row if num != 0]
    
#     for i in range(len(flatten_board) - 1):
#         for j in range(i + 1, len(flatten_board)):
#             if flatten_board[i] > flatten_board[j]:
#                 inversions += 1

#     return inversions % 2 == 0

# def get_empty_position(board):
#     for i, row in enumerate(board):
#         for j, num in enumerate(row):
#             if num == 0:
#                 return i, j

# def shuffle_board():
#     numbers = list(range(1, 16))
#     random.shuffle(numbers)

#     board = [numbers[i:i+4] for i in range(0, 16, 4)]
    
#     if not is_solvable(board):

#         return shuffle_board()

#     return board

# def move(board, direction):
#     empty_i, empty_j = get_empty_position(board)

#     if direction == "up" and empty_i > 0:
#         board[empty_i][empty_j], board[empty_i - 1][empty_j] = board[empty_i - 1][empty_j], board[empty_i][empty_j]
#     elif direction == "down" and empty_i < 3:
#         board[empty_i][empty_j], board[empty_i + 1][empty_j] = board[empty_i + 1][empty_j], board[empty_i][empty_j]
#     elif direction == "left" and empty_j > 0:
#         board[empty_i][empty_j], board[empty_i][empty_j - 1] = board[empty_i][empty_j - 1], board[empty_i][empty_j]
#     elif direction == "right" and empty_j < 3:
#         board[empty_i][empty_j], board[empty_i][empty_j + 1] = board[empty_i][empty_j + 1], board[empty_i][empty_j]

# def is_solved(board):
#     return all(board[i][j] == i * 4 + j + 1 for i in range(4) for j in range(4)) and board[3][3] == 0

# def main():
#     board = shuffle_board()

#     while True:
#         print_board(board)

#         if is_solved(board):
#             print("Щиро вітаю! Ви розгадали головоломку.")
#             break

#         direction = input("Введіть напрямок (up, down, left, right), щоб перемістити порожнє місце, або quit, щоб вийти: ")

#         if direction == 'quit':
#             print("Вихід з гри.")
#             break

#         move(board, direction)

# if __name__ == "__main__":
#     main()