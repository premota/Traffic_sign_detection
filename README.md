# Creating an Automatic Traffic sign detection model using YOLOv8 on custom dataset

## Result from testing
![traffic_sign_recorgnition](https://github.com/premota/Traffic_sign_detection/assets/105300445/f89db439-6b84-42de-89c4-6ad5111ed8b9)

## Overview
Welcome to the future of robotic perception! Our project harnesses the power of YOLOv8, a cutting-edge object detection model, to revolutionize the way autonomouse vehicles interpret and respond to their environment. By focusing on the critical task of traffic sign detection, we aim to enhance the safety and efficiency of autonomous vehicle systems navigating complex real-world scenarios.

## Project objectives
1. collect and annotate image dataset of Traffic signs.
2. Download pre-trained yolov8 model from ultralytics
3. Train yolov8 on custome dataset and test on video file.
   
## Project requirements
1. Python 3.8
2. Numpy 1.24.1
3. Pandas 2.0.3
4. Ultralytics 8.0.196
5. OpenCV-python 4.8.0.74

## Dataset
the data used for this project was collected from www.kaggle.com and is available on "data" folder.

## Project Architecture
Project Architecture
The project is organized into structured folders and files to facilitate seamless development, training, testing, and documentation.

**Folders:**
1.data:
Description: Contains the annotated dataset for training and evaluation.
Purpose: Facilitates model training by providing a diverse set of images with annotated traffic signs.

2. test_result:
Description: Stores the results of testing the trained model.
Purpose: Enables the assessment of model performance on new images or videos.

3. test_video:
Description: Holds video data for testing the model on dynamic scenarios.
Purpose: Allows the evaluation of the model's ability to detect traffic signs in real-time video streams.

**Files:**

1. README.md:
Description: Comprehensive documentation for the project.
Purpose: Serves as the primary reference point for understanding the project's goals, structure, and usage.

2. Training.ipynb:
Description: colabs Notebook for training the traffic sign detection model.
Purpose: Provides an interactive and detailed environment for training the model using the specified dataset.

3. traffic_sign.pt:
Description: File containing the trained model weights.
Purpose: Stores the learned parameters of the traffic sign detection model for later use in inference.
traffic_sign.yaml:

4. Description: YAML configuration file for the YOLOv8 model.
Purpose: Defines the architecture, training parameters, and settings of the YOLOv8 model, ensuring reproducibility.

5. video_test.py:
Description: Python script for testing the model on video data.
Purpose: Provides a programmatic interface for assessing the model's performance on dynamic video scenarios.


## Future goals
This traffic sign detection project sets the stage for elevating the capabilities of self-driving vehicles in navigating dynamic environments. Looking ahead, here are concise directions for mu future work, focusing on key enhancements:

1. Semantic Understanding:
Expand the model to not only detect traffic signs but also understand their contextual meaning, enabling more nuanced decision-making by self-driving vehicles.

2. Adaptive Learning in Changing Environments:
Develop adaptive learning mechanisms to help the model adjust dynamically to evolving conditions, ensuring sustained performance in changing scenarios.

3. Multi-Modal Integration:
Investigate the fusion of multi-modal data, combining inputs from cameras, LiDAR, and other sensors to enhance the model's overall understanding of the environment.

4. Open-Source Collaboration:
Foster an open-source community around self-driving vehicle traffic sign detection, encouraging collaboration and contributions from researchers and developers globally.

5. Continuous Dataset Expansion:
Regularly update and expand the training dataset to keep the model adaptable to new traffic sign variations, regional differences, and emerging challenges.

6. Benchmarking and Evaluation Metrics:
Contribute to standardized benchmarks and evaluation metrics for self-driving vehicle traffic sign detection, facilitating fair comparisons and best practices.
