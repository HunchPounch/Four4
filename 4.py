import numpy as np
from PIL import Image, ImageEnhance
from random import randint

def File(filename1, filename2, filename3):

    try:
        image1 = Image.open(filename1)
        image2 = Image.open(filename2)
    except OSError:
        print("Failed\n")
        return 2
    
    image_array1 = np.array(image1)
    image_array2 = np.array(image2)

    testshape1 = image_array1.shape
    testshape2 = image_array2.shape
    
    if testshape1 != testshape2:
        print("ERRROR: different file sizes")
        return 1
    
    shape = image_array1.shape

    '''for i in range(276, 284):
        for j in range(235,241):
            
            image_array1[i][j][0] = 0
            image_array1[i][j][1] = 0
            image_array1[i][j][2] = 0'''
            
    '''for i in range(shape[0]):
        for j in range(shape[1]):
            image_array2[i][j][0] = randint(0, 1)
            image_array2[i][j][1] = randint(0, 1)
            image_array2[i][j][2] = randint(0, 1)'''

    for i in range(shape[0]):
        for j in range(shape[1]):
            if image_array2[i][j][0]==0 and image_array2[i][j][1]==0 and image_array2[i][j][2]==0:
                brightness = int(image_array1[i][j][0]) + int(image_array1[i][j][1]) + int(image_array1[i][j][2])
                image_array1[i][j][0] = brightness/3
                image_array1[i][j][1] = brightness/3
                image_array1[i][j][2] = brightness/3
                
                            

    pil_image = Image.fromarray(image_array1)
    pil_image.save(filename3)


namefile1 = input("Enter name of first file\n")
namefile2 = input("Enter name of second file\n")
namefile3 = input("Enter name of output file\n")
File(namefile1, namefile2, namefile3)
print("Processing completed\n")
