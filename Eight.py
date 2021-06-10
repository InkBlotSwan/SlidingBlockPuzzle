# File Eight.py

from queue import *
import random

# Board class, contains all board functionality
class Board(object):
	def __init__(self, state = ["1","2","3","4","5","6","7","8"," "], desired = ["1","2","3","4","5","6","7","8"," "]):
		self.state = state
		self.desired = desired
	
	# Prints out the board, needs to be used after every move
	def print_board(self):
		print_storage = []
		for i in self.state:
			print_storage.append(i)
		print("|%s|%s|%s|\n|%s|%s|%s|\n|%s|%s|%s|\n\n\n" %(print_storage[0], print_storage[1], print_storage[2], print_storage[3], print_storage[4], print_storage[5], print_storage[6], print_storage[7], print_storage[8]))

	# Movement functions, moves the blank space in the direction specified
	def move_up(self):
		try:
			new_state = self.state
			index = new_state.index(" ")
			temp = new_state[index - 3]
			new_state[index - 3] = new_state[index]
			new_state[index] = temp
			return new_state
		except IndexError:
			pass
	def move_down(self):
		try:
			new_state = self.state
			index = new_state.index(" ")
			temp = new_state[index + 3]
			new_state[index + 3] = new_state[index]
			new_state[index] = temp
			return new_state
		except IndexError:
			pass
	def move_left(self):
		try:
			new_state = self.state
			index = new_state.index(" ")
			temp = new_state[index - 1]
			new_state[index - 1] = new_state[index]
			new_state[index] = temp
			return new_state
		except IndexError:
			pass
	def move_right(self):
		try:
			new_state = self.state
			index = new_state.index(" ")
			temp = new_state[index + 1]
			new_state[index + 1] = new_state[index]
			new_state[index] = temp
			return new_state
		except IndexError:
			pass

	# Shuffles the board, allowing the user to start solving
	def shuffle(self):
		for i in range(random.randint(10,25)):
			x = random.randint(1,4)
			if x == 1:
				self.move_up()
			if x == 2:
				self.move_down()
			if x == 3:
				self.move_left()
			if x == 4:
				self.move_right()
	
	def hueristic_calc(self,state):
		cost = 0
		for i in range(len(self.state)):
			if state[i] != self.desired[i]:
				cost += 1
		return cost
	
	def next_to(self, current):
		neighbours = []
		current = list(current.queue)
		neighbours.append(current.move_down())
		neighbours.append(current.move_up())
		neighbours.append(current.move_left())
		neighbours.append(current.move_right())
		return neighbours
	# Solves the puzzle
	def a_star(self):
		start = PriorityQueue()
		for i in self.state:
			start.put(self.state)
		poss_states = PriorityQueue(maxsize = 0)
		poss_states.put(start, 0)
		visited = {}
		cost_so_far = {}
		visited[start] = None
		cost_so_far[start] = 0
		while not poss_states.empty():
			current = poss_states.get()
			
			if current == self.desired:
				break
			for next in self.next_to(current):
				new_cost = cost_so_far[current] + self.hueristic_calc(current, next)
				if next not in cost_so_far or new_cost < cost_so_far[next]:
					cost_so_far[next] = new_cost
					priority = new_cost + hueristic_calc(desired, next)
					poss_states.put(next, priority)
					visited[next] = current
# Active code, draws on board class
puzzle8 = Board()

while True:
	puzzle8.print_board()
	key = input("a:move left\nd:move right\nw:move up\ns:move down\n\nalso type 'a*' for sort, and 'shuffle' to reset")
	if key == "a":
		puzzle8.state = puzzle8.move_left()
	elif key == "d":
		puzzle8.state = puzzle8.move_right()
	elif key == "s":
		puzzle8.state = puzzle8.move_down()
	elif key == "w":
		puzzle8.state = puzzle8.move_up()
	elif key == "a*":
		puzzle8.a_star()
	elif key == "shuffle":
		puzzle8.shuffle()
	else:
		print("quitting...")
		break