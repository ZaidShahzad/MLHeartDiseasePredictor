# MLHeartDiseasePredictor

## Table of Contents
- [Overview](#overview)
- [Live Demo](#live-demo)
- [Features](#features)
- [How to Use](#how-to-use)
- [Technical Aspects](#technical-aspects)
- [Installation and Local Run](#installation-and-local-run)
- [License](#license)
- [Authors](#authors)

## Overview
The MLHeartDiseasePredictor is an interactive machine learning application designed to predict the likelihood of heart disease in patients based on various clinical parameters. Built using Python, it leverages a Support Vector Machine (SVM) model for predictions and is deployed with a Gradio interface on Hugging Face Spaces.

## Live Demo
Access the live application here: [Heart Disease Predictor](https://huggingface.co/spaces/ZaidShahzad/HeartDiseasePredictor)

## Features
- Predict the likelihood of heart disease in patients.
- Interactive web-based interface for easy input and visualization of predictions.
- Uses clinical parameters such as age, gender, type of chest pain, and more for analysis.

## How to Use
1. Visit the [Heart Disease Predictor](https://huggingface.co/spaces/ZaidShahzad/HeartDiseasePredictor) space.
2. Input the required patient data into the respective fields.
3. Click on "Predict" to view the prediction.
4. The app will display whether the patient is likely to have heart disease.

## Technical Aspects
- **Data Preprocessing**: Inputs are processed to fit the model's requirements, including categorical to numerical conversions.
- **Model**: Uses a Support Vector Machine (SVM) for making predictions.
- **Interface**: Built using Gradio, an open-source Python library for creating customizable ML interfaces.

## Installation and Local Run
To run the application locally, follow these steps:
1. Clone the repository.
2. Install the required dependencies using `pip install -r requirements.txt`.
3. Run `python App.py`.

## License
This project is licensed under the [MIT License](LICENSE).

## Authors
1. [Zaid Shahzad](https://github.com/ZaidShahzad)
2. [Ash112alash](https://github.com/ash112alash)
3. [Diegotyb](https://github.com/Diegotyb)
