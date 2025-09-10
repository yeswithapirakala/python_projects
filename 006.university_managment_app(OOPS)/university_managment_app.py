#university managment system


#person(name,age)- display_details)()
#student(person,age,rollno,branch) - display_details()
#teacher(person,age,emp_id,dept,salary) - display_details()
#university(uni_name,courses)- add_student(),add_emp(),courses(),tot_emp(),tot_student)

#creating person class
class Person:
  #constructor,initializing the variables
  #attributes of the class- name,age
  def __init__(self,name:str,age:int): #self keyword is used to access the variables
    self.name=name
    self.age=age

  # display_details() method is used to display the details of the person
  def display_details(self):
    pass

#creating student class
class Student(Person):
  #constructor,initializing the variables
  #attributes of the class-name,age,rollno,email,branch
  def __init__(self, name: str, age: int, rollno: int, branch: str, email: str = None):#email is optional so we use None
    super().__init__(name,age) #super keyword is used to access the variables of the parent class
    self.rollno=rollno
    self.email=email
    self.branch=branch

  # display_details() method is used to display the details of the student
  def display_details(self):
    #calling the display_details() method of the parent class
    super().display_details()
    pass


#creating employee class
class Employee(Person):
  #constructor,initializing the variables
  #attributes of the class-name,age,emp_id,dept,salary
  def __init__(self,name:str,age:int,emp_id:int,dept:str,salary:float):
    super().__init__(name,age)
    self.emp_id=emp_id
    self.dept=dept
    self.salary=salary

  def display_details(self):
    pass


#creating university class
class University:
  #constructor,initializing the variables
  #attributes of the class-uni_name,courses,students,teachers
  def __init__(self,uni_name:str,course:list[str]):
    self.uni_name=uni_name
    self.course=course
    self.students_table=dict()
    self.teachers_table=dict()

  #methods of the class university
  #method courses
  def courses(self):
    pass

  #method add_student
  def add_student(self,std_obj):#std_obj is the object of the student class
    if std_obj.rollno in self.students_table:
      #student does not exist
      return f"student {std_obj.name} already exists"
    else:
      #student already exists
      self.students_table[std_obj.rollno]=[std_obj.name,std_obj.age,std_obj.branch,std_obj.email]
      return f"successfully added student {std_obj.name}"



  #method add_emp
  def add_emp(self,emp_obj):#emp_obj is the object of the employee class
    if emp_obj.emp_id in self.teachers_table:
      #employee does not exist
      return f"employee {emp_obj.name} already exists"
    else:
      #employee already exists
      self.teachers_table[emp_obj.emp_id]=[emp_obj.name,emp_obj.age,emp_obj.dept,emp_obj.salary]
      return f"successfully added employee {emp_obj.name}"


  #method add_courses
  def add_courses(self,new_course:str): #new_course is the new course to be added
    if new_course in self.course:
      #course already exists
      return f"course {new_course} already exists"
    else:
      #course does not exist
      self.course.append(new_course)
      return f"successfully added course {new_course}"


  #method tot_student
  def tot_student(self):
    #printing the details of the students
    for item in self.students_table.items():
      print(item)


  #method tot_emp
  def tot_emp(self):
    #printing the details of the employees
    for item in self.teachers_table.items():
      print(item)


#main
if __name__ =="__main__":
  print("Welcome to Purple Dream University Managment System")
  #obj for uni
  uni=University("Purple Dream University",["CSE","ECE","MECH","CIVIL","EEE"])
  #creating objects of the classes student
  std1=Student("Abharam",20,1,"CSE")
  std2=Student("Sara",21,2,"ECE")
  #creating objects of the classes employee
  emp1=Employee("Kim",30,1,"CSE",500000)
  emp2=Employee("Jeon",31,2,"ECE",600000)
  #adding courses to the university
  print(uni.add_courses("IT"))

  #adding students to the university
  print(uni.add_student(std1))
  print(uni.add_student(std2))
  uni.tot_student()
  #adding employees to the university
  print(uni.add_emp(emp1))
  print(uni.add_emp(emp2))
  uni.tot_emp()




