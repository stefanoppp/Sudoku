import math

class Sudoku():
    def __init__(self, table1):
        self.table1 = table1
        self.largo = len(self.table1)
        self.zona = int(math.sqrt(self.largo))        
        self.no_delete = []
        self.state_values()
 
    def state_values(self):
        for i in range(len(self.table1)):
            for j in range(len(self.table1)):
                if (self.table1[i][j] != 0):
                    self.no_delete.append((i , j))

    def not_change(self, x, y):

        if (x, y) in self.no_delete:
            return False
        else:
            return True        

    def no_row_repeat(self, x, n):
        
        if (int(n) in self.table1[int(x)]):
            return False
        else:
            return True
            
    def no_column_repeat(self, y, n):
        
        for i in self.table1:
            if (i[int(y)] == int(n)):
                return False
            else:
                return  True

    def no_repeat_zona (self, x, y, n):

        
        if (int(x) < int(self.zona)):
            x = 0
        elif (x >= self.zona and x <= (self.zona * 2)):
            x = self.zona
        else:
            x = self.zona * 2

        for i in range(self.zona):
            for j in range(self.zona):
                if self.table1[x + i][x + j] == n:
                    return False
        return True

    def insert_num(self, x, y, n):

        if self.not_change(x, y) and self.no_row_repeat(x, n) and self.no_column_repeat(y, n) and self.no_repeat_zona(x, y, n):

            self.table1[int(x)][int(y)] = int(n)
            
            return True
        else:
            return False

    def win(self):

        for i in self.table1:
            
            if (0 in i):
                
                return False
        return True

    def getTable(self):
        self.print_table1 = ""
        for i in range(self.largo):
            if i == self.zona or i == self.zona*2:
                for n in range(self.largo):
                    self.print_table1 += "--"
                    if n == self.zona-1 or n == self.zona*2-1:
                        self.print_table1 += "+-"
                if n == self.zona-1 or n == self.zona*2-1:
                    self.print_table1 = self.print_table1[:-3]
                self.print_table1 += "\n"
            for j in range(self.largo):
                if j == self.zona or j == self.zona*2:
                    self.print_table1 += "| "
                self.print_table1 += str(self.table1[i][j]) + " "
            self.print_table1 += "\n"

        return self.print_table1
