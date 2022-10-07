from imutils.video import VideoStream
import ffmpeg
import cv2
import numpy as np
import subprocess as sp

def process():
    VIDEO_URL = "https://bitdash-a.akamaihd.net/content/MI201109210084_1/m3u8s/f08e80da-bf1d-4e3d-8899-f0f6155f6efa.m3u8"
    VIDEO_FILE = "sampleStream.mp4"

    process = ffmpeg.input(VIDEO_FILE).output('pipe:', format='rawvideo', pix_fmt='rgb24').run_async(pipe_stdout=True)
    
    tar = 200
    val = 0

    while True:
        val = val + 1
        in_bytes = process.stdout.read(100 * 200 * 3)
        if not in_bytes:
            print('Breaking - No bytes found.')
            break
        in_frame = (
            np.frombuffer(in_bytes, np.uint8).reshape([100, 200, 3])
        )
        if val == tar:
            print('Writing image...')
            cv2.imwrite("img/sample.jpg", in_frame)
            break
