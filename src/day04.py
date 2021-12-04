import sys


def winner(board):
    for i in range(0, 25, 5):
        if board[i] == board[i + 1] == board[i + 2] == board[i + 3] == board[i +
                                                                             4]:
            return True
    for i in range(5):
        if board[i] == board[i + 5] == board[i + 10] == board[i +
                                                              15] == board[i +
                                                                           20]:
            return True
    return False


f = open(sys.argv[1])
data = f.read().split('\n\n')

numbers = [int(x) for x in data[0].split(',')]
data.remove(data[0])

boards = []
for d in data:
    boards.append([int(x) for x in d.split()])

part1 = 0
part2 = 0
done1 = False
done2 = False
winners = set()
for number in numbers:
    if done2:
        break
    for board_id, board in enumerate(boards):
        for i in range(len(board)):
            if board[i] == number:
                board[i] = -1
        if winner(board):
            winners.add(board_id)
            if not done1:
                done1 = True
                for b in board:
                    if b != -1:
                        part1 += b
                part1 *= number
            if len(winners) == len(boards):
                done2 = True
                for b in board:
                    if b != -1:
                        part2 += b
                part2 *= number
                break

print(f'{part1 = }')
print(f'{part2 = }')
