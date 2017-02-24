'''
Module to race cars on a grid to a random point
-----------------------------------------------

Use: http://codereview.stackexchange.com/questions/155913/create-two-vehicles-move-them-on-a-grid-based-on-user-input
as inspiration with adjustments made by Denis Willett on 2/23/2017

Written in Python 3
'''

class Directions:
    """Circular buffer of possible directions"""
    DIRECTIONS = 'NESW'

    def __init__(self, start):
        self.index = self.DIRECTIONS.index(start)

    def next(self):
        self.index = (self.index + 1) % len(self.DIRECTIONS)

    def previous(self):
        self.index = (self.index - 1) % len(self.DIRECTIONS)

    @property
    def current(self):
        return(self.DIRECTIONS[self.index])


class Vehicle():
    MOVEMENT = {'N': (0, 1), 'E': (1, 0), 'S': (0, -1), 'W':(-1, 0)}

    def __init__(self, x, y, facing, grid, obstacle):
        self.x = x
        self.y = y
        self.facing = Directions(facing)
        self.grid_width, self.grid_height = grid
        self.obstacle = obstacle

    @property
    def direction(self):
        return(self.facing.current)

    @property
    def position(self): 
        return( (self.x, self.y) )

    def parse_commands(self, commands):
        action = {
            'L': self.facing.previous,
            'R': self.facing.next,
            'M': self.move,
        }
        for command in commands:
            action[command]()

    def move(self):
        offset_x, offset_y = self.MOVEMENT[self.facing.current]
        x = self.x + offset_x
        y = self.y + offset_y

        if (x, y) != self.obstacle and 0 <= x <= self.grid_width and 0 <= y <= self.grid_height:
            self.x = x
            self.y = y


def setup_and_move_vehicule(grid, obstacle):
    x, y, facing = input().split()
    vehicule = Vehicule(int(x), int(y), facing, grid, obstacle)
    vehicule.parse_commands(input().strip())
    return(vehicule.position, vehicule.direction)


def main():
    grid = map(int, input().split())
    v1_pos, v1_dir = setup_and_move_vehicule(grid, None)
    v2_pos, v2_dir = setup_and_move_vehicule(grid, v1_pos)
    print(v1_pos[0], v1_pos[1], v1_dir)
    print(v2_pos[0], v2_pos[1], v2_dir)


if __name__ == '__main__':
    main()