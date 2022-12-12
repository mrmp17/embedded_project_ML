import cv2
import numpy as np

image0 = cv2.imread('/home/tjaz/final_ass/embedded_project_ML/Dataset/Testing/0/testing_1.jpg',0)
image1 = cv2.imread('/home/tjaz/final_ass/embedded_project_ML/Dataset/Testing/1/testing_1.jpg',0)
image2 = cv2.imread('/home/tjaz/final_ass/embedded_project_ML/Dataset/Testing/1/frame_1350.jpg',0)

image0 = image0/255
image1 = image1/255
image2 = image2/255


image_one_row1 = []

for i in range(20):
    for j in range(20):
        image_one_row1.append(image1[i][j])


image_one_row0 = []

for i in range(20):
    for j in range(20):
        image_one_row0.append(image0[i][j])

image_one_row2 = []

for i in range(20):
    for j in range(20):
        image_one_row2.append(image2[i][j])

file = open("test_img1.txt", 'w')
content = str(image_one_row1)
file.write(content)
file.close


file = open("test_img0.txt", 'w')
content = str(image_one_row0)
file.write(content)
file.close

file = open("test_img2.txt", 'w')
content = str(image_one_row2)
file.write(content)
file.close

