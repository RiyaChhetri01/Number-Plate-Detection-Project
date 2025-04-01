import cv2

haarcascade = "model/haarcascade_russian_plate_number.xml"

# reading the camera
cap = cv2.VideoCapture(0)
cap.set(3, 640)  # width
cap.set(4, 480)  # height

min_area = 500
count = 0

while True:
    success, img = cap.read()

    # loading the model
    plate_cascade = cv2.CascadeClassifier(haarcascade)
    img_gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

    plates = plate_cascade.detectMultiScale(img_gray, 1.1, 4)
    for x, y, w, h in plates:
        area = w * h
        if area > min_area:
            cv2.rectangle(img, (x, y), (x + w, y + h), (0, 255, 0), 2)
            cv2.putText(
                img,
                "Number Plate",
                (x, y - 5),
                cv2.FONT_HERSHEY_COMPLEX_SMALL,
                1,
                (255, 0, 255),
                2,
            )

            # above code is for just detecting the number plate

            # below code is now extract the number plate from the image and then apply OCR on it
            img_roi = img[y : y + h, x : x + w]  # cropping kar rhae hai

    cv2.imshow("Result", img)

    if cv2.waitKey(1) & 0xFF == ord("s"):
        cv2.imwrite("plates/scaned_img" + str(count) + ".jpg", img_roi)
        cv2.rectangle(img, (0, 200), (600, 300), (0, 255, 0), cv2.FILLED)
        cv2.putText(
            img,
            "Plate Saved",
            (150, 265),
            cv2.FONT_HERSHEY_COMPLEX_SMALL,
            2,
            (0, 0, 255),
            2,
        )
        cv2.imshow("Result", img)
        cv2.waitKey(500)
        count = count + 1
