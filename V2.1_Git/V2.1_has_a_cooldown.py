import torch
import cv2
from telegram import Bot
from datetime import datetime
import time
import csv

# Initialize the Telegram bot
bot = Bot(token="Enter your token here")

# Function to capture mouse events for selecting ROI
def POINTS(event, x, y, flags, param):
    if event == cv2.EVENT_MOUSEMOVE:
        colorsBGR = [x, y]
        print(colorsBGR)

# Create a window for capturing mouse events
cv2.namedWindow('ROI')
cv2.setMouseCallback('ROI', POINTS)

# Open video capture (replace '1.mp4' with the video file name or type 0 for webcam)
cap = cv2.VideoCapture('1.mp4')

# Load YOLOv5 model
model = torch.hub.load('ultralytics/yolov5', 'yolov5s', pretrained=True)

# Counter for frame processing
count = 0

# Cooldown mechanism variables
cooldown_start_time = time.time()
cooldown_duration = 1  # cooldown duration in seconds

# Confidence threshold for detection
confidence_threshold = 0.5

# CSV file for logging detections
log_file = 'detections_log.csv'

# Create and write header to the log file
with open(log_file, 'w', newline='') as csvfile:
    fieldnames = ['Timestamp', 'Class', 'Confidence', 'Xmin', 'Ymin', 'Xmax', 'Ymax']
    writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
    writer.writeheader()

while True:
    try:
        # Read a frame from the video
        ret, frame = cap.read()

        # Exit loop if no frame is captured
        if not ret:
            break

        # Process every third frame
        count += 1
        if count % 3 != 0:
            continue

        # Resize the frame for processing
        frame = cv2.resize(frame, (1020, 500))

        # Run YOLOv5 on the frame
        results = model(frame)
        current_time = datetime.now().strftime("%Y-%m-%d %H:%M:%S")

        # Check cooldown before processing detections
        if time.time() - cooldown_start_time >= cooldown_duration:
            for index, row in results.pandas().xyxy[0].iterrows():
                x1 = int(row['xmin'])
                y1 = int(row['ymin'])
                x2 = int(row['xmax'])
                y2 = int(row['ymax'])
                confidence = row['confidence']
                class_name = row['name']

                # Check if the detection confidence is above the threshold
                if confidence > confidence_threshold:
                    # Log the detection
                    with open(log_file, 'a', newline='') as csvfile:
                        writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
                        writer.writerow({
                            'Timestamp': current_time,
                            'Class': class_name,
                            'Confidence': confidence,
                            'Xmin': x1,
                            'Ymin': y1,
                            'Xmax': x2,
                            'Ymax': y2
                        })

                    # Send a Telegram message for each detection
                    bot.send_message(chat_id="Enter your chat id here",
                                     text=f"Detected {class_name} with confidence {confidence} at: {current_time}")

                    # Draw rectangle and label on the frame
                    label = f"{class_name}: {confidence:.2f}"
                    cv2.rectangle(frame, (x1, y1), (x2, y2), (0, 255, 0), 2)
                    cv2.putText(frame, label, (x1, y1 - 10), cv2.FONT_HERSHEY_SIMPLEX, 0.5, (0, 255, 0), 2)

            # Reset cooldown timer
            cooldown_start_time = time.time()

        # Display the frame with the ROI
        cv2.imshow("ROI", frame)

        # Wait for the 'Esc' key to exit the program
        if cv2.waitKey(1) & 0xFF == 27:
            break

    except KeyboardInterrupt:
        print("KeyboardInterrupt received. Exiting gracefully.")
        break

# Release video capture and close OpenCV windows
cap.release()
cv2.destroyAllWindows()
