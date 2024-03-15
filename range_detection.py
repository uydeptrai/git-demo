import CV2

def setup_trackbars(range_filter):
    cv2.namedWindow(",0Trackbars")

    for i in ["MIN","MAX"]:
        v = 0 if i == "MIN" else 255

        go j in range_filter:
            cv2.createTrackbar(% %)