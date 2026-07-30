# Scenario 1: Student Result System

# Imagine creating a program for a school.

# You need to:
# Store student name, roll number
# Calculate average marks
# Decide grade based on marks
# Display results for multiple students


class Student:

    def __init__(self,name,roll_number):
        self.name = name
        self.roll_number = roll_number
       

#average logic - > Sum of all values/ number of all in short len
    def average_marks(self):

        Total_x = 0 #this will have total marks

        for x in self.Total_marks:
            Total_x += x;
            

        Total_y = 0 #this will have marks obtained in total

        for y in self.Marks_obtained:
            Total_y += y;

        #Now average and returning it
        average = (Total_y / Total_x)*100;

        return average

    def grade_assigning(self):

        avg = self.average_marks();

        if avg > 90:
            return "Grade A+ achived"

        elif 90 >= avg>= 80:
            return "Grade A achived"

        elif 80 > avg > 70:
            return "Grade B achived"  

        elif 70 > avg > 60:
            return "Grade C achived"

        elif 60 > avg > 50:
            return "Grade D achived"

        else:
            return "Fail"




S1 = Student("Ram",14,);

# Subjects and marks say:
S1.subjects = ["English","Math","Physics","Chemistry","Computer"]

#Total marks of each corresponding subjects
S1.Total_marks = [80,100,70,70,50]

#Obtained marks of each corresponding subjects by a student
S1.Marks_obtained= [50,65,40,42,30]


for items in S1.subjects:
    print(items)

print("Name :",S1.name,"\tRoll No:",S1.roll_number,"\t Average",S1.average_marks())
print("Status : ",S1.grade_assigning())

print("\n ........................................................")


S2 = Student("Anish",17);
S2.subjects = ["English","Math","Physics","Chemistry","Computer"]

#Total marks of each corresponding subjects
S2.Total_marks = [100,100,100,50,50]

#Obtained marks of each corresponding subjects by a student
S2.Marks_obtained= [92,90,80,40,42]


print("Name :",S2.name,"\tRoll No:",S2.roll_number,"\t Average",S2.average_marks())
print("Status : ",S2.grade_assigning())