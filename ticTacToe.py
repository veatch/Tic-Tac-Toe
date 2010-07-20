def draw_grid():
    for i in range(width_and_height):
        row = ""
        top_row = ""
        bottom_row = ""
        for j in range(width_and_height):
            cell_number = j+(width_and_height*i)
            if cell_list[cell_number] == ' ':
                top_row += "%s " % (cell_number + 1) #grid starts at 0, display starts at 1
            else:
                top_row += '  '
            if j % width_and_height != width_and_height-1:
                top_row += " *"
            bottom_row += "  %s" % (cell_list[cell_number])
            if j % width_and_height != width_and_height-1:
                bottom_row += "*"
        print top_row
        print bottom_row
        if i != width_and_height-1:
            print "****"*width_and_height


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
    if 0 <= cell_to_mark < width_and_height**2:
        if cell_list[cell_to_mark] != ' ':
            print "That cell is already marked. Try again."
            return False
        return True
    print "That number isn't on the grid. Try again."
    return False

def computer_move():
    index = is_near_win(cell_list, computer_marker)
    if index >= 0:
        return index
    index = is_near_win(cell_list, human_marker)
    if index >= 0:
        return index
    index = find_move_with_fewest_human_wins()
    if index >= 0:
        return index
    index = width_and_height/2 # center column
    index += width_and_height*index # center row
    if cell_list[index] == ' ':
        return index
    return cell_list.index(' ');

def is_near_win(list_to_check, marker): 
    if list_to_check.count(marker) >= width_and_height-1:
        open_space = 0;
        for i in range ((width_and_height**2)-1):
            temp_list = list_to_check[:]
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

#loops here should be changed to bump up j when open_space is bumped up, or something
def find_move_with_fewest_human_wins():
    open_space = 0
    #iterate over grid
    for i in range ((width_and_height**2)-1):
        temp_list = cell_list[:]
        try:
            open_space = temp_list.index(' ', open_space)
            #try marking open space with computer_marker
            temp_list[open_space] = computer_marker
            #if that sets up a computer win, assume human will block
            index = is_near_win(temp_list, computer_marker)
            if index >= 0:
                temp_list[index] = human_marker
                finishing_open_space = 0
                possible_wins = 0
                #after human block, check remaining empty spaces
                for j in range ((width_and_height**2)-1):
                    finishing_list = temp_list[:]
                    try:
                        finishing_open_space = finishing_list.index(' ', finishing_open_space)
                        finishing_list[finishing_open_space] = human_marker
                        win = check_for_win(finishing_list, human_marker)
                        #count how many spaces could be human wins
                        if win:
                            possible_wins+= 1
                    except ValueError:
                        pass
                    finishing_open_space += 1
                #if 1 or 0, computer will be able to block, so return the original open space
                if possible_wins <= 1:
                    return open_space
        except ValueError:
            pass
        #otherwise, there are more human wins available than can be blocked, so try next space
        open_space += 1
    return -1

def next_move():
    if is_human_turn:
        valid = False
        if not first_move:
            cmd_line_messg = "Your move, human. Remember, you're O: "
        else:
            cmd_line_messg = 'Welcome to tic tac toe, human. Pick your cell: '
        while not valid:
            try:
                cell_to_mark = int(raw_input(cmd_line_messg))-1 #grid starts at 0, display starts at 1
                valid = is_valid_input(cell_to_mark)
            except ValueError:
                print "That input is not valid. Try one of the numbers on the grid."
    else:
        print
        print "Let's see..."
        print
        cell_to_mark = computer_move()
    mark_cell(cell_to_mark, current_player_marker())

width_and_height = 3
cell_list = [' '] * width_and_height**2
winner = None
is_human_turn = True
human_marker = 'O'
computer_marker = 'X'
first_move = True

draw_grid()
next_move()
first_move = False

while winner == None:
    is_human_turn = not is_human_turn
    draw_grid()
    next_move()
    winner = check_for_win(cell_list, current_player_marker())

draw_grid()
print
if winner == "draw":
    print "It's a draw!"
elif is_human_turn:
    print "You won?? That's impossible!"
else:
    print "I WIN"