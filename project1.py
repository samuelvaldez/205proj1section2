#Lets see if this shows up in our github

import PIL
from PIL import Image  #using pilow for images
import statistics



#im = Image.open("1.png")
imageList = []
redPixelList =[]
bluePixelList = []
greenPixelList =[]


picWidth = 495
picHeight = 557 #double check these.

newImage = Image.new("RGB", (picWidth,picHeight))#creates a new image for we can work with with mode type RGB


for i in range(1,10):
    #print (i)
    imageList.append(Image.open("Project1Images/" + str(i)+ ".png"))
    
    

    

for x in range(0, picWidth):#starts from the top to the bottom of image
    for y in range(0, picHeight):
        for myImg in imageList:
            myRed, myBlue, myGreen = myImg.getpixel((x,y))
            
            redPixelList.append(myRed)
            bluePixelList.append(myBlue)
            greenPixelList.append(myGreen)#adds  rgb pixels in respected list
         
        
        reconstructedR = statistics.median(redPixelList)   #grabs all of pixels of each index, finds the size of list then divides by 2
        reconstructedB = statistics.median(bluePixelList)   
        reconstructedG = statistics.median(greenPixelList) 
        
        newImage.putpixel((x,y), (reconstructedR,reconstructedG,reconstructedB))# adds pixel to image with start possition at 0,0

        
        

        
        del redPixelList[:]
        del greenPixelList[:]
        del bluePixelList[:]#deletes pixellists  so only 9 values for each list gets saved each time

newImage.save('newImage.png')#creates new image and saves it to current directory type png
