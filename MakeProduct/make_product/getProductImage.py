import cv2
import imutils
import time
from threading import Thread
from rembg.bg import remove
import numpy as np
from PIL import ImageFile, Image
import os


class WebcamVideoStream:
    def __init__(self, src=0):
        # initialize the video camera stream and read the
        # first frame from the stream
        self.stream = cv2.VideoCapture(src)
        time.sleep(2)

        # Using read() method to access the camera stream, returns a tuple
        # The first value is a Boolean value representing whether
        # a frame is captured correctly or not. With this, you can know
        # at the end of a video capture whether all the frames are captured
        # correctly or not.
        # The second value is the captured frame, which is basically a numpy array.
        (self.grabbed, self.frame) = self.stream.read()

        # initialize the variable used to indicate if
        # the thread shoud be stopped
        self.stopped = False

    def start(self):
        # start the thread to read frames from the video stream
        Thread(target=self.update, args=()).start()
        return self

    def update(self):
        # keep looping infinitely until the thread is stopped
        while True:
            # if the thread indicator variable is set, stop the thread
            if self.stopped:
                return

            # otherwise, read the next frame from the stream
            (self.grabbed, self.frame) = self.stream.read()

    def read(self):
        # return the frame most recently read
        return self.frame

    def stop(self):
        # indicate that the thread should be stopped
        self.stopped = True


def rembg(image, truncated=False):

    # image: image data opened by pillow
    # # Remove background
    # truncated is True if working with trucated image formats (ex. JPEG / JPG)
    if truncated:
        ImageFile.LOAD_TRUNCATED_IMAGES = True

    return remove(image)


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

        # Press "q" to close the video window before it ends if you want
        if cv2.waitKey(22) & 0xFF == ord('q'):
            video_frame = frame
            cv2.destroyAllWindows()
            videoStream.stop()
            break
    # Return image for this frame
    return video_frame

    # cv2.imwrite("scratch.png", video_frame)


def get_rect_bounding(img):
    # Change image color mode to gray
    img = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    contours, hierarchy = cv2.findContours(
        img, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_NONE)
    # Find the largest contour
    object_contour = max(contours, key=cv2.contourArea)

    x, y, w, h = cv2.boundingRect(object_contour)
    # cv2.rectangle(img_contour, (x, y), (x+w, y+h), (0, 255, 0), 5)
    return x, y, w, h


def crop_image(image, coordinate):
    # 裁剪后只剩下3条色道，透明色道没了
    # [TODO] How to crop PNG image
    x, y, w, h = coordinate
    img_croped = image[y:y+h+1, x:x+w+1]
    return img_croped


def overlay_transparent():
    pass


def cv2pillow(image):
    """Input opencv mode image, return pillow mode image"""
    # img = cv2.imread("scratch.png", cv2.IMREAD_UNCHANGED)

    if image.shape[2] == 4:
        # You may need to convert the color.
        img_rgba = cv2.cvtColor(image, cv2.COLOR_BGRA2RGBA)
        img_rgba[:, :, 3] = image[:, :, 3]
        img_pil = Image.fromarray(img_rgba)
    elif image.shape[2] == 3:
        # You may need to convert the color.
        img_rgba = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)
        img_pil = Image.fromarray(img_rgba)

    return img_pil
    # img_pil.save("openct2PIL.png")


def pillow2cv(image):
    """Input pillow mode image, return opencv mode image"""
    # img = cv2.imread("scratch.png", cv2.IMREAD_UNCHANGED)

    img_opencv = cv2.cvtColor(np.array(image), cv2.COLOR_RGBA2BGRA)

    return img_opencv
    # cv2.imwrite("img_opencv", img_opencv)
    # img_pil.save("openct2PIL.png")


# Refer
# [cv2-threshold](https://pyimagesearch.com/2021/04/28/opencv-thresholding-cv2-threshold/)
# [blending-and-pasting-images](https://datahacker.rs/012-blending-and-pasting-images-using-opencv/)


def take_photo(videoStream):
    # def take_photo():
    # get_video_frame("rtsp://192.168.1.9:8080/h264_pcm.sdp")
    img = get_video_frame(video_stream=videoStream)
    # img = cv2.imread("temp.png", cv2.IMREAD_UNCHANGED)
    # img is opencv mode, we need to convert to pillow mode
    # cv2.imwrite("temp.png", img)
    # image = Image.open("temp.png")
    img_pillow = cv2pillow(img)

    img_rembg = rembg(img_pillow)

    img_cv = pillow2cv(img_rembg)
    # print("image img_cv's shape: ", img_cv.shape)
    coordinate = get_rect_bounding(img_cv)
    img_crop = crop_image(img_cv, coordinate)
    print("image img_crop's shape: ", img_crop.shape)

    # Initialize the final image
    bg_side = 700
    final_img = np.zeros([bg_side, bg_side, 4], dtype=np.uint8)
    final_img.fill(255)

    # reshape the cropped image
    product_img_side = 650
    img_resize = imutils.resize(
        img_crop, height=product_img_side) if img.shape[0] > img.shape[1] else \
        imutils.resize(img_crop, width=product_img_side)

    print("image img_resize's shape: ", img_resize.shape)
    # Paste background removed image to white background image
    height, width = img_resize.shape[:2]
    x_offset = int((bg_side - width) / 2)
    x_end = x_offset + width

    y_offset = int((bg_side - height) / 2)
    y_end = y_offset + height

    final_img[y_offset:y_end, x_offset:x_end] = img_resize

    return final_img


if __name__ == "__main__":
    videoStream = "rtsp://192.168.2.3:8080/h264_pcm.sdp"
    image = take_photo(videoStream)
    cv2.imwrite("final_img.png", image)
