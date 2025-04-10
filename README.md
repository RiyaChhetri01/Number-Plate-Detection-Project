
#  Number Plate Detection using OpenCV & EasyOCR

This project aims to detect and recognize vehicle number plates using a combination of **OpenCV** for image processing and **EasyOCR** for Optical Character Recognition (OCR). It was developed as a collaborative project by [Riya Chhetri](https://github.com/RiyaChhetri01) and [Lakshay Sharma](#) to explore real-time object detection and text recognition techniques.

---

## Project Overview

The model detects number plates from vehicle images using a **Haar Cascade classifier**, and then uses **EasyOCR** to extract the alphanumeric characters from the detected region.

---

## Dataset

- The model is trained using **.xml files for Russian number plates**.
- Haar Cascade (`haarcascade_russian_plate_number.xml`) is used to detect the plate region from vehicle images.

---

## How It Works

1. **Input** an image containing a vehicle.
2. **Detect** the number plate region using OpenCV's `CascadeClassifier`.
3. **Crop** the detected region of interest (ROI).
4. **Recognize** the text using EasyOCR.
5. **Display** the detected plate and the recognized text on the image using OpenCV's `rectangle()` and `putText()` functions.

---

##  Technologies Used

- Python
- OpenCV
- EasyOCR
- Haar Cascade Classifier

---

##  Setup Instructions

1. **Clone the Repository**
   ```bash
   git clone https://github.com/RiyaChhetri01/Number-Plate-Detection-Project.git
   cd Number-Plate-Detection-Project
## 🙌 Contributors

- [Riya Chhetri](https://github.com/RiyaChhetri01)  
- [Lakshay Sharma](https://github.com/CODE-LAKSHAY-SHARMA)

