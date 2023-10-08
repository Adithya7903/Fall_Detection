# Object Detection and Notification System

## Overview

This Python script combines YOLOv5 for real-time object detection with a cooldown mechanism and dynamic Region of Interest (ROI) selection. Detected objects trigger notifications via Telegram, and additional features include bounding box labels, a confidence threshold, and logging.

## Features

- **Interactive ROI Selection:** Use mouse events to dynamically define the Region of Interest within the video stream.

- **Object Detection:** Implement YOLOv5 for real-time object detection within the selected ROI.

- **Telegram Notifications:** Receive instant Telegram notifications for detected objects, including class and confidence level.

- **Bounding Box Labels:** Display labels with confidence scores on bounding boxes.

- **Confidence Threshold:** Set a confidence threshold to filter detections and reduce false positives.

- **Logging:** Log detection events to a CSV file for further analysis.

## Setup

1. **Dependencies:**
   - Install the required dependencies:
     ```bash
     pip install torch opencv-python[headless] telegram
     ```

2. **Telegram Bot Setup:**
   - Obtain a Telegram bot token from [BotFather](https://t.me/BotFather).
   - Replace `"Enter your bot token"` and `"Enter your chat id"` with the obtained values in the script.

3. **Run the Script:**
   - Run the script using the command:
     ```bash
     python object_detection.py
     ```
   - Follow the instructions in the terminal to dynamically select the ROI.

4. **Exit the Program:**
   - Press 'Esc' to exit the program gracefully.

## Customization

- **Video Source:**
  - Change the video source by modifying the video file name or use a webcam by setting the source to `0`.

- **Region of Interest (ROI):**
  - Initially, set the value to `0` for dynamically selecting the ROI. After obtaining the diagonal coordinates, update the script with your coordinates and set the value to `1` to run the script with the restricted area.

- **Notification Recipient:**
  - Replace `"Enter your chat id"` with the designated chat ID for receiving Telegram notifications.

- **Confidence Threshold:**
  - Adjust the `confidence_threshold` variable to filter detections based on confidence level.

## Contributors

@Adithya7903 - Initial work


