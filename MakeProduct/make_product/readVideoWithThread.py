from threading import Thread
import imutils
import cv2
import time


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


if __name__ == '__main__':
    # created a *thread* video stream, allow the carera sensor to warmup
    print("[INFO] sampling THREAD frames from webcam...")
    # vs = WebcamVideoStream(src="rtsp://192.168.2.3:8080/h264_pcm.sdp").start()
    vs = WebcamVideoStream(src="http://192.168.2.3:8080").start()
    img_counter = 0

    while True:
        # grab the frame from the threaded video stream and resize
        # it to have a maximum width of 400 pixels
        frame = vs.read()
        frame = imutils.resize(frame, height=600)

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
            # SPACE pressed, write down current frame
            # vs.stream.release()  # Release the camera
            img_name = f"opencv_frame_{img_counter}.png"
            cv2.imwrite(img_name, frame)
            print(f"{img_name} saved.")
            img_counter += 1

    # do a bit of cleanup
    cv2.destroyAllWindows()
    vs.stop()
