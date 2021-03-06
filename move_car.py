# Descriptive Header

#Global variables defined out of class
directions = ['N','E','S','W'] 
movement = {'N': (0,1), 'E': (1,0), 'S': (0,-1), 'W':(-1,0)}
commands = {'L': 'turn_left', 'R': 'turn_right', 'M': 'move'}


# List comprehensions seem to be recomended in these situations
GRID_MAX_X, GRID_MAX_Y = map(int, raw_input().split())


# Different structure for multiple vehicles...
first_vehicle_x = None
first_vehicle_y = None

class Vehicle():
    def __init__(self, x, y, face):
        self.x = x
        self.y = y
        self.dir = face

        #naming dir might not be a good name...
    def turn_left(self):
        self.dir = directions[(directions.index(self.dir)-1)%len(directions)]

    def turn_right(self):
        self.dir = directions[(directions.index(self.dir)+1)%len(directions)]

    def move(self): #does not handle linear movement?
        new_x = self.x + movement[self.dir][0]
        new_y = self.y + movement[self.dir][1]

        #below not needed...
        if new_x != first_vehicle_x or new_y != first_vehicle_y:
            if new_x in xrange(GRID_MAX_X+1):
                self.x = new_x
            if new_y in xrange(GRID_MAX_Y+1):
                self.y = new_y

vehicle_one_pos = raw_input().split()
vehicle_one_commands = raw_input()

vehicle_one = Vehicle(int(vehicle_one_pos[0]), int(vehicle_one_pos[1]), vehicle_one_pos[2])
for command in vehicle_one_commands:
    # Maybe better to have function here, not eval class
    eval("vehicle_one.{0}()".format(commands[command]))

first_vehicle_x = vehicle_one.x
first_vehicle_y = vehicle_one.y

'''
User interface might benefit from more refined prompting
Not everyone is going to remember the readme 
and some examples may be useful...
'''



vehicle_two_pos = raw_input().split()
vehicle_two_commands = raw_input()

# typo - pos
vehicle_two = Vehicle(int(vehicle_two_pos[0]), int(vehicle_two_pos[1]), vehicle_two_ps[2])
for command in vehicle_two_commands:
    eval("vehicle_two.{0}()".format(commands[command]))

print vehicle_one.x, vehicle_one.y, vehicle_one.dir
print vehicle_two.x, vehicle_two.y, vehicle_two.dir
