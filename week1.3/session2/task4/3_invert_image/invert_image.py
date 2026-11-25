# Week 1.3, Session 2: Invert PGM image
# Open a pgm image file to read
# You can use the relative path ../images/filename
# You could handle file errors with try/except

# Create inverted image
# the formula: invert_pixel_value = max_gray - original_pixel_value
image = str(input("enter file name"))

# processing and storing width, height, max values
info = []
with open(image,"r") as x:
    info.append(x.readline().strip().split())
    info.append(x.readline().strip().split())
    info.append(x.readline().strip().split())

width = int(info[1][0])
height = int(info[1][1])
max_grey=int(info[2][0])
print(f"{width}x{height}, {max_grey}\n")

with open(image, "r") as x:
    pgm_img=x.read()

# processing the pgm_img into a list

pgm_img=[line.split(",") for line in pgm_img.strip().split("\n")]
pgm_img.remove(pgm_img[0])
pgm_img.remove(pgm_img[0])
pgm_img.remove(pgm_img[0])
pgm_img = [line[0].split() for line in pgm_img]

pgm_img = [int(pgm_img[j][k]) for j in range(len(pgm_img)) for k in range(len(pgm_img[j]))]
pgm_img = [str(max_grey - pixel) for pixel in pgm_img]

nested = [pgm_img[i:i+width] for i in range(0, len(pgm_img), width)]
nested.insert(0, [str(max_grey)])
nested.insert(0,[str(width), str(height)])
nested.insert(0,["P2"])

with open("inverted_img","w") as x:
    for line in nested:
        delimiter = " "
        join_str = delimiter.join(line)
        x.write(join_str + "\n")

with open("inverted_img","r") as x:
    final_file = x.read()

print(final_file)


# write the inverted pgm image to a new file.
# Remember to include:
# - the string `P2`
# - the width and height dimensions
# - maximum gray value
# - you could convert numbers in a list to strings and join them with spaces
#   for example line = [255, 255, 0, 255, 255]
#   string_line = " ".join(str(item) for item in line)
#   # output: string_line = "255 255 0 255 255"


# /workspaces/semester-1/week1.3/session2/task4/images/gradient.pgm