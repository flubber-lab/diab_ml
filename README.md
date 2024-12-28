# Diabetes Prediction App

## Overview
This repository contains a Streamlit-based web application that predicts the likelihood of diabetes based on user inputs. The app uses a machine learning model pre-trained by the author to provide predictions in real-time.

## Features
- User-friendly interface built with Streamlit.
- Predicts diabetes risk based on inputs like gender, age, BMI, and medical history.
- Displays results dynamically with visual and audio feedback.
- Integrates a custom-trained machine learning model for accurate predictions.

## Installation

1. Clone the repository:
   ```bash
   git clone [<repository_url>](https://github.com/flubber-lab/diab_ml.git)
   cd diab_ml
   ```
2. Install the required Python libraries:
   ```bash
   pip install -r requirements.txt
   ```
3. Ensure the trained model file (`Arun.pkl`) is in the root directory.
4. Run the application:
   ```bash
   streamlit run app.py
   ```

## Inputs
The application accepts the following inputs from the user:

- **Gender**: Select from Male, Female, or Other.
- **Age**: Enter your age as a number.
- **Hypertension**: Indicate whether you have hypertension (Yes/No).
- **Heart Disease**: Indicate whether you have heart disease (Yes/No).
- **Smoking History**: Select from options like Current, Former, Never, etc.
- **BMI**: Enter your Body Mass Index.
- **HbA1c Level**: Enter your HbA1c level.
- **Blood Glucose Level**: Enter your blood glucose level.

## Outputs
- **Diabetes Prediction**: The app predicts whether the user is diabetic or not.
- **Feedback**:
  - Displays dynamic messages (e.g., "You are diabetic" or "You are not diabetic").
  - Plays audio feedback based on the prediction result.
  - Shows an animation during processing.

## Files
- `app.py`: Main application script.
- `Arun.pkl`: Custom-trained machine learning model used for predictions.
- `requirements.txt`: Dependencies required to run the application.

## Usage
1. Launch the app by running:
   ```bash
   streamlit run app.py
   ```
2. Fill in the inputs on the app interface.
3. Click the "Predict" button to see the results.

## Example
1. Input Details:
   - Gender: Male
   - Age: 45
   - Hypertension: Yes
   - Heart Disease: No
   - Smoking History: Never
   - BMI: 27.5
   - HbA1c Level: 6.2
   - Blood Glucose Level: 140
2. Output: The app predicts whether the user is diabetic or not and provides appropriate feedback.

## Model
The app uses a custom-trained machine learning model (`Arun.pkl`) to perform the predictions. The model was trained using scikit-learn on a relevant diabetes dataset.

## Dependencies
- Python 3.7+
- Streamlit
- Numpy
- Scikit-learn
- Pickle

To install dependencies:
```bash
pip install -r requirements.txt
```

## Future Enhancements
- Add more detailed error handling.
- Enhance the user interface with additional visualizations.
- Integrate more advanced machine learning models for improved accuracy.

## License
This project is licensed under the MIT License. See the LICENSE file for details.

## Acknowledgments
- Thanks to the creators of the dataset.
- Inspired by Streamlit's simplicity and versatility.

