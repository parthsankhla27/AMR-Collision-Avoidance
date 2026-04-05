from PIL import Image, ImageDraw
import os
# this script helps visualize the bounding boxes from a sample labels file to its respective images file 
# to check if the labels were properly converted to correct YOLO format 

# path for a sample image and its label
image_path = r"C:/Users/parth/Desktop/Docs/GRAD DOCS/Spring 25/MMAE 500 Data Driven Modelling/Project/AMR_Collision_Project/datasets/cardboard_box/train/images/cardboard-216_jpg.rf.01b37382644d7555fadf0813029b2cf5.jpg"
label_path = r"C:/Users/parth/Desktop/Docs/GRAD DOCS/Spring 25/MMAE 500 Data Driven Modelling/Project/AMR_Collision_Project/datasets/cardboard_box/train/labels/cardboard-216_jpg.rf.01b37382644d7555fadf0813029b2cf5.jpg"

# Open image
img = Image.open(image_path)
w, h = img.size

# Draw bounding boxes
draw = ImageDraw.Draw(img)
with open(label_path, 'r') as f:
    for line in f:
        parts = list(map(float, line.strip().split()))
        cls, x, y, bw, bh = parts
        xmin = (x - bw/2) * w
        ymin = (y - bh/2) * h
        xmax = (x + bw/2) * w
        ymax = (y + bh/2) * h
        draw.rectangle([xmin, ymin, xmax, ymax], outline="red", width=2)

img.show()
