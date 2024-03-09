import cv2

cap = cv2.VideoCapture(0)

while True:
    ret, frame = cap.read()

    # Canny edge detection
    edges = cv2.Canny(frame, 100, 200)

    # Blur
    blurred = cv2.blur(frame, (15, 15), 0)

    # Feature detection
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    corners = cv2.goodFeaturesToTrack(gray, maxCorners=25, qualityLevel=0.01, minDistance=10)
    if corners is not None:
        corners = corners.astype(int)
        for corner in corners:
            x, y = corner[0]
            cv2.circle(frame, (x, y), 5, (0, 0, 255), -1)

    cv2.imshow('Features', frame)
    cv2.imshow('Canny Edge Detection', edges)
    cv2.imshow('Blurred', blurred)

    if cv2.waitKey(1) == 27:
        break

cap.release()
cv2.destroyAllWindows()