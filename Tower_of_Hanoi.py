#Tower of Hanoi Problem 

#Define a stack class 
class Stack: 
	
	max_size = 1000
	
	def _init_(self):
		self.stack = []

	def set_max_stack_size(self,max_size):
		self.max_size = max_size

	def push(self,value):
		self.stack.insert(0,value)

	def pop(self):
		self.stack.pop(0)

	def is_empty(self):
		if(len(self.stack) == 0)
			return True
		else 
			return False 


first_stack = Stack()
second_stack = Stack()
third_stack = Stack()

first_stack.push(5)
first_stack.push(6)
first_stack.push(7)
print first_stack
first_stack.pop
print first_stack