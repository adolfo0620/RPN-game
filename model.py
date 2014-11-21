import random
import sqlite3

defaultdb = "rpngame.db"

class User:
	def __init__(self,name_given,user_id):
		self.name = name_given
		self.id = user_id
		# maybe score should be here

class DB:
	def __init__(self):
		self.db_name = defaultdb
	
	# please use number for pins
	def create_user(self,name,pin):
		
		conn = sqlite3.connect(self.db_name)
		c  = conn.cursor()
		
		if(isinstance( x, int ): 
			c.execute("INSERT INTO users VALUES (?,?)",(name,pin))
			conn.commit()
			c.close()
			return True
		else:
			conn.commit()
			c.close()
			return False 
	
	def update_user_stats(self):
		pass

	def fetch_user(self,name,pin):
		conn = sqlite3.connect(self.db_name)
		c = conn.cursor()
		# how to code in error checking
		c.execute("SELECT name,id FROM users WHERE user.pin=(?) and user.name=(?)",(name,pin))
		user_data = c.fetchall()[0]
		user = User(user_data[0],user_data[1])
		conn.commit()
		c.close()
		return user
	
	def save_turn(self,bool,time_take,difficulty_lvl):
		pass

class Turns:
	def __init__(self):
		self.start time = None
		self.end_time = None
		self.difficulty_lvl = 1
		self.correct_incorrect = None 
		self.time_taken = None
		self.rpn = RPN()

class RPN:
	def __init__(self):
		self.epression = ""
		self.answer_equation = ""
		self.user_answer = ""

    def chooseRandom(self,operatorLimit,numberLimit):
        Operators = ["+","-","*","/"]
        chosenOperator = Operators[random.randint(0,operatorLimit)]
        chosenFirstNumber = str(random.randint(1,numberLimit))
        chosenSecondNumber = str(random.randint(1,numberLimit))
        return chosenOperator, chosenFirstNumber, chosenSecondNumber

    # broken
    def answer_equation(self,equation):
        x = 0
        ops = ["+", "-", "*"] # "\", "mod"
        stack = []
        while x < len(equation):
            if not equation[x] in ops:
                stack.append(equation[x])
            else:
                y = stack.pop()
                stringy = stack.pop() + equation[x] + y
                stack.append(str(eval(stringy)))
            x += 1
        return (stack[0])


    def generate_equation(self,operatorLimit,numberLimit,lengthLimit):
        chosenLength = random.randint(1,lengthLimit)
        TestString = []
        length = 0

        while length < chosenLength:
            currentOperator, currentFirstNumber, currentSecondNumber = self.chooseRandom(operatorLimit,numberLimit)
            if length == 0:
                TestString.append(currentFirstNumber)
                TestString.append(currentSecondNumber)
                TestString.append(currentOperator)
            else:
                TestString.append(currentFirstNumber)
                TestString.append(currentOperator)
            length += 1
        return TestString

    def compare_user_answer(self,user_answer):
        pass

# test 
rpn = RPN()
eq = rpn.genater_equation(2,10,5)
print(eq)