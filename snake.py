#!/usr/bin/python

import random
import enum

class Direction(enum.Enum):
        LEFT = 0
        RIGHT = 1
        UP = 2
        DOWN = 3


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
        for i in range(len(self.board)):
            for j in range(len(self.board[i])):
                if self.board[i][j] == 'S':
                    return (i, j)

    def get_apple_pos(self):
        for i in range(len(self.board)):
            for j in range(len(self.board[i])):
                if self.board[i][j] == 'o':
                    return (i, j)

    def set_snake_pos(self, row, col):
        pos = self.get_snake_pos()
        self.board[pos[0]][pos[1]] = '_'
        self.board[row][col] = 'S'


    def move_snake(self, direction):
        pos = self.get_snake_pos()

        if direction == Direction.UP:
            self.set_snake_pos(pos[0]-1,pos[1])
        elif direction == Direction.DOWN:
            self.set_snake_pos(pos[0]+1,pos[1])
        elif direction == Direction.RIGHT:
            self.set_snake_pos(pos[0],pos[1]+1)
        elif direction == Direction.LEFT:
            self.set_snake_pos(pos[0],pos[1]-1)

    def check_apple(self):
        if self.get_apple_pos() is None:
            self.snake_obj.eat() 
    
    def get_snake(self):
        return self.snake_obj
                

def main():

    local_board = Board()
    local_board.gen_apple()
    local_board.gen_snake()
    

    while True:
        
        local_board.show_board()

        snake_dir = input("Direction? > ")
        if snake_dir == "left" or snake_dir == 'a':
            print("Move Left")
            local_board.move_snake(Direction.LEFT)
        elif snake_dir == "right" or snake_dir == 'd':
            print("Move Right")
            local_board.move_snake(Direction.RIGHT)
        elif snake_dir == "up" or snake_dir == 'w': 
            print("Move Up")
            local_board.move_snake(Direction.UP)
        elif snake_dir == "down" or snake_dir == 's':
            print("Move Down")
            local_board.move_snake(Direction.DOWN)
        elif snake_dir == "exit":
            print("Done")
            exit(0)
        else:
            print("Invalid")
        
        print("Snake @ " + str(local_board.get_snake_pos()))
        print("Apple @ " + str(local_board.get_apple_pos()))
        print("Score @ " + str(local_board.snake_obj.get_points())) 
        local_board.check_apple()

main()
