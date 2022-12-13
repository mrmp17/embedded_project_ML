import cv2
import numpy as np

test_images = open("test_images.h","w").close()
test_images = open("test_images.h","w")

test_images.write("float images_array[20][400] = {")

for i in range(1,21):
    i_str = str(i)
    file_name = "/home/tjaz/final_ass/embedded_project_ML/Testing_hls/image" + i_str +".jpg"
    image = cv2.imread(file_name,0)
    
    image = image/255
    image = image.flatten()


    test_images.write("{")

    for j in range(399):
        test_images.write(str(image[j]) + ", ")

    test_images.write(str(image[399]))


    if (i  <20):
        test_images.write("},\t")


    
test_images.write("}};")

    


   




   









image0 = cv2.imread('/home/tjaz/final_ass/embedded_project_ML/Dataset/Testing/0/testing_1.jpg',0)
image1 = cv2.imread('/home/tjaz/final_ass/embedded_project_ML/Dataset/Testing/1/testing_1.jpg',0)
image2 = cv2.imread('/home/tjaz/final_ass/embedded_project_ML/Dataset/Testing/1/frame_1350.jpg',0)

image0 = image0/255
image1 = image1/255
image2 = image2/255


image_one_row1 = []



file = open("test_img1.txt", 'w')
content = str(image_one_row1)
file.write(content)
file.close


