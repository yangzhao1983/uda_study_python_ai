import helper
env_data=helper.fetch_maze()

#TODO 1模拟环境的行数
rows = len(env_data)

#TODO 2模拟环境的列数
columns = len(env_data[0])

#TODO 3取出模拟环境第三行第六列的元素
row_3_col_6 = env_data[2][5]

print("迷宫共有", rows, "行", columns, "列，第三行第六列的元素是", row_3_col_6)

#TODO 4计算模拟环境中，第一行的的障碍物个数。
number_of_barriers_row1 = len([col for col in env_data[0] if col==2])

#TODO 5计算模拟环境中，第三列的的障碍物个数。
number_of_barriers_col3 = len([row[2] for row in env_data if row[2]==2])

print("迷宫中，第一行共有", number_of_barriers_row1, "个障碍物，第三列共有", number_of_barriers_col3, "个障碍物。")

start_coord = None
destination_coord = None
for row_index in range(len(env_data)):
    for col_index in range(len(env_data[row_index])):
        if env_data[row_index][col_index] == 1:
            start_coord = (row_index, col_index)
        elif env_data[row_index][col_index] == 3:
            destination_coord = (row_index, col_index)

loc_map = {"start": start_coord, "destination" : destination_coord} #TODO 6按照上述要求创建字典

robot_current_loc = loc_map["start"] #TODO 7保存机器人当前的位置

def is_move_valid_special(loc, act):
    """
    Judge wether the robot can take action act
    at location loc.

    Keyword arguments:
    loc -- tuple, robots current location
    act -- string, robots meant action
    """
    #TODO 8
    cur_row = loc[0]
    cur_col = loc[1]
    if act == 'u':
        if cur_row - 1 < 0 or env_data[cur_row-1][cur_col] == 2:
            return False
    elif act == 'd':
        if cur_row + 1 == len(env_data) or env_data[cur_row+1][cur_col] == 2:
            return False
    elif act == 'l':
        if cur_col - 1< 0 or env_data[cur_row][cur_col-1] == 2:
            return False
    else:
        if cur_col + 1 == len(env_data[cur_row]) or env_data[cur_row][cur_col+1] == 2:
            return False

    return True

def is_move_valid(env_data, loc, act):
    """
    Judge wether the robot can take action act
    at location loc.

    Keyword arguments:
    env -- list, the environment data
    loc -- tuple, robots current location
    act -- string, robots meant action
    """
    #TODO 9
    cur_row = loc[0]
    cur_col = loc[1]
    if act == 'u':
        if cur_row - 1 < 0 or env_data[cur_row-1][cur_col] == 2:
            return False
    elif act == 'd':
        if cur_row + 1 == len(env_data) or env_data[cur_row+1][cur_col] == 2:
            return False
    elif act == 'l':
        if cur_col - 1< 0 or env_data[cur_row][cur_col-1] == 2:
            return False
    else:
        if cur_col + 1 == len(env_data[cur_row]) or env_data[cur_row][cur_col+1] == 2:
            return False

    return True

def valid_actions(env_data, loc):
    candidate_steps = ['u','d','l','r']
    feasible_steps = [act for act in candidate_steps if is_move_valid(env_data, loc, act)]
    return feasible_steps

##TODO 11 从头定义、实现你的函数
def move_robot(loc, act):
    cur_row = loc[0]
    cur_col = loc[1]
    if is_move_valid_special(loc, act):
        if act == 'u':
            cur_row -= 1
        elif act == 'd':
            cur_row += 1
        elif act == 'l':
            cur_col -= 1
        else:
            cur_col += 1
    return cur_row, cur_col

##TODO 12 从头实现你的函数
import random
def random_choose_actions(env_data, loc):
    for step in range(300):
        feasible_acts = valid_actions(env_data, loc)
        next_act = random.choice(feasible_acts)
        next_loc = move_robot(loc, next_act)
        if env_data[next_loc[0]][next_loc[1]] == 3:
            print("在第{}个回合找到宝藏".format(step + 1))
            break
        loc = next_loc


#定义操作
# u:上
# d:下
# l:左
# r:右
acts = ['u','d','l','r']

