import cv2
from time import time

# view on the camera
def view_camera():

    cap = cv2.VideoCapture(-1)

    while True:
        ret, frame = cap.read()
        cv2.imshow('frame', frame)

        # press Q to quit
        if cv2.waitKey(1) & 0xFF == ord('q'):
            break

    cap.release()
    cv2.destroyAllWindows()



# read a video and write a new video
def write_video(str):
    cap = cv2.VideoCapture(str)

    fcc = cv2.VideoWriter_fourcc('M','J','P','G')
    frame_width = int(cap.get(3)) # cv2.CAP_PROP_FRAME_WIDTH
    frame_height = int(cap.get(4)) # cv2.CAP_PROP_FRAME_HEIGHT

    out = cv2.VideoWriter('./assets/videos/out.avi', fcc, 60, (frame_width, frame_height))

    first_milisecond = int(time() * 1000)
    print(first_milisecond)
    while cap.isOpened:
        ret, frame = cap.read()
        if ret:
            gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
            cv2.imshow('frame', frame)
            cv2.imshow('gray', gray)
            print(gray)
            out.write(frame)

            if cv2.waitKey(1) & 0xFF == 27:
                break

            print('video is playing...')
        else:
            break

    last_milisecond = int(time() * 1000)
    run_time = (last_milisecond - first_milisecond) / 1000
    print(f'Completed: {run_time}s!')
    print(cap.get(5)) # FPS
    print(cap.get(6)) # FourCC
    cap.release()
    out.release()
    cv2.destroyAllWindows()

# view the video wrote
def read_out(str):
    cap = cv2.VideoCapture(str)

    first_milisecond = int(time() * 1000)
    print(first_milisecond)
    while cap.isOpened:
        ret, frame = cap.read()

        if ret:
            cv2.imshow('frame', frame)
            if cv2.waitKey(1) & 0xFF == 27:
                break
            print('video is playing...')

        else:
            break

    last_milisecond = int(time() * 1000)
    run_time = (last_milisecond - first_milisecond) / 1000
    print(f'Completed: {run_time}s!')
    cap.release()
    cv2.destroyAllWindows()


write_video('./assets/videos/test_video.mp4')
# read_out('./assets/videos/out.avi')
