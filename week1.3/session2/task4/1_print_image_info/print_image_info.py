# Week 1.3, Session 2: Print PGM image info
# /workspaces/semester-1/week1.3/session2/task4/images/gradient.pgm
# Open a pgm image file
# You can use the relative path ../images/filename
# You could handle file errors with try/except.
image = str(input("enter file name"))
info=[]
with open(image,"r") as x:
    info.append(x.readline().strip().split(" "))
    info.append(x.readline().strip().split(" "))
    info.append(x.readline().strip().split(" "))

print(f"\nimage dimensions are {info[1][0]}x{info[1][1]}")
print(f"max gray value is {info[2][0]}")
# Read the file content

# print image dimension (i.e., Dimensions: width x height pixels)

# print max gray value (i.e., Max Gray Value: max_gray_value)