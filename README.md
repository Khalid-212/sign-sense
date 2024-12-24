# Sign-Sense: Amharic Sign Language Recognition

**Sign-Sense** is an innovative project aimed at recognizing Amharic sign language gestures using computer vision and machine learning techniques. This project leverages OpenCV for image processing, FreeType for rendering Amharic text, and a pre-trained model for accurate gesture classification. It seeks to bridge the communication gap by enabling seamless interaction through Amharic sign language.

## Project Overview

Sign-Sense provides a solution for recognizing Amharic sign language gestures with high accuracy, offering:
- Gesture classification using a pre-trained machine learning model.
- Real-time hand gesture data collection.
- Rendering of Amharic text on images to display recognized gestures.

## Project Structure

The repository contains the following files:

### Scripts
- **`dataCollection.py`**: Script to collect hand gesture data using a webcam.
- **`fep.py`**: Script to render Amharic text on an image using FreeType and OpenCV.
- **`test.py`**: Script to test hand gesture recognition using a pre-trained model.

### Configuration & Dependencies
- **`.gitignore`**: Specifies files and directories to be ignored by Git.
- **`settings.json`**: VS Code settings for the project configuration.
- **`labels.txt`**: A list of labels representing hand gestures.
- **`requirements.txt`**: List of dependencies required to run the project.

## Setup

Follow these steps to set up the project on your local machine:

1. Clone the repository:
   ```bash
   git clone https://github.com/yourusername/Sign-Sense.git
   cd Sign-Sense
   ```

2. Install the required dependencies:
   ```bash
   pip install -r requirements.txt
   ```

3. Ensure you have a webcam connected to your system for gesture data collection.

## Usage

### Data Collection

To collect hand gesture data, run the **`dataCollection.py`** script:

```bash
python dataCollection.py
```

- Press **`s`** to save an image of the current hand gesture.
- Press **`q`** to quit the data collection process.

### Amharic Text Rendering

To render Amharic text on an image, run the **`fep.py`** script:

```bash
python fep.py
```

This script will overlay Amharic text on images using FreeType and OpenCV.

### Gesture Recognition

To test the hand gesture recognition, run the **`test.py`** script:

```bash
python test.py
```

- The system will classify gestures based on a pre-trained model.
- Press **`q`** to quit the recognition process.

## License

This project is licensed under the [MIT License](LICENSE).

## Acknowledgements

- **OpenCV** – For image processing and computer vision capabilities.
- **FreeType** – For rendering Amharic text in the application.
- **cvzone** – For additional computer vision tools.

Feel free to contribute to this project by submitting issues or pull requests. Your contributions are welcome!
