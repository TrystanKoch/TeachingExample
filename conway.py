from time import sleep

class ConwayLifeBoard:
    
    def __init__(self, n: int):
        """Initialize a square board of height and width n. The
           starting array contains only cells in the off, or False,
           state."""
        self.array = [[False for j in range(n)] for i in range(n)]
        self.size = n


    def __str__(self) -> str:
        """This string will be an array of 1 and 0, representing
           True and False, respectively."""
        string = ""
        for i in range(self.size):
            string += " ".join(map(str,map(int,self.array[i]))) + "\n"
        return string.replace("0", " ")


    def toggle(self, i: int, j: int) -> None:
        """Toggles the truth value of the cell (row i, col j)."""
        self.array[i][j] = not self.array[i][j]


    def get_cell(self, i: int, j: int) -> bool:
        """Get the state of the cell (row i, col j).
           Any cells outside of the board should be considered off."""
        if i<0 or j<0 or i>=self.size or j>=self.size:
            return False
        else:
            return self.array[i][j]


    def cell_next(self, i: int, j: int) -> bool:
        """Returns the state of the cell in the next time step given the
           cell's current state and the cells surrounding it."""
        return self.conway(self.get_cell(i,j), self.count_surrounding(i,j))


    def count_surrounding(self, i: int, j: int) -> int:
        """Counts the number of cells immediately surrounding the cell
          (row i, col j), but excluding the cell itself."""
        surrounding_cells = 0
        for ii in range(i-1, i+2):
            for jj in range(j-1, j+2):
                if not (ii==i and jj==j):
                    surrounding_cells += int(self.get_cell(ii,jj))
        return surrounding_cells


    def conway(self, cell_state: bool, surrounding_cells: int) -> bool:
        """The rules for Conway's Game of Life."""
        if cell_state and 1<surrounding_cells<4:
            return True
        elif (not cell_state) and surrounding_cells==3:
            return True
        else:
            return False


    def step(self) -> None:
        """Update every cell in the array with its new value."""
        new_array = [[self.cell_next(i,j) for j in range(self.size)] for i in range(self.size)]
        self.array = new_array


    def play(self, steps: int=0) -> None:
        """Go t"""
        sleep_time = 0.25
        if steps<=0:
            while True:
                print(self)
                sleep(sleep_time)
                self.step()
        else:
            while steps>=0:
                print(self)
                sleep(sleep_time)
                self.step()
                steps -= 1
                
        
            
                
def test():
    a = ConwayLifeBoard(10)
    #print(a)
    a.toggle(2,3)
    a.toggle(3,4)
    a.toggle(4,4)
    a.toggle(4,3)
    a.toggle(4,2)
    print(a)
    a.play(23)
    return a
    


if __name__=="__main__":
    a = test()
        
    
