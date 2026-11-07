
import cv2
import easyocr
import pyttsx3

# Initialize the OCR reader and speech engine once
reader = easyocr.Reader(["en"], gpu=False)
engine = pyttsx3.init()

# Open laptop camera
camera = cv2.VideoCapture(0)

print("Press SPACE to capture and read.")
print("Press Q to quit.")

while camera.isOpened():
    success, frame = camera.read()

    if not success:
        break
    cv2.imshow("Blind Reader Camera", frame)
    key = cv2.waitKey(1) & 0xFF
 
    if key == ord(" "):
        # Convert captured image to text
        results = reader.readtext(frame, detail=0)
        text = " ".join(results).strip()

        if text:
            print("Detected text:", text)
            engine.say(text)
            engine.runAndWait()
        else:
            engine.say("No text detected. Please try again.")
            engine.runAndWait()

    elif key == ord("q"):
        break

camera.release()
cv2.destroyAllWindows()
