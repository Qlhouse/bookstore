from __future__ import print_function
from measureFPS import FPS
from accessVidelStream import WebcamVideoStream
import argparse
import imutils
import cv2

# construct the argument parse and parse the arguments
ap = argparse.ArgumentParser()
ap.add_argument("-n", "--num-frames", type=int, default=1000,
                help="Number of frames to loop over fro FPS test")
ap.add_argument("-d", "--display", type=int, default=-1,
                help="Whether or not frames should be displayed")
args = vars(ap.parse_args())

# grab a pointer to the video stream and initialize the FPS counter
print("[INFO] sampling frame from webcam...")
# stream = cv2.VideoCapture("rtsp://192.168.2.3:8080/h264_pcm.sdp")
stream = cv2.VideoCapture("rtsp://192.168.1.9:8080/h264_pcm.sdp")
fps = FPS().start()

# loop over some frames
while fps._numFrames < args["num_frames"]:
    # grab the frame from the stream and resize it to have a
    # maximum width of 400 pixels
    (grabbed, frame) = stream.read()
    frame = imutils.resize(frame, width=400)

    # check to see if the frame should be displayed to our screen
    if args["display"] > 0:
        cv2.imshow("Frame", frame)
        key = cv2.waitKey(1) & 0xFF

    # update the FPS counter
    fps.update()

# stop the timer and display FPS information
fps.stop()
print("[INFO] elasped time: {:.2f}".format(fps.elapsed()))
print("[INFO] approx. FPS: {:.2f}".format(fps.fps()))

# do a bit of cleanup
stream.release()
cv2.destroyAllWindows()

# created a *thread* video stream, allow the carera sensor
# to warmup, and start the FPS counter
print("[INFO] sampling THREAD frames from webcam...")
# vs = WebcamVideoStream(src="rtsp://192.168.2.3:8080/h264_pcm.sdp").start()
vs = WebcamVideoStream(src="rtsp://192.168.1.9:8080/h264_pcm.sdp").start()
fps = FPS().start()


# loop over some frames...this time using the threaded stream
while fps._numFrames < args["num_frames"]:
    # grab the frame from the threaded video stream and resize
    # it to have a maximum width of 400 pixels
    frame = vs.read()
    frame = imutils.resize(frame, width=400)

    # check to see if the frame should be displayed
    # to our screen
    if args["display"] > 0:
        cv2.imshow("Frame", frame)
        key = cv2.waitKey(1) & 0xFF

    # update the FPS counter
    fps.update()

# stop the timer and display FPS information
fps.stop()
print("[INFO] elasped time: {:.2f}".format(fps.elapsed()))
print("[INFO] approx. FPS: {:.2f}".format(fps.fps()))

# do a bit of cleanup
cv2.destroyAllWindows()
vs.stop()
