import cv2
import imutils
from readVideoWithThread import WebcamVideoStream
from remove_img_background import rembg
import numpy as np
from PIL import ImageFile, Image
import os


def get_video_frame(video_stream):
    # created a *thread* video stream, allow the carera sensor to warmup
    # The function return a opencv mode frame, which is a picture
    print("[INFO] sampling THREAD frames from webcam...")
    # videoStream = WebcamVideoStream(src="rtsp://192.168.2.3:8080/h264_pcm.sdp").start()
    videoStream = WebcamVideoStream(
        src=video_stream).start()
    # img_counter = 0
    video_frame = None

    while True:
        # grab the frame from the threaded video stream and resize
        # it to have a maximum width of 400 pixels
        frame = videoStream.read()
        frame = imutils.resize(frame, height=700)

        # display the frame to our screen
        cv2.imshow("Frame", frame)
        # key = cv2.waitKey(1) & 0xFF
        # cv2.waitKey() method waits for the user's response through
        # a key press. This waitKey() method takes an argument of type
        # integer denoting the number of seconds to wait for the key press.
        # Press "q" to close the video window before it ends if you want
        if cv2.waitKey(22) & 0xFF == ord('q'):
            video_frame = frame
            cv2.destroyAllWindows()
            videoStream.stop()
            break

    return video_frame

    # cv2.imwrite("scratch.png", video_frame)


def get_rect_bounding(img):
    """
    img: the input image
    img_contour: draw contour on the image
    """
    # Change image color mode to gray
    img = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    contours, hierarchy = cv2.findContours(
        img, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_NONE)
    # Find the largest contour
    object_contour = max(contours, key=cv2.contourArea)

    # peri = cv2.arcLength(object_contour, True)
    # approx = cv2.approxPolyDP(object_contour, 0.02 * peri, True)
    # print(len(approx))
    x, y, w, h = cv2.boundingRect(object_contour)
    # cv2.rectangle(img_contour, (x, y), (x+w, y+h), (0, 255, 0), 5)
    return x, y, w, h


def crop_image(image, coordinate, padding=40):
    x, y, w, h = coordinate
    img_croped = image[y-padding:y+h+padding+1, x-padding:x+w+padding+1]
    return img_croped

# Refer
# [cv2-threshold](https://pyimagesearch.com/2021/04/28/opencv-thresholding-cv2-threshold/)
# [blending-and-pasting-images](https://datahacker.rs/012-blending-and-pasting-images-using-opencv/)

if __name__ == "__main__":
    # get_video_frame("rtsp://192.168.1.9:8080/h264_pcm.sdp")
    # img = get_video_frame("rtsp://192.168.2.3:8080/h264_pcm.sdp")
    # # img is opencv mode, we need to convert to pillow mode
    # # img = cv2.cvtColor(img, cv2.COLOR_BGR)
    # cv2.imwrite("temp.png", img)
    # image = Image.open("temp.png")
    # # img_pil = Image.fromarray(img)

    # img_rembg = rembg(image)
    # img_rembg.save("scratch.png")

    img = cv2.imread("scratch.png", cv2.IMREAD_UNCHANGED)

    coordinate = get_rect_bounding(img)
    img_cropt = crop_image(img, coordinate)

    # Create white background image
    white_bg = np.zeros([700, 700, 3], dtype=np.unit8)
    white_bg.fill(255)

    # reshape background removed image
    height, width = img.shape
    side = "height"
    # Paste background removed image to white background image

    cv2.imwrite("final_img.png", img_cropt)
