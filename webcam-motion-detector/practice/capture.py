import cv2, time

video = cv2.VideoCapture(0) 
## if it is a video file you can input a path "" between the brackets 
time.sleep(3) # will wait for 3 second
video = cv2.VideoCapture(0) 
# This requires double video = cv2.VideoCapture because hardware requires time to turn on
# This way the second input will be when the camera is on and that will be converted 

# To begin video capturing, use a while loop and use an if statement to break
while True:
    check, frame = video.read()
    # check if boolean, frame is np.array 
    # good use of check is to see if the script is actually running or not 
    print(check)
    print(frame)

    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

    cv2.imshow("Capturing", gray)
    key = cv2.waitKey(2000)

    if key ==ord('q'):
        break

video.release()
cv2.destroyAllWindows()