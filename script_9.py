names=input("Enter names separated by commas:")
assignments = input("Enter assignment counts separated by commas:")
grades = input("Enter grades separated by commas:")

names_list = names.split(",")
assignments_list = assignments.split(",")
grades_list = grades.split(",")

message_format = "Hi {},\n\n\nThis is a reminder that you have {} assignments left to submit before you can graduate. Your" \
                 " current grade is {} and can increase to {} if you submit all assignments before the due date.\n"

for index in range(len(names_list)):
    print(message_format.format(names_list[index].title(), assignments_list[index], grades_list[index],
                               int(grades_list[index]) +  2*int(assignments_list[index])))