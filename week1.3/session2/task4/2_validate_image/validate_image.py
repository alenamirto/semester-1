# Week 1.3, Session 2: Validate image

# Open a pgm image
# You could handle file errors with try/except

# Read the file content

# Store the width, the height, and the maximum gray value

# For each pixel, check if the pixel value is between 0 and the maximum gray value inclusive

# Check if the widths and heights are the same as specified

# 4. Print the final verdit.
#  Print `Valid image` if the widths, the heights are the same, and all pixel values between 0 and the maximum gray value inclusive
#  Print `Invalid width` if the widths are different
#  Print `Invalid height` if the heights are different
#  Print `Invalid pixel values` if any pixel values is less than 0 and greater than the maximum gray value

###################################################

image = str(input("enter file name"))

# processing and storing width, height, max values
info = []
with open(image,"r") as x:
    info.append(x.readline().strip().split())
    info.append(x.readline().strip().split())
    info.append(x.readline().strip().split())

print(info)
width = int(info[1][0])
height = int(info[1][1])
max_grey=int(info[2][0])
print(f"{width}x{height}, {max_grey}\n")

# processing the pgm_img into a list
with open(image, "r") as x:
    pgm_img=x.read()

pgm_img=[line.split(",") for line in pgm_img.strip().split("\n")]
pgm_img.remove(pgm_img[0])
pgm_img.remove(pgm_img[0])
pgm_img.remove(pgm_img[0])
pgm_img = [line[0].split() for line in pgm_img]

# validation
correct_height = False
correct_width = True
correct_max = True

if height == len(pgm_img):
    correct_height = True

for line in pgm_img:
    pgm_img_width = len(line)
    if pgm_img_width == width:
        correct_width = True
    else:
        correct_width = False
        break

print(pgm_img)

for line in pgm_img:
    for pixel in line:
        if int(pixel) < 0 or int(pixel) > max_grey:
            correct_max = False
            break

print(f"height={correct_height}, width={correct_width}, max={correct_max}")

# /workspaces/semester-1/week1.3/session2/task4/images/gradient.pgm
