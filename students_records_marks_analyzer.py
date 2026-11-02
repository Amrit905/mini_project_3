#   student work and marks analyzer
#define subject
subjects = ("python","Maths","Dbms") 
print("STUDENT RECORDS AAND MARKS ANALYZER")
print("subjects:",subjects)
 
print("first subjects",subjects[0])
print("second subjects",subjects[1])
print("third subjects",subjects[2])
#tuple unpacking

subject1, subject2,subject3=subjects

print(subject1)
print(subject2)
print(subject3)
#add student record
students={}
n=int(input("how many students?"))
for i in range(n):
    student_id =input("enter student id:")
    while student_id in students:
        print("student id already exist!")
        student_id=input("enter other student id:")
    name=input("enter name:")
    marks=[]
    for subject in subjects:
        mark=int(input("enter"+subject+"marks:"))
        while mark<0 or mark>100:
            print("invalid marks!enter marks betweeb 0 and 100.")
            mark=int(input("enter"+subject+"marks:"))
        marks.append(mark)
        students[student_id]={
            "name":name,
            "marks":marks
        }
print("student records added successfully!")
      