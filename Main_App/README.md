# Object Detection App

This repository contains a Python application for fall detection and object detection using OpenCV, YOLOv5, and Telegram.

## Features

- **Fall Detection**: Uses background subtraction to detect falls in a video stream.
- **Object Detection**: Utilizes YOLOv5 for real-time object detection in a video stream.
- **Telegram Notifications**: Sends notifications to a Telegram chat when falls or object detections occur.

## Getting Started

### Prerequisites

Make sure you have the following installed:

- Python 3
- OpenCV
- YOLOv5
- Telegram API Token

### Installation

1. Clone the repository:

    ```bash
    git clone https://github.com/Adithya7903/object-detection-app.git
    cd object-detection-app
    ```

2. Install requirements:

    ```bash
    pip install -r requirements.txt
    ```

### Usage

1. Run the application:

    ```bash
    python main.py
    ```

2. Follow the on-screen instructions to choose between fall detection and object detection.

## Configuration

- Replace `enter your token here` with your actual Telegram bot token in `app.py`.
- Ensure the correct file paths for YOLOv5 model weights and configuration files.

## Contributing

Feel free to contribute to this project. Fork the repository and create a pull request with your changes.


## Acknowledgments

- Thanks to [Ultralytics YOLOv5](https://github.com/ultralytics/yolov5) for the pre-trained YOLOv5 model.
- [Telegram Bot API](https://core.telegram.org/bots) for the Telegram integration.

