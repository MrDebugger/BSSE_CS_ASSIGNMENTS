# TASK 1
class TwoStacks: 
	def __init__(self, n):	 
		self.size = n 
		self.arr = [None] * n 
		self.top1 = -1
		self.top2 = self.size 
	def push1(self, x): 
		if self.top1 < self.top2 - 1 : 
			self.top1 = self.top1 + 1
			self.arr[self.top1] = x 
	def push2(self, x): 
		if self.top1 < self.top2 - 1: 
			self.top2 = self.top2 - 1
			self.arr[self.top2] = x 
	def pop1(self): 
		if self.top1 >= 0: 
			x = self.arr[self.top1] 
			self.top1 = self.top1 -1
			return x 
	def pop2(self): 
		if self.top2 < self.size: 
			x = self.arr[self.top2] 
			self.top2 = self.top2 + 1
			return x 

ts = TwoStacks(5) 
ts.push1(5) 
print("Pushed 5 to Stack 1")
ts.push2(10) 
print("Pushed 10 to Stack 2")
ts.push2(15) 
print("Pushed 15 to Stack ")
ts.push1(11) 
print("Pushed 11 to Stack 1")
ts.push2(7) 
print("Pushed 7 to Stack 2")

print("Popped element from stack1 is " + str(ts.pop1())) 
ts.push2(40) 
print("Pushed 40 to Stacks")
print("Popped element from stack2 is " + str(ts.pop2())) 
"""

# Task 2
class Queue: 
	def __init__(self): 
		self.s1 = [] 

	def enQueue(self, x): 
		self.s1.append(x) 

	def deQueue(self): 
		if len(self.s1) == 0: 
			print("Q is Empty") 
		return self.s1.pop(0) 

q = Queue() 
print("EnQueue 1:",q.enQueue(1)) 
print("EnQueue 2:",q.enQueue(2)) 
print("EnQueue 3:",q.enQueue(3)) 
print("DeQueue:",q.deQueue()) 
print("DeQueue:",q.deQueue()) 
print("DeQueue:",q.deQueue()) 

# Task 3
def printDiagnol(lst): 
	print('Diagnol Forward ', end ="") 
	print([lst[i][i] for i in range(len(lst))]) 
	print('Diagnol Backward ', end ="") 
	print([lst[i][len(lst)-i-1] for i in range(len(lst))]) 
	
lst = [
		[1, 2, 3], 
		[4, 5, 6], 
		[7, 8, 9]
	] 
print("List",lst)
printDiagnol(lst) 

# Task 4
class Queue: 
	def __init__(self): 
		self.s1 = [] 
		self.s2 = [] 
	def enQueue(self, x): 
		while len(self.s1) != 0: 
			self.s2.append(self.s1[-1]) 
			self.s1.pop() 
		self.s1.append(x) 
		while len(self.s2) != 0: 
			self.s1.append(self.s2[-1]) 
			self.s2.pop() 
	def deQueue(self): 
		if len(self.s1) == 0: 
			print("Q is Empty") 
		x = self.s1[-1] 
		self.s1.pop() 
		return x 

q = Queue() 
print("EnQueue 1:",q.enQueue(1))
print("EnQueue 2:",q.enQueue(2)) 
print("EnQueue 3:",q.enQueue(3))
print("DeQueue:",q.deQueue()) 
print("DeQueue:",q.deQueue()) 
print("DeQueue:",q.deQueue()) 



# Task 5
from queue import Queue 
class Stack: 
	def __init__(self): 
		self.q1 = Queue() 
		self.q2 = Queue() 
		self.curr_size = 0
	def push(self, x): 
		self.curr_size += 1
		self.q2.put(x) 
		while (not self.q1.empty()): 
			self.q2.put(self.q1.queue[0]) 
			self.q1.get() 
		self.q = self.q1 
		self.q1 = self.q2 
		self.q2 = self.q 
	def pop(self): 
		if (self.q1.empty()): 
			return
		self.q1.get() 
		self.curr_size -= 1
	def top(self): 
		if (self.q1.empty()): 
			return -1
		return self.q1.queue[0] 
	def size(self): 
		return self.curr_size 

s = Stack() 
s.push(1) 
s.push(2) 
s.push(3) 

print("current size of Stack: ", s.size()) 
print('Top Value:',s.top()) 
print('Pop Value',s.pop()) 
print('Top Value:',s.top()) 
print('Pop Value',s.pop()) 
print('Top Value:',s.top()) 

print("current size of Stack: ", s.size()) 

"""