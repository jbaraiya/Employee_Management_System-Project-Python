import re
class Varification:
	def varifyEmail(self):
		pattern=re.compile(r'[a-z0-9]+@(yahoo|gmail)\.com')
		while 1:
			e=input("Enter email: ")
			if pattern.match(e):
				return e
			else:
				print("Invalid Email")