acts_valid_dict = {
    'u' : lambda env_data, loc : loc[0] - 1 >= 0 and env_data[loc[0]-1][loc[1]] != 2,
    'd' : lambda env_data, loc : loc[0] + 1 < len(env_data) and env_data[loc[0]+1][loc[1]] != 2,
    'l' : lambda env_data, loc : loc[1] - 1 >= 0 and env_data[loc[0]][loc[1]-1] != 2,
    'r' : lambda env_data, loc : loc[0] + 1 <len(env_data[loc[0]]) and env_data[loc[0]][loc[1]+1] != 2,
}

def is_move_valid(env_data, loc, act):
    """
    Judge wether the robot can take action act
    at location loc.

    Keyword arguments:
    env -- list, the environment data
    loc -- tuple, robots current location
    act -- string, robots meant action
    """
    #TODO 9
    cur_row = loc[0]
    cur_col = loc[1]
    if act == 'u':
        if cur_row - 1 < 0 or env_data[cur_row-1][cur_col] == 2:
            return False
    elif act == 'd':
        if cur_row + 1 == len(env_data) or env_data[cur_row+1][cur_col] == 2:
            return False
    elif act == 'l':
        if cur_col - 1< 0 or env_data[cur_row][cur_col-1] == 2:
            return False
    else:
        if cur_col + 1 == len(env_data[cur_row]) or env_data[cur_row][cur_col+1] == 2:
            return False

    return True

def is_move_valid_special(loc, act):
    """
    Judge wether the robot can take action act
    at location loc.

    Keyword arguments:
    loc -- tuple, robots current location
    act -- string, robots meant action
    """
    #TODO 8
    cur_row = loc[0]
    cur_col = loc[1]
    if act == 'u':
        if cur_row - 1 < 0 or env_data[cur_row-1][cur_col] == 2:
            return False
    elif act == 'd':
        if cur_row + 1 == len(env_data) or env_data[cur_row+1][cur_col] == 2:
            return False
    elif act == 'l':
        if cur_col - 1< 0 or env_data[cur_row][cur_col-1] == 2:
            return False
    else:
        if cur_col + 1 == len(env_data[cur_row]) or env_data[cur_row][cur_col+1] == 2:
            return False

    return True

## TODO 10 从头定义、实现你的函数
def valid_actions(env_data, loc):
    candidate_steps = ['u','d','l','r']
    feasible_steps = [act for act in candidate_steps if is_move_valid(env_data, loc, act)]
    return feasible_steps

##TODO 11 从头定义、实现你的函数
def move_robot(loc, act):
    cur_row = loc[0]
    cur_col = loc[1]
    if is_move_valid_special(loc, act):
        if act == 'u':
            cur_row -= 1
        elif act == 'd':
            cur_row += 1
        elif act == 'l':
            cur_col -= 1
        else:
            cur_col += 1
    return cur_row, cur_col

def valid_next_loc(env_data, loc):
    feasible_acts = valid_actions(env_data, loc)
    return (move_robot(loc, next_act) for next_act in feasible_acts)

def get_loc_by_value(env_data, val):
    for row in range(len(env_data)):
        for col in range(len(env_data[row])):
            if env_data[row][col] == val:
                return row, col

    return None

def output_path(env_data):
    ## get target loc
    target_loc = get_loc_by_value(env_data, 3)

    ## define a list as queue
    queue = []

    ## define a two-dimension list visited
    visited = []
    for row_num in range(len(env_data)):
        visited_row = []
        visited.append(visited_row)
        for col_num in range(len(env_data[row_num])):
            visited_row.append(False)

    ## define a dict, (row, col) : (row, col), $cur_loc : $ parent_loc
    dict={}
    dict[target_loc]=None

    ## push start loc to queue
    queue.append(target_loc)

    ## loop,
    while len(queue):
        #### 0. get the top of queue as cur_loc,
        cur_loc = queue.pop(0)

        #### 1. if cur_loc is start loc, output the path, return.
        if env_data[cur_loc[0]][cur_loc[1]] == 1:
            ##### out put the path
            ans = []
            while cur_loc:
                ans.append(cur_loc)
                cur_loc = dict[cur_loc]
            print('->'.join(map(str, ans)))
            return

        #### 1.1 mark it as visited
        visited[cur_loc[0]][cur_loc[1]] = True

        #### 2. find the valid next loc for the cur_loc

        #### 3. for each valid next loc:
        for next_loc in valid_next_loc(env_data, cur_loc):
            ####        if is not visited, create new item in dict, put it to queue
            if not visited[next_loc[0]][next_loc[1]]:
                dict[next_loc] = cur_loc
                queue.append(next_loc)

output_path(env_data)