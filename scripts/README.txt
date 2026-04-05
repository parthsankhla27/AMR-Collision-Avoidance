# Project Code and Supporting Files

This document provides a summary of the code and supplementary files submitted as part of the MMAE 500 Data-Driven Modeling project: "Collision Hazard Detection for Autonomous Mobile Robots Using Deep Learning-Based Object Detection".

The files are organized as follows:

## Python Scripts
* `checklabel.py`:
    * A  script used during initial data exploration to check and print the class IDs present in the raw dataset label files before any relabeling or merging. Helps verify the starting point of the data.
* `convertlabels.py`:
    * Contains functions and logic to convert bounding box annotations from various potential formats (e.g., 4-point rotated, or just re-formatting standard YOLO) into a consistent standard YOLO format (center_x, center_y, width, height). Used as part of the data preprocessing pipeline.
* `relabel_dataset.py`:
    * The main custom script developed for data preprocessing. It implements the logic to iterate through the raw dataset folders and reassign the class ID of each bounding box according to a predefined mapping, consolidating different original labels into the unified target classes for training.
* `visualizelabels.py`:
    * Script used to overlay bounding boxes and class labels onto images. Essential for visually verifying the accuracy of dataset annotations and preprocessing steps before model training.

## Configuration and Results
* `args.yaml`:
    * Configuration file detailing the parameters used for the model training run, including hyperparameters (epochs, batch size, optimizer, learning rates), input settings (image size), hardware device, and paths.
* `data.yaml`:
    * Configuration file used by the training script (YOLOv8) to define the paths to the training, validation, and test datasets and the names of the object classes 


This collection of files supports the methods and results presented in the accompanying project report. The Python scripts demonstrate the data preprocessing steps, while the configuration and results files provide the details of the training setup and quantitative performance evaluation.