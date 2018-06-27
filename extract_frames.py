import cv2

#os.chdir("./DashCam_Footage")
path = './DashCam_Footage/Video2.MP4'
vidcap = cv2.VideoCapture(path)
success, image = vidcap.read()

count = 0
success = True

while success:
    success, image = vidcap.read()
    print('Read a new frame: ', success)
    cv2.imwrite('DashCam_Footage/Video2_Frames/%d.jpg' % count, image)     # save frame as JPEG file
    count += 1
