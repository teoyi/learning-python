import cv2


img = cv2.imread(r"galaxy.jpg", 0) #color = 1, B&W = 0. color w alpha = -1

print(type(img))
print(img)
print(img.shape) ## shows the num of rows and columns in the array
print(img.ndim) ## shows dimensions of numpy array 

resized_image = cv2.resize(img, (int(img.shape[1]/2),int(img.shape[0]/2))) 
# previous size does not fit the screen size, so this will
# modify it 
cv2.imshow("Galaxy", resized_image)
cv2.imwrite("Galaxy_resized.jpg", resized_image) #This saves a new file
cv2.waitKey(0) # value in bracket is in milliseconds, 0 = press any button to close 
cv2.destroyAllWindows()

