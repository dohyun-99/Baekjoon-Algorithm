#N=지도의 세로 길이, M=지도의 가로 길이, K=이동횟수
N, M, K=map(int, input().split())
board=[[0 for i in range(M+1)]]
for i in range(N):
    line=[0,]+list(map(int, input().split()))+[0]
    board.append(line)
board.append([0 for i in range(M+1)])


# 보드판 이동 - 방향에 따라 좌표 이동
# 조건 : 이동 방향에 칸이 없으면 반대 방향으로 돌아감!

# # 1. 주사위가 이동 방향으로 한 칸 굴러간다. 만약, 이동 방향에 칸이 없다면, 이동 방향을 반대로 한 다음 한 칸 굴러간다.
# 주사위가 한칸 굴러가기 - 현재 위치 파악, 주사위의 방향에 따라 한칸 구름(좌표 이동) & 주사위는 새로운 주사위로 대체
def move_board(dir,loc): #(x,y)
    origin_loc = loc[:]
    
    if dir%4==0: # Right
        loc[1]+=1
    elif dir%4==1: #Down
        loc[0]+=1
    elif dir%4==2: #Left
        loc[1]-=1
    elif dir%4==3: #Up
        loc[0]-=1

    if board[loc[0]][loc[1]] == 0:
        dir+=2
        # print(dir)
        return move_board(dir, origin_loc)   
    return dir, loc

def dice_plane(origin_dice, direction):
    dice_loc=[]

    # 동 = Right (→)
    if direction%4==0:
        dice_loc=[1,6,2,3,5,4]

    # 서 = Left (←)
    if direction%4==2:
        dice_loc=[1,3,4,6,5,2]
    
    # 남 = Down (↓)
    if direction%4==1:
        dice_loc=[6,2,1,4,3,5]
    
    # 북 = Up(↑)
    if direction%4==3:
        dice_loc=[3,2,5,4,6,1]

    new_dice=[]
    for i in dice_loc:
        new_dice.append(origin_dice[i-1])
    # print(new_dice)
    return new_dice


# # 2. 주사위가 도착한 칸 (x, y)에 대한 점수를 획득한다.
def get_score(location): #연속해서 이동할 수 있는 칸의 갯수 세기
    same_score=[location]
    score_num=board[location[0]][location[1]]
    # print("Board_score",score_num)
    def search_4ways(point):
        x=point[0]
        y=point[1]
        four_ways=[[x-1,y],[x,y-1],[x,y+1],[x+1,y]]
        for i in four_ways:
            if (board[i[0]][i[1]] == score_num) and (i not in same_score):
                same_score.append(i)
                search_4ways(i)
            elif (board[i[0]][i[1]] == score_num) and (i in same_score):
                pass
        return same_score
    # print("Score", len(same_score))
    return len(search_4ways(location))*score_num



# # 3. 주사위의 아랫면에 있는 정수 A와 주사위가 있는 칸 (x, y)에 있는 정수 B를 비교해 이동 방향을 결정한다.
# #A > B인 경우 이동 방향을 90도 시계 방향으로 회전시킨다.
# #A < B인 경우 이동 방향을 90도 반시계 방향으로 회전시킨다.
# #A = B인 경우 이동 방향에 변화는 없다.
def move_dice(last_move, dice_map, location):
    A=int(dice_map[-1]) # 주사위 아랫면의 정수
    B=board[location[0]][location[1]] # 주사위가 있는 칸의 정수
    if A>B:
        return last_move+1
    elif A<B:
        return last_move-1
    elif A == B:
        return last_move

direction=0 #숫자
score=0
dice=[2,4,1,3,5,6]
current_loc=[1,1]
# print(current_loc)
score_board=[]
for i in range(N+1):
    score_board.append([0 for i in range(M+1)])

# ()
for i in range(K):
    # print(f"{i+1}th move")
    direction, current_loc = move_board(direction, current_loc)
    dice=dice_plane(dice,direction)
    # print(current_loc)
    if score_board[current_loc[0]][current_loc[1]]>0:
        score+=score_board[current_loc[0]][current_loc[1]]
    else:
        score+=get_score(current_loc)
        score_board[current_loc[0]][current_loc[1]]=get_score(current_loc)
    direction = move_dice(direction, dice, current_loc)
    # print(direction%4)
    # print(score, dice)

print(score)

