import cv2
import numpy as np

# Read video from website
# vcap = cv2.VideoCapture("http://192.168.1.9:8080/video")
vcap = cv2.VideoCapture("rtsp://192.168.1.9:8080/h264_pcm.sdp")

img_counter = 0


def rescale_frame(frame, percent=75):
    width = int(frame.shape[1] * percent / 100)
    height = int(frame.shape[0] * percent / 100)
    dim = (width, height)
    return cv2.resize(frame, dim, interpolation=cv2.INTER_AREA)


while(True):
    # Capture frame-by-frame
    ret, frame = vcap.read()
    if frame is not None:
        # Display the resulting frame
        frame60 = rescale_frame(frame, 60)
        cv2.imshow('frame', frame60)
        # Press "q" to close the video window before it ends if you want
        if cv2.waitKey(22) & 0xFF == ord('q'):
            break
        if cv2.waitKey(1) % 256 == 32:
            # SPACE pressed, write down current frame
            img_name = f"opencv_frame_{img_counter}.png"
            cv2.imwrite(img_name, frame)
            print(f"{img_name} saved.")
            img_counter += 1
    else:
        print("Frame is None")
        break

# Capture image from video

# When everything done, release the capture
vcap.release()
cv2.destroyAllWindows()
print("Video stop")
