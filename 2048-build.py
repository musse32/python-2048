"""
Clone of 2048 game.
"""

import poc_2048_gui

# Directions, DO NOT MODIFY
UP = 1
DOWN = 2
LEFT = 3
RIGHT = 4

# Offsets for computing tile indices in each direction.
# DO NOT MODIFY this dictionary.
OFFSETS = {UP: (1, 0),
           DOWN: (-1, 0),
           LEFT: (0, 1),
           RIGHT: (0, -1)}

def merge(line):
    """
    Helper function that merges a single row or column in 2048
    """
    # replace with your code from the previous mini-project
    lst2 = []
    for ndx,val in enumerate(line): ##Append the none-zero values into new list
        if val !=0:
            lst2.append(val)

    lst2.extend([0]*(len(line)-len(lst2))) ##Add zeros to the tail of new list

    max_ndx = len(lst2)-1      			#Limit the loop to second to last index
    for ndx in range(len(lst2)):
        if ndx < max_ndx:
            if lst2[ndx]==lst2[ndx+1]:  #In list2, if values are the same:
                lst2[ndx] = lst2[ndx]*2 #Double the legal value
                lst2[ndx+1] = 0		#Replace the next value with 0
    lst3 = []
    for ndx,val in enumerate(lst2):
        if val !=0:
            lst3.append(val)
    lst3.extend([0]*(len(lst2)-len(lst3)))
    return lst3
class TwentyFortyEight:
    """
    Class to run the game logic.
    """

    def __init__(self, grid_height, grid_width):
        # replace with your code
        self.grid_height = grid_height
        self.grid_width = grid_width
        self.reset()
        self.grid = self.grid

    def reset(self):
        """
        Reset the game so the grid is empty except for two
        initial tiles.
        """
        # replace with your code
        self.grid = [[0 for col in range(self.grid_width)] for row in range(self.grid_height)]
        self.new_tile()
        self.new_tile()
        return self.grid
    
    def __str__(self):
        """
        Return a string representation of the grid for debugging.
        """
        # replace with your code
        return '{grid}'.format(grid=self.grid)

    def get_grid_height(self):
        """
        Get the height of the board.
        """
        # replace with your code
        return self.grid_height

    def get_grid_width(self):
        """
        Get the width of the board.
        """
        # replace with your code
        return self.grid_width

    def move(self, direction):
        """
        Move all tiles in the given direction and add
        a new tile if any tiles moved.
        """
        #Get each board location
        #Create grid with same deminsions as board
        loc = [[0 for col in range(6)] for row in range(4)]
        for i in range(board.grid_height):
            for j in range(board.grid_width):
                loc[i][j] = (i,j)
                
        #Get initial locations for lines to merge for given direction
        init_loc = {}
        init_lines = {}
        final_loc = {}
        final_lines = {}
        
        init_loc[UP] = [(0, col) for col in range(board.grid_width)]
        init_lines[UP] = [[(i[0] +j, i[1]) for j in range(board.grid_height)] for i in init_loc[UP]]
        
        init_loc[DOWN] = [(board.grid_height-1, col) for col in range(board.grid_width)]
        init_lines[DOWN] = [[(i[0] -j, i[1]) for j in range(board.grid_height)] for i in init_loc[DOWN]]
        
        init_loc[LEFT] = [(row, 0) for row in range(board.grid_height)]
        init_lines[LEFT] = [[(i[0], i[1]+j) for j in range(board.grid_width)] for i in init_loc[LEFT]]
        
        init_loc[RIGHT] = [(row, board.grid_width-1) for row in range(board.grid_height)]
        init_lines[RIGHT] = [[(i[0], i[1]-j) for j in range(board.grid_width)] for i in init_loc[RIGHT]]
        
        #find values for the init_lines
        tomerge = [[board.grid[j[0]][j[1]] for j in i] for i in init_lines[direction]]
        
        #merge each of the values
        merged = []
        for i in tomerge:
            merged.append(merge(i))
        
        #Find locations to return the values
        #final_loc[UP] = [(row, 0) for row in range(len(merged))]
        #final_lines[UP] = [[(j, i) for j in range(board.grid_width)] for i in range(board.grid_height)]
        
        #final_loc[LEFT] = [(col, 0) for row in range(len(merged))]
        #final_lines[LEFT] = [[(j, i) for j in range(board.grid_height)] for i in range(board.grid_width)]
        #create the new grid with the new lines but same as old grid shape
        #final_grid = {}
        #final_grid[UP] = [[merged[j[0]][j[1]] for j in i] for i in final_lines[UP]]
        #final_grid[LEFT] = [[merged[j[0]][j[1]] for j in i] for i in final_lines[UP]]
        for i in range(len(merged)):
            for j in range(len(merged[i])):
                board.set_tile(init_lines[direction][i][j][0], init_lines[direction][i][j][1], merged[i][j])

        
        #Return the values into the original board
        #replace with your code
        #Add a random tile
        self.new_tile()
        return self.grid
    def new_tile(self):
        """
        Create a new tile in a randomly selected empty
        square.  The tile should be 2 90% of the time and
        4 10% of the time.
        """
        # replace with your code
        newtile = random.choice([2]*9+[4])
        options = []
        for row in range(len(self.grid)):
            for col in range(len(self.grid[row])):
                if self.grid[row][col] == 0:
                    options.append([row, col])
        selection = random.choice(options)
        self.grid[selection[0]][selection[1]] = newtile
        return '{newtile} placed at {selection}'.format(newtile=newtile, selection=selection)
    
    def set_tile(self, row, col, value):
        """
        Set the tile at position row, col to have the given value.
        """
        self.grid[row][col] = value
        return '{value} set at ({row}, {col})'.format(value=value, row=row, col=col)

    def get_tile(self, row, col):
        """
        Return the value of the tile at position row, col.
        """
        # replace with your code
        return self.grid[row][col]


poc_2048_gui.run_gui(TwentyFortyEight(4, 4))
