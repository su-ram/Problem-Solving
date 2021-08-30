board = list(input())
poli = ['AAAA','BB']
index = 0

def can_place(start, poli):
    substring = ''.join(board[start:start+len(poli)])
    if len(substring) == len(poli) and substring.count('.') == 0 :
        return True
    return False


while index < len(board):
    if board[index] == 'X':
        if can_place(index, poli[0]):
            board[index:index+len(poli[0])] = poli[0]
            index += 4
        elif can_place(index, poli[1]):
            board[index:index+len(poli[1])] = poli[1]
            index += 2
        else:
            index += 1
        continue
    index += 1
print(''.join(board) if board.count('X') == 0 else -1)

