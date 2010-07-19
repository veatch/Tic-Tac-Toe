def draw_grid():
    for i in range(width_and_height):
        row = ""
        for j in range(width_and_height):
            row += "%s " % (j+1+(width_and_height*i))
            if j % width_and_height != width_and_height-1:
                row += "*"
        print row
        #print "%s *%s *%s" % (1+(width_and_height*i), 2+(width_and_height*i), 3+(width_and_height*i))
        row = ""
        for j in range(width_and_height):
            row += " %s" % (cell_list[j+(width_and_height*i)])
            if j % width_and_height != width_and_height-1:
                row += "*"
        print row
        #print " %s* %s* %s" % (cell_list[i])
        if i != width_and_height-1:
            print "***"*width_and_height


def current_player_marker():
    if is_human_turn:
        return human_marker
    else:
        return computer_marker


def mark_cell(cell, marker):
    cell_list[cell] = marker

def check_for_win(list_to_check, marker):
    if list_to_check.count(marker) >= width_and_height:
        for i in range(width_and_height):
            if list_to_check[i] == marker:
                is_winner = check_for_vertical_win(list_to_check, i, marker)
                if is_winner:
                    return True
            if list_to_check[i*width_and_height] == marker:
                is_winner = check_for_horizontal_win(list_to_check, i*width_and_height, marker)
                if is_winner:
                    return True
            is_winner = check_for_left_diagonal_win(list_to_check, marker)
            if is_winner:
                return True
            is_winner = check_for_right_diagonal_win(list_to_check, marker)
            if is_winner:
                return True
    if ' ' not in list_to_check:
        return "draw"
    return None

def check_for_vertical_win(list_to_check, column, marker):
    maybe_winner = True
    for j in range (1, width_and_height):
        if list_to_check[column+(j*width_and_height)] != marker:
            maybe_winner = False
            break
    return maybe_winner

def check_for_horizontal_win(list_to_check, row, marker):
    maybe_winner = True
    for j in range (1, width_and_height):
        if list_to_check[row+j] != marker:
            maybe_winner = False
            break
    return maybe_winner

def check_for_left_diagonal_win(list_to_check, marker):
    maybe_winner = True
    for i in range (width_and_height):
        if list_to_check[i+(i*width_and_height)] != marker:
            maybe_winner = False
            break
    return maybe_winner

def check_for_right_diagonal_win(list_to_check, marker):
    maybe_winner = True
    for i in range (width_and_height):
        if list_to_check[width_and_height-1+(i*(width_and_height-1))] != marker:
            maybe_winner = False
            break
    return maybe_winner

def is_valid_input(cell_to_mark):
    if 0 < cell_to_mark <= width_and_height**2:
        if cell_list[cell_to_mark] != ' ':
            print "That cell is already marked. Try again."
            return False
        return True
    print "That number isn't on the grid. Try again."
    return False

def computer_move():
    index = is_near_win(computer_marker)
    if index >= 0:
        return index
    index = is_near_win(human_marker)
    if index >= 0:
        return index
    index = width_and_height/2 # center column
    index += width_and_height*index # center row
    if cell_list[index] == ' ':
        return index
    return cell_list.index(' ');

def is_near_win(marker): 
    if cell_list.count(marker) >= width_and_height-1:
        open_space = 0;
        for i in range ((width_and_height**2)-1):
            temp_list = cell_list[:]
            try:
                open_space = temp_list.index(' ', open_space)
                temp_list[open_space] = marker
                win = check_for_win(temp_list, marker)
                if win:
                    return open_space
            except ValueError:
                pass
            open_space += 1
    return -1

width_and_height = 3
cell_list = [' '] * width_and_height**2
winner = None
is_human_turn = True
human_marker = 'O'
computer_marker = 'X'

draw_grid()
#todo update first move:
cell_to_mark = input('Welcome to tic tac toe, human. Pick your cell: ')-1
mark_cell(cell_to_mark, current_player_marker())

while winner == None:
    is_human_turn = not is_human_turn
    draw_grid()
    if is_human_turn:
        valid = False
        while not valid:
            try:
                cell_to_mark = int(raw_input("Your move, human. Remember, you're O: "))-1 #grid starts at 0, display starts at 1
                valid = is_valid_input(cell_to_mark)
            except ValueError:
                print "That input is not valid. Try one of the numbers on the grid."
    else:
        cell_to_mark = computer_move()
    mark_cell(cell_to_mark, current_player_marker())
    winner = check_for_win(cell_list, current_player_marker())

if winner == "draw":
    print "It's a draw!"
elif is_human_turn:
    print "human wins? wtf"
else:
    print "I WIN"