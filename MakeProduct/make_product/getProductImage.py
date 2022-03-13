import cv2
import imutils
from readVideoWithThread import WebcamVideoStream

# Get a frame in which the product is clear
# created a *thread* video stream, allow the carera sensor to warmup
print("[INFO] sampling THREAD frames from webcam...")
# videoStream = WebcamVideoStream(src="rtsp://192.168.2.3:8080/h264_pcm.sdp").start()
videoStream = WebcamVideoStream(
    src="rtsp://192.168.1.9:8080/h264_pcm.sdp").start()
# img_counter = 0

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
        break
    if cv2.waitKey(1) % 256 == 32:
        # SPACE pressed, write down curent frame
        # videoStream.stream.release()  # Release the camera
        # img_name = f"opencv_frame_{img_counter}.png"
        cv2.imwrite(img_name, frame)
        print(f"{img_name} saved.")
        # img_counter += 1
