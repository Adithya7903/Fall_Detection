# Fall Detection System using OpenCV
# Overview
This repository contains a Python script for a fall detection system utilizing the OpenCV computer vision library. The system processes video input, identifies potential falls based on changes in object dimensions, and triggers alerts, including notifications through Telegram.

# Features
Background Subtraction: Utilizes the MOG2 background subtraction algorithm to isolate foreground objects from video frames.

Contour Analysis: Detects contours in the foreground mask, enabling the identification of objects and their key features.

Fall Detection: Monitors the height-to-width ratio of identified contours; a sustained change triggers fall detection.

Telegram Notification: Sends real-time fall alerts via Telegram, providing instant notifications to designated recipients.
# Prerequesite
-packages to downlaod
- python==2.7.7
- numpy==1.14.5
- opencv-python==3.4.1.15
- pylint==1.9.2
- scikit-learn==0.19.1

# How it works
For each frame readed of the video corverted into gray, is removed the background, finded the contour and drawed the contours.
If the heigh of the contour is lower than width, it may be a fall and we add 1 to a count, if the count is greater than 10, will be drawed a rectangle to the possible person fallen.

# Please remember to replace the placeholder comments with your actual bot token and chat ID before running the script. Additionally, ensure that you have the necessary libraries installed, such as the python-telegram-bot library.





