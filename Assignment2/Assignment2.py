class Tasbih:
	def __init__(self):
		self.count = 0
	def add(self):
		self.count+1
	def reset(self):
		self.count = 0


class Number:
	def Largest(self,a,b):
		return a if a > b else b
	def Smallest(self,a,b):
		return a if a < b else b


class Calculator:
	def __inti__(self):
		self.ops = {'+':self.add,'-':self.sub,'/':self.div,'*':self.mul}
	def add(self,op1,op2):
		return op1+op2
	def sub(self,op1,op2):
		return op1-op2
	def div(self,op1,op2):
		return op1//op2
	def mul(self,op1,op2):
		return op1*op2
	def notFound(self,*args):
		return None
	def inp(self,op,op1,op2):
		return self.ops.get(op,self.notFound)(op1,op2)

class ReverseList:
	def rev(self,List):
		List.reverse()


class ListClass:
	def inList(self,elem, List):
		return elem in List
	def odd(self,List):
		return [num for num in List if num%2]

	def total(self,List):
		return sum(List)

class Robot:
	counter = 0
	def __init__(self):
		Robot.counter+=1
		print("Robot Created")
	def destroy(self):
		Robot.counter-=1
		print("Robot Destroyed")