import helper
import math
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

# cost from current loc to target loc
def h(cur_loc, target_loc):
    return 10* (math.fabs(cur_loc[0] - target_loc[0]) + math.fabs(cur_loc[1] - target_loc[1]))

# loc_info:
# cost from start loc to current loc
def g(loc_info, open_list_dict):
    # 1. get parent
    # 2. if parent == null, g = 0
    # 3. if parent !=null, g = parent.g + 10


    parent_loc = open_list_dict[loc_info][0]
    if parent_loc:
        return open_list_dict[parent_loc][1] + 10
    else:
        return 0

def sort_key_open_list_by_f(cur_cell):
    return cur_cell[1]

# find the path by A*
def a_star(env_data):
    # data structure
    # open list: [(cur_loc_row, cur_loc_col),f]
    # open list dict: {(cur_loc_row, cur_loc_col): [(parent_loc_row, parent_loc_col), g, h]}
    # close list [(cur_loc_row, cur_loc_col)]
    open_list = []
    open_list_dict = {}
    close_list = []

    # find the start loc and target loc
    start_loc = get_loc_by_value(env_data, 1)
    target_loc = get_loc_by_value(env_data, 3)

    # create open list
    open_list_dict[start_loc] = [None]
    open_list_dict[start_loc].append(0)
    open_list_dict[start_loc].append(h(start_loc, target_loc))
    open_list.append([start_loc, open_list_dict[start_loc][1] + open_list_dict[start_loc][2]])

    # loop until target_loc is in open list or open list is empty
    while open_list:
    ##  for each item in open list, find the one with the smallest F as cur_loc.
        cur_item = open_list.pop(0)

    ##  put it to close list
        close_list.append(cur_item[0])
        if cur_item == target_loc:
            break;
    ##  loop for each adjacent items of cur_loc
        for adjacent in valid_next_loc(env_data, cur_item[0]):
            if adjacent in close_list:
                continue
    ###     if not valid, or already in close_list, ignore
    ###     if already in open list, check the path from cur_loc to it, calculate new_g, if new_g < old_g, it means
    ###     that, it is a better path, update its parent_loc, g and f. Resort open list by f in ascending order.
            for open_list_item in open_list:
                if open_list_item[0] == adjacent:
                    new_g = g(adjacent, open_list_dict)
                    old_g = open_list_dict[adjacent][1]
                    if new_g < old_g:
                        open_list_dict[adjacent][1] = new_g
                        open_list_item[1] = new_g + open_list_dict[adjacent][2]
                        open_list_item[0] = cur_item[0]
                        open_list.sort(key=sort_key_open_list_by_f)
    ###     if not in open list, put it to open list, and set cur_loc as the parent of it, record f, g and h
            else:
                open_list_dict[adjacent] = [cur_item[0]]
                open_list_dict[adjacent].append(10 + open_list_dict[cur_item[0]][1])
                open_list_dict[adjacent].append(h(adjacent, target_loc))
                open_list.append([adjacent, open_list_dict[cur_item[0]][1] + open_list_dict[cur_item[0]][2]])
                open_list.sort(key=sort_key_open_list_by_f)
    # out put path
    for step in close_list:
        print(step)

a_star(env_data)