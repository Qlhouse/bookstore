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


if __name__ == "__main__":
    # get_video_frame("rtsp://192.168.1.9:8080/h264_pcm.sdp")
    img = get_video_frame("rtsp://192.168.2.3:8080/h264_pcm.sdp")
    # img is opencv mode, we need to convert to pillow mode
    img = cv2.cvtColor(img, cv2.COLOR_BGR)
    cv2.imwrite("temp.png", img)
    image = Image.open("temp.png")
    # img_pil = Image.fromarray(img)

    img_rembg = rembg(image)
    img_rembg.save("scratch.png")
    # img_background_removed is pillow mode, convert to opencv mode
    # img_rembg_cv = np.asarray(img_rembg)
    # cv2.imwrite("scratch.png", img_rembg_cv)
