import varifyEmployee as ve
from database import Record
class Employee:
	_employeeDepartment="CE"
	_employeeFirstName=""
	_employeeLastName=""
	_employeeSalary=0
	_employeeEmail=""
	def __init__(self):
		e=ve.Varification()
		_employeeFirstName=input("Enter first name: ")
		_employeeLastName=input("Enter last name: ")
		_employeeSalary=int(input("Enter salary: "))
		_employeeEmail=e.varifyEmail()
		_employeeDepartment=input("Enter dapartment: ")
	@classmethod
	def insert_department(cls,dept):
		cls._employeeDepartment=dept
		print("New Department: "+cls._employeeDepartment)

print("1.Add Employee")
print("2.Display All Employee")
print("3.Add Department")
print("4.Display Employee as Last Name")
print("5.Remove Employee")
ch=int(input("Enter your choice: "))
if ch==1:
	e=Employee()
	r=Record()
	r.insert_record(e._employeeFirstName,e._employeeLastName,e._employeeEmail,e._employeeSalary,e._employeeDepartment)
elif ch==2:
	r=Record()
	r.display_record()
elif ch==3:
	dept=input("Enter Department: ")
	Employee.insert_record(dept)
elif ch==4:
	last=input("Enter Last Name: ")
	e.displayEmployeeLastName(last)
elif ch==5:
	first=input("Enter First Name: ")
	e.removeEmployeeFirstName(first)