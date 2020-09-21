import sqlite3
class Record:
	conn=""
	cur=""
	def __init__(self):
		try:
			self.conn=sqlite3.connect("emp.db")
		except:
			pass
		self.cur=self.conn.cursor()
		try:
			self.cur.execute("CREATE TABLE employee(id integer primary key autoincrement, fname text, lname text, email text, salary integer, department text)")
			self.conn.commit()
		except:
			pass

	def insert_record(self,fname,lname,email,salary,department):
		self.cur.execute("INSERT INTO employee (fname,lname,email,salary,department) VALUES (?,?,?,?,?)",(fname,lname,email,salary,department))
		self.conn.commit()
	def display_record(self):
		self.cur.execute("SELECT * FROM employee")
		record=self.cur.fetchall()
		for line in record:
			print(line)
	def displayEmployeeLastName(self,last):
		self.cur.execute("SELECT FROM employee WHERE lname=self.last")
		record=self.cur.fetchall()
		for line in record:
			print(line)
	def removeEmployeeFirstName(self,first):
		self.cur.execute("DELETE FROM emplyee WHERE first=self.first")
		self.conn.commit()
