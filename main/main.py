import tkinter as tk
import random

class Simulation():
    def __init__(self, root= None):
        
        #二次元配列の初期化
        self.Bp = [[0 for j in range(50)] for i in range(50)]

        self.beta = 1/2
 
        #窓        
        self.root = root
        self.root.title("感染のシミュレーション")
        self.root.geometry("500x500")
        self.root.resizable(width=False, height=False)

        #画用紙
        self.canvas = tk.Canvas(self.root, width = 500, height = 500, background='black')
        self.canvas.place(x=-2, y=-2)
        self.canvas.propagate(0)
         
        for i in range(0, 50):
            for j in range(0, 50):
                self.Bp[i][j] = self.canvas.create_rectangle(i * 10, j * 10, (i + 1) * 10, (j + 1) * 10, fill="blue", width=1, tags= "P(" + str(i) + ", " + str(j) + ")")
       

        self.canvas.itemconfig("P(10, 10)", fg="black")

    def MOVE(self):
        for i in range(0, 50):
            for j in range(0, 50):
                if self.Bp[i + 1][j + 1] == 1 or self.Bp[i + 1][j - 1]
         
        self.root.after(100, self.MOVE) #自分を実行
   
                          



def Main():

    win = tk.Tk()
    Simulation(root = win)
    win.mainloop()       

if __name__ == '__main__':
    Main()

#https://teratail.com/questions/172973

#https://daeudaeu.com/tkinter_canvas_method/#itemconfig

#https://techacademy.jp/magazine/33531
