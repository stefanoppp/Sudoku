from sudoku import Sudoku

class Interfaz():

    def ask_largo(self):
        self.largo = 0
        self.table1 =  ([[5,3,0,0,7,0,0,0,0],
                          [6,0,0,1,9,5,0,0,0],
                          [0,9,8,0,0,0,0,6,0],
                          [8,0,0,0,6,0,0,0,3],
                          [4,0,0,8,0,3,0,0,1],
                          [7,0,0,0,2,0,0,0,6],
                          [0,6,0,0,0,0,2,8,0],
                          [0,0,0,4,1,9,0,0,5],
                          [0,0,0,0,8,0,0,7,9]])
        self.game = Sudoku(self.table1)

    def enter_number(self, x, y, n):
        try:
            if int(x) > self.largo:
                return False
            elif int(y) > self.largo:
                return False
            elif n != 0:
                if int(n) > 0 and int(n) < self.largo+1:
                    return  True
            else:
                return True
        except Exception:
            return False

    def ask_values(self):
        self.n = input("Escriba el numero que desea agregar: ")
        self.x = input("Escriba el numero de fila deseada: ")
        self.y = input("Escriba el numero de columna deseada: ")
        print()

    def play(self):
        self.ask_largo()
        print()
        while not self.game.win():
            print(self.game.getTable())
            self.ask_values()
            if self.enter_number(self.n , self.x , self.y):
                print(self.game.insert_num(int(self.n) , int(self.x)-1 , int(self.y)-1))
            else:
                print("Ingrese un numero del 1 al 9")
        print("\n FIN")

if __name__ == "__main__":
    game = Interfaz()
    game.play()    


