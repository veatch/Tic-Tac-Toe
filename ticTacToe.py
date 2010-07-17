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


width_and_height = 3
cell_list = [' '] * width_and_height**2
draw_grid()
cell_to_mark = input('Welcome to tic tac toe, human. Pick your cell: ')
cell_to_mark -= 1 # grid starts at 0, grid display starts at 1
cell_list[cell_to_mark] = '0'
draw_grid()