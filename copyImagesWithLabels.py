import os
from shutil import copy

# Current working directory
cwd = os.getcwd()
print (cwd)

# Directory with images to copy
img_dir = "/media/ubuntu/Data/Dataset/COCO"

# Directory with labels (copy images here)
lbl_dir = "/media/ubuntu/Data/Dataset/COCOlables"

for iname in os.listdir(img_dir):
    imgName = iname.rsplit('.', 1)[0]
    for lname in os.listdir(lbl_dir):
        lblName = lname.rsplit('.', 1)[0]
        if (imgName == lblName):
            copy(os.path.join(img_dir,iname), lbl_dir)
            break

