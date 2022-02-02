def a_move(n):
    if n%2==0:
        return n-(n//2)
    else:
        return n-2

def b_move(n):
    if n%3==0:
        return n-(n*2//3)
    else:
        return n-3
number_of_win_turn = 3
max_s = 37
min_s= 1
moves = ['0'*(number_of_win_turn-len(bin(i)[2:]))+bin(i)[2:] for i in range(2**number_of_win_turn)]
def who_win(move, n):
    for turn in range(len(move)):
        if move[turn] == '0':
            n = a_move(n)
        elif move[turn] == '1':
            n = b_move(n)
        if turn == 0:
            if n==1:
                pw = True
            else:
                pw = False
        elif turn == 1:
            if n==1:
                vw = True
            else:
                vw = False
        elif turn == 2:
            if n ==1 :
                p2w = True
            else:
                p2w = False
    if not pw and not vw and p2w:
        return True
    return False
def game1():
    for s in range(min_s,max_s+1,1):
        for move in moves:
            if who_win(move,s):
                if move[1]=='0':
                    temp = '1'
                else:
                    temp =  '0'
                if who_win(move[0]+temp+'0',s) or who_win(move[0]+temp+'1',s):
                    return s
def game2():
    for s in range(max_s,min_s-1,-1):
        for move in moves:
            if who_win(move,s):
                if move[1]=='0':
                    temp = '1'
                else:
                    temp =  '0'
                if who_win(move[0]+temp+'0',s) or who_win(move[0]+temp+'1',s):
                    return s
            
                    
                      
    
                    
print(f'{game1()}{game2()}')
                
