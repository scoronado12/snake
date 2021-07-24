#!/usr/bin/python

import random


class Snake:
    def __init__(self):
        self.length = 1 
        self.points = 0

    def eat(self):
        self.length += 1
        self.points += 5

    def get_points(self):
        return self.points

    def get_length(self):
        return self.length
    
    def get_symbol(self):
        return 'S'


class Board:
    def __init__(self):
        #Board is 31x21
        self.board = [['_','_','_','_','_','_','_','_','_','_','_','_','_','_','_','_','_','_','_','_'],
                      ['_','_','_','_','_','_','_','_','_','_','_','_','_','_','_','_','_','_','_','_'],
                      ['_','_','_','_','_','_','_','_','_','_','_','_','_','_','_','_','_','_','_','_'],
                      ['_','_','_','_','_','_','_','_','_','_','_','_','_','_','_','_','_','_','_','_'],
                      ['_','_','_','_','_','_','_','_','_','_','_','_','_','_','_','_','_','_','_','_'],
                      ['_','_','_','_','_','_','_','_','_','_','_','_','_','_','_','_','_','_','_','_'],
                      ['_','_','_','_','_','_','_','_','_','_','_','_','_','_','_','_','_','_','_','_'],
                      ['_','_','_','_','_','_','_','_','_','_','_','_','_','_','_','_','_','_','_','_'],
                      ['_','_','_','_','_','_','_','_','_','_','_','_','_','_','_','_','_','_','_','_'],
                      ['_','_','_','_','_','_','_','_','_','_','_','_','_','_','_','_','_','_','_','_'],
                      ['_','_','_','_','_','_','_','_','_','_','_','_','_','_','_','_','_','_','_','_'],
                      ['_','_','_','_','_','_','_','_','_','_','_','_','_','_','_','_','_','_','_','_'],
                      ['_','_','_','_','_','_','_','_','_','_','_','_','_','_','_','_','_','_','_','_'],
                      ['_','_','_','_','_','_','_','_','_','_','_','_','_','_','_','_','_','_','_','_'],
                      ['_','_','_','_','_','_','_','_','_','_','_','_','_','_','_','_','_','_','_','_'],
                      ['_','_','_','_','_','_','_','_','_','_','_','_','_','_','_','_','_','_','_','_'],
                      ['_','_','_','_','_','_','_','_','_','_','_','_','_','_','_','_','_','_','_','_'],
                      ['_','_','_','_','_','_','_','_','_','_','_','_','_','_','_','_','_','_','_','_'],
                      ['_','_','_','_','_','_','_','_','_','_','_','_','_','_','_','_','_','_','_','_'],
                      ['_','_','_','_','_','_','_','_','_','_','_','_','_','_','_','_','_','_','_','_'],
                      ['_','_','_','_','_','_','_','_','_','_','_','_','_','_','_','_','_','_','_','_'],
                      ['_','_','_','_','_','_','_','_','_','_','_','_','_','_','_','_','_','_','_','_'],
                      ['_','_','_','_','_','_','_','_','_','_','_','_','_','_','_','_','_','_','_','_'],
                      ['_','_','_','_','_','_','_','_','_','_','_','_','_','_','_','_','_','_','_','_'],
                      ['_','_','_','_','_','_','_','_','_','_','_','_','_','_','_','_','_','_','_','_'],
                      ['_','_','_','_','_','_','_','_','_','_','_','_','_','_','_','_','_','_','_','_'],
                      ['_','_','_','_','_','_','_','_','_','_','_','_','_','_','_','_','_','_','_','_'],
                      ['_','_','_','_','_','_','_','_','_','_','_','_','_','_','_','_','_','_','_','_'],
                      ['_','_','_','_','_','_','_','_','_','_','_','_','_','_','_','_','_','_','_','_'],
                      ['_','_','_','_','_','_','_','_','_','_','_','_','_','_','_','_','_','_','_','_'],
                      ['_','_','_','_','_','_','_','_','_','_','_','_','_','_','_','_','_','_','_','_']]

        
    def gen_apple(self):
         self.board[random.randint(1,28)][random.randint(1,18)] = 'o'

    def gen_snake(self):
        self.snake_obj = Snake()
        self.board[10][15] = self.snake_obj.get_symbol()
    
    def show_board(self):
        print('\n'.join(' '.join(str(x) for x in row) for row in self.board))
    

    def get_snake_pos(self):
        for i in self.board()
        return (0,0)

def main():

    local_board = Board()
    local_board.gen_apple()
    local_board.gen_snake()
   
    while True:
        
        local_board.show_board()

        snake_dir = input("Direction? > ")
        if snake_dir == "left":
            print("Move Left")
        elif snake_dir == "right":
            print("Move Right")
        elif snake_dir == "up":
            print("Move Up")
        elif snake_dir == "down":
            print("Move Down")
        else:
            print("Invalid")




main()