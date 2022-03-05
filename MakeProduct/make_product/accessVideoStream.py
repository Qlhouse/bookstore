from threading import Thread
import imutils
import cv2


class WebcamVideoStream:
    def __init__(self, src=0):
        # initialize the video camera stream and read the
        # first frame from the stream
        self.stream = cv2.VideoCapture(src)
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
    vs = WebcamVideoStream(src="rtsp://192.168.1.9:8080/h264_pcm.sdp").start()

    while True:
        # grab the frame from the threaded video stream and resize
        # it to have a maximum width of 400 pixels
        frame = vs.read()
        frame = imutils.resize(frame, width=400)

        # display the frame to our screen
        cv2.imshow("Frame", frame)
        key = cv2.waitKey(1) & 0xFF

    # do a bit of cleanup
    cv2.destroyAllWindows()
    vs.stop()
