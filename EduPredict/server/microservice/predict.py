"""
Student Performance Prediction Script
Author: [Your Name]
Date: 2025-01-01
Description: Loads a trained model and makes predictions based on student data
"""

import sys
import pandas as pd
import joblib
import os

def load_prediction_model():
    """
    Load the pre-trained student performance prediction model

    Returns:
        model: Loaded trained model
    """
    # Get the directory of the current script
    script_directory = os.path.dirname(os.path.abspath(__file__))

    # Construct path to the model file
    model_file_path = os.path.join(script_directory, 'student_performance_model.joblib')

    # Also try relative path in case script is run from different directory
    if not os.path.exists(model_file_path):
        model_file_path = 'student_performance_model.joblib'

    # Load the trained model
    try:
        trained_model = joblib.load(model_file_path)
        print(f"Model loaded successfully from: {model_file_path}", file=sys.stderr)
        return trained_model
    except FileNotFoundError:
        print(f"Error: Model file not found at {model_file_path}", file=sys.stderr)
        print(f"Current working directory: {os.getcwd()}", file=sys.stderr)
        print(f"Files in current directory: {os.listdir('.')}", file=sys.stderr)
        print(f"Files in script directory: {os.listdir(script_directory)}", file=sys.stderr)
        sys.exit(1)
    except Exception as e:
        print(f"Error loading model: {str(e)}", file=sys.stderr)
        sys.exit(1)

def prepare_input_data(attendance, study_hours, previous_marks, assignment_score):
    """
    Prepare input data in the correct format for prediction

    Args:
        attendance (float): Student attendance percentage
        study_hours (float): Hours studied per day
        previous_marks (float): Previous academic marks
        assignment_score (float): Assignment score

    Returns:
        pandas.DataFrame: Formatted input data
    """
    try:
        # Create a DataFrame with the input parameters
        input_data = pd.DataFrame([[
            float(attendance),
            float(study_hours),
            float(previous_marks),
            float(assignment_score)
        ]], columns=[
            'Attendance (%)',
            'Study Hours per Day',
            'Previous Marks (%)',
            'Assignment Score'
        ])

        return input_data
    except Exception as e:
        print(f"Error preparing input data: {str(e)}", file=sys.stderr)
        sys.exit(1)

def make_prediction(model, input_data):
    """
    Make a prediction using the trained model

    Args:
        model: Loaded trained model
        input_data (pandas.DataFrame): Prepared input data

    Returns:
        str: Prediction result ('Pass' or 'Fail')
    """
    try:
        # Perform prediction
        prediction_result = model.predict(input_data)[0]

        # Convert numerical prediction back to categorical
        return 'Pass' if prediction_result == 1 else 'Fail'
    except Exception as e:
        print(f"Error making prediction: {str(e)}", file=sys.stderr)
        sys.exit(1)

def main():
    """
    Main function to execute the prediction process
    """
    # Validate command line arguments
    if len(sys.argv) != 5:
        print("Usage: python predict.py <attendance> <study_hours> <previous_marks> <assignment_score>")
        print("Example: python predict.py 85.0 4.0 75.0 80.0")
        sys.exit(1)

    try:
        # Extract command line arguments
        attendance = sys.argv[1]
        study_hours = sys.argv[2]
        previous_marks = sys.argv[3]
        assignment_score = sys.argv[4]

        # Load the pre-trained model
        model = load_prediction_model()

        # Prepare input data
        input_features = prepare_input_data(attendance, study_hours, previous_marks, assignment_score)

        # Make prediction
        result = make_prediction(model, input_features)

        # Output the prediction result
        print(result)

    except ValueError as e:
        print(f"Error: Invalid input values. Please provide numeric values. Details: {str(e)}", file=sys.stderr)
        sys.exit(1)
    except Exception as e:
        print(f"An error occurred during prediction: {str(e)}", file=sys.stderr)
        sys.exit(1)

if __name__ == "__main__":
    main()
