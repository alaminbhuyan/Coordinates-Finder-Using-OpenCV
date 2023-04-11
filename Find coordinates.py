# Used python version 3.10
# load necessary libraries
import cv2
import os


# Function to display the coordinates of the points clicked on the image
def click_event(event, x, y, flags, params):
    global i
    # Checking for left mouse clicks
    if event == cv2.EVENT_LBUTTONDOWN:
        # display the coordinates on the terminal
        print(x, ' ', y)
        # create a file and store the coordinates information
        with open(file="coordinates.txt", mode='a') as f:
            f.write(f"point:{i}:-> x: {x}, y: {y}\n")
            i += 1
        # Display the coordinates on the image window
        font = cv2.FONT_HERSHEY_SIMPLEX
        cv2.putText(img=img, text=str(x) + ' , ' + str(y), org=(x, y), fontFace=1, fontScale=1, color=(255, 0, 0),
                    thickness=2)
        cv2.imshow("Image", img)
    # Checking for right mouse clicks
    if event == cv2.EVENT_RBUTTONDOWN:
        # display the coordinates on the terminal
        print(x, ' ', y)
        # Display the coordinates on the image window
        font = cv2.FONT_HERSHEY_SIMPLEX
        blue = img[y, x, 0]
        green = img[y, x, 1]
        red = img[y, x, 2]

        cv2.putText(img=img, text=str(blue) + ' , ' + str(green) + ' , ' + str(green), org=(x, y), fontFace=1,
                    fontScale=1, color=(255, 0, 0),
                    thickness=2)
        cv2.imshow("Image", img)


# driver function
if __name__ == '__main__':
    if os.path.exists("coordinates.txt"):
        os.remove("coordinates.txt")
    i = 1
    img = cv2.imread("Image/Bangladesh_Flag61.jpeg")
    img = cv2.resize(src=img, dsize=(500, 500))
    cv2.imshow("Image", img)
    # setting mouse handler for the image and calling the click_event function
    # cv2.setMouseCallback(windowName, onMouse)
    cv2.setMouseCallback('Image', click_event)
    cv2.waitKey()
    cv2.destroyAllWindows()
