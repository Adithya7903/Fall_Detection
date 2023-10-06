import torch
import cv2
from telegram import Bot
from datetime import datetime

# Initialize the Telegram bot
bot = Bot(token="Enter your bot token")  # Enter your bot token

# Function to capture mouse events for selecting ROI
def POINTS(event, x, y, flags, param):
    if event == cv2.EVENT_MOUSEMOVE:  
        colorsBGR = [x, y]
        print(colorsBGR)

# Create a window for capturing mouse events
cv2.namedWindow('ROI')
cv2.setMouseCallback('ROI', POINTS)

# Open video capture (replace '2.mp4' with the video file name or type 0 for webcam)
cap = cv2.VideoCapture('2.mp4')

# Load YOLOv5 model
model = torch.hub.load('ultralytics/yolov5', 'yolov5s', pretrained=True)

count = 0

while True:
    try:
        ret, frame = cap.read()
        
        # Exit loop if no frame is captured
        if not ret:
            break
        
        count += 1
        
        # Process every third frame
        if count % 3 != 0:
            continue
        
        # Resize the frame for processing
        frame = cv2.resize(frame, (1020, 500))
        
        # Define the Region of Interest (ROI) based on mouse events
        ROI = frame[62:311, 295:705]  # Example restricted area [295, 62],[705, 311]
        
        # Run YOLOv5 on the ROI
        results = model(ROI)
        
        # Iterate through detected objects and draw rectangles
        for index, row in results.pandas().xyxy[0].iterrows():
            x1, y1, x2, y2 = map(int, [row['xmin'], row['ymin'], row['xmax'], row['ymax']])
            detected_class = row['name']
            print(detected_class)
            
            # Get current time for notification
            current_time = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
            
            # Send a Telegram message for each detection
            bot.send_message(chat_id="Enter your chat id", text=f"Detected {detected_class} at: {current_time}")
            
            # Draw rectangle on the ROI
            cv2.rectangle(ROI, (x1, y1), (x2, y2), (0, 255, 0), 2)
        
        # Display the frame with the ROI
        cv2.imshow("ROI", frame)
        
        # Wait for the 'Esc' key to exit the program
        if cv2.waitKey(0) & 0xFF == 27:
            '''
            First time keep value 0 and run the program, note down opposite diagonal co-ordinates with your mouse
            Edit the "ROI" frame with the given format above with your own co-ordinates,
            Then change it to 1 so you can run it with the restricted area
            '''
            break

    except KeyboardInterrupt:
        print("KeyboardInterrupt received. Exiting gracefully.")
        break

# Release video capture and close OpenCV windows
cap.release()
cv2.destroyAllWindows()
