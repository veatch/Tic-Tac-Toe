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


def mark_cell(cell):
    cell -= 1 # grid starts at 0, grid display starts at 1
    cell_list[cell] = current_player_marker()

def check_for_win():
    if cell_list.count(current_player_marker()) >= width_and_height:
        for i in range(width_and_height):
            marker = current_player_marker()
            if cell_list[i] == marker:
                is_winner = check_for_vertical_win(i, marker)
                if is_winner:
                    return True
            if cell_list[i*width_and_height] == marker:
                is_winner = check_for_horizontal_win(i*width_and_height, marker)
                if is_winner:
                    return True
            is_winner = check_for_left_diagonal_win(marker)
            if is_winner:
                return True
            is_winner = check_for_right_diagonal_win(marker)
            if is_winner:
                return True
    return None

def check_for_vertical_win(column, marker):
    maybe_winner = True
    for j in range (1, width_and_height):
        if cell_list[column+(j*width_and_height)] != marker:
            maybe_winner = False
            break
    return maybe_winner

def check_for_horizontal_win(row, marker):
    maybe_winner = True
    for j in range (1, width_and_height):
        if cell_list[row+j] != marker:
            maybe_winner = False
            break
    return maybe_winner

def check_for_left_diagonal_win(marker):
    maybe_winner = True
    for i in range (width_and_height):
        if cell_list[i+(i*width_and_height)] != marker:
            maybe_winner = False
            break
    return maybe_winner

def check_for_right_diagonal_win(marker):
    maybe_winner = True
    for i in range (width_and_height):
        if cell_list[width_and_height-1+(i*(width_and_height-1))] != marker:
            maybe_winner = False
            break
    return maybe_winner

width_and_height = 3
cell_list = [' '] * width_and_height**2
winner = None
is_human_turn = True
human_marker = 'O'
computer_marker = 'X'

draw_grid()
cell_to_mark = input('Welcome to tic tac toe, human. Pick your cell: ')
mark_cell(cell_to_mark)

while winner == None:
    is_human_turn = not is_human_turn
    draw_grid()
    cell_to_mark = input("Your move, human. Remember, you're O: ")
    mark_cell(cell_to_mark)
    winner = check_for_win()

if is_human_turn:
    print "human wins? wtf"
else:
    print "I WIN"