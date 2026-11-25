# Week 1.3, Session 2: Calculate Average Grade and Write to a File

# Open 'student_data.csv' to read each student's grades
# hint: skip the header row with data[1:]
data=[]
grade_data = []
with open("/workspaces/semester-1/week1.3/session2/task3/2_average_grade/student_data.csv","r") as x:
    data = x.read()

new_data = [line.split(",") for line in data.strip().split("\n")]
new_data.remove(new_data[0])

for line in new_data:
    a=int(line[2])
    b=int(line[3])
    c=int(line[4])
    grade_data.append(round(((a+b+c)/3),2))

print(grade_data)

refined_list = [[new_data[i][0],new_data[i][1],grade_data[i]] for i in range(0,len(new_data))]
for line in refined_list:
    print(f"{line[1]} with id {line[0]} has an avg grade {line[2]} in maths, science, and history,")

# Read each student's grades and calculate their average grade
# hint: CSV data comes as strings, convert grade columns to int() for maths
# hint: student_data.csv has columns: ID, Name, Mathematics, Science, History
# hint: average = (maths + science + history) / 3


# Open a file called 'report.txt'
# Write each student's name and their average grade to the report
# hint: use 'w' mode to create a fresh report each time
# hint: format averages nicely, maybe to 2 decimal places with :.2f
