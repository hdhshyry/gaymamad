import cv2
src = cv2.imread('messi.jpg', cv2.IMREAD_UNCHANGED)

#percent by which the image is resized
scale_percent = 200

#calculate the 50 percent of original dimensions
width = int(src.shape[1] * scale_percent / 100)
height = int(src.shape[0] * scale_percent / 100)

# dsize
dsize = (width, height)

# resize image
output = cv2.resize(src, dsize)

cv2.imshow('ss',output)
cv2.waitKey(0)
cv2.destroyAllWindows()
layer = output.copy()
gp = [layer] #Declaring a variable hence creating the Gaussian Pyramid array.
for j in range(10):#Providing room for iteration.
    layer = cv2.pyrDown(layer)
    gp.append(layer)
    cv2.imshow(str(j), layer)#This function displays the multiple images created.
cv2.imshow("Original image",output)#This will have the original image displayed.
cv2.waitKey(0)
cv2.destroyAllWindows()