# Object Detection and Notification System

## Overview

This repository hosts a Python script that employs YOLOv5 for real-time object detection within a specified Region of Interest (ROI) in a video stream. Detected objects trigger notifications via Telegram, providing instantaneous alerts. The script supports dynamic ROI selection through mouse events for enhanced flexibility.

## Features

- **Interactive ROI Selection:** Utilize the mouse events to dynamically define the Region of Interest (ROI) within the video stream.

- **Object Detection:** Employ YOLOv5 for accurate and real-time object detection within the selected ROI.

- **Telegram Notifications:** Receive instant notifications on Telegram when an object is detected, including the type of object and the timestamp.

## Setup

1. **Dependencies:**
   - Install the required dependencies:
     ```bash
     pip install torch opencv-python[headless] telegram
     ```

2. **Telegram Bot Setup:**
   - Obtain a Telegram bot token from [BotFather](https://t.me/BotFather).
   - Replace `"Enter your bot token"` with the obtained token in the script.

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
  - Initially, set the value to `0` for dynamically selecting the ROI. After obtaining the diagonal coordinates, update the script with your own coordinates and set the value to `1` to run the script with the restricted area.

- **Notification Recipient:**
  - Replace `"Enter your chat id"` with the designated chat ID for receiving Telegram notifications.

## Contributors

- @Adithya7903 - Initial work


