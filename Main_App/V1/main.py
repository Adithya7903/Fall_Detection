import cv2
import time
from telegram import Bot
from datetime import datetime

# Edit the bot token and chat id before running the program

# Initialize the Telegram bot
bot = Bot(token="enter your bot's token here")  # Type your bot token here

# Video capture from file
cap = cv2.VideoCapture('50waystofall.mp4')

# Wait for a moment to ensure the camera is ready
time.sleep(2)

# Background subtraction using MOG2
fgbg = cv2.createBackgroundSubtractorMOG2()
j = 0  # Counter for consecutive frames where height is less than width

while True:
    # Read a frame from the video
    ret, frame = cap.read()

    try:
        # Convert the frame to grayscale for background subtraction
        gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
        fgmask = fgbg.apply(gray)

        # Find contours in the foreground mask
        contours, _ = cv2.findContours(fgmask, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)

        if contours:
            # List to hold all areas of detected contours
            areas = [cv2.contourArea(contour) for contour in contours]

            # Find the contour with the maximum area
            max_area = max(areas, default=0)
            max_area_index = areas.index(max_area)
            cnt = contours[max_area_index]

            # Calculate bounding box parameters
            x, y, w, h = cv2.boundingRect(cnt)

            # Draw contour on the foreground mask
            cv2.drawContours(fgmask, [cnt], 0, (255, 255, 255), 3, maxLevel=0)

            if h < w:
                j += 1

            # If consecutive frames have height less than width, consider it a fall
            if j > 10:
                print("The person is falling")  # Output message

                # Get current time for notification
                current_time = datetime.now().strftime("%Y-%m-%d %H:%M:%S")

                # Send a notification via Telegram
                bot.send_message(chat_id="Enter your chat id here", text=f"Fall detected at: {current_time}")

                # Mark the fall on the foreground mask
                cv2.putText(fgmask, 'FALL', (x, y), cv2.FONT_HERSHEY_TRIPLEX, 0.5, (255, 255, 255), 2)
                cv2.rectangle(frame, (x, y), (x + w, y + h), (0, 0, 255), 2)

            if h > w:
                j = 0  # Reset the counter
                cv2.rectangle(frame, (x, y), (x + w, y + h), (0, 255, 0), 2)

            # Display the video frame
            cv2.imshow('video', frame)

            # Break the loop if 'Esc' is pressed
            if cv2.waitKey(33) == 27:
                break
    except Exception as e:
        print(f"An error occurred: {e}")
        break

# Release video capture and close OpenCV windows
cap.release()
cv2.destroyAllWindows()