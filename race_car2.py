'''
Interactive terminal game to race cars to find a jackpot

User enters grid and car information, 
the program creates a random jackpot,
then determines if the cars will make it to 
the jackpot

Written on 2/23/2017 by Denis Willett
for Python 3
'''

from random import randint

def move_vehicle(position, direction, gridx, gridy, jackpot):
	MOVEMENT = {'N': (0, 1), 'E': (1, 0), 'S': (0, -1), 'W':(-1, 0)}

	if position == jackpot:
		return(True)

	else:
		position[0] += MOVEMENT[direction][0]
		position[1] += MOVEMENT[direction][1]

		if position[0] > gridx or position[1] > gridy:
			return(False)

		# Keep moving vehicle until jackpot or hits boundary
		move_vehicle(position, direction, gridx, gridy, jackpot)


def pot_of_gold(x, y):
	goldx = randint(0, x)
	goldy = randint(0, y)
	return( (goldx, goldy) )



def main():
	print('Please enter size of grid separated by spaces')
	print('For example: 8 8')
	gridx, gridy = [int(x) for x in input().split()]

	jackpot = pot_of_gold(gridx, gridy)
	print(jackpot)

	print('Thanks!')
	print('Now please enter the grid position for Car 1 as above.')
	print('For example: 2 2')
	car1x, car1y = [int(x) for x in input().split()]

	print('Awesome!')
	print('Now please enter the grid position for Car 2 as above.')
	print('For example: 2 2')
	car2x, car2y = [int(x) for x in input().split()]


	print('Cool!')
	print('Mhich direction should Car 1 move?')
	print('Either N S E W')
	dir1 = input()

	print('Last question...')
	print('Which direction should Car 2 move?')
	print('Either N S E W')
	dir2 = input()	

	print('Thanks!')

	

	Car1 = move_vehicle((car1x, car1y), dir1, gridx, gridy, jackpot)
	Car2 = move_vehicle((car1x, car1y), dir1, gridx, gridy, jackpot)
	if Car1:
		print('Car1 hit the jackpot!')
	if Car2:
		print('Car2 hit the jackpot!')

if __name__ == '__main__':
	main()