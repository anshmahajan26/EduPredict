"""
Student Performance Prediction Model Training Script
Author: [Your Name]
Date: 2025-01-01
Description: Trains a machine learning model to predict student performance outcomes
"""

import pandas as pd
import numpy as np
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestClassifier
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import accuracy_score, classification_report, confusion_matrix
from sklearn.preprocessing import StandardScaler
import joblib
import os

def load_student_data(filepath):
    """
    Load student performance data from CSV file
    
    Args:
        filepath (str): Path to the dataset file
    
    Returns:
        pandas.DataFrame: Loaded dataset
    """
    if not os.path.exists(filepath):
        raise FileNotFoundError(f"Dataset not found at {filepath}")
    
    dataset = pd.read_csv(filepath)
    print(f"Dataset loaded successfully with {len(dataset)} records")
    return dataset

def preprocess_data(dataset):
    """
    Preprocess the data for model training
    
    Args:
        dataset (pandas.DataFrame): Raw dataset
    
    Returns:
        tuple: Features (X) and target variable (y)
    """
    # Convert categorical result to numerical values (Pass=1, Fail=0)
    dataset['Result'] = dataset['Result'].map({'Pass': 1, 'Fail': 0})
    
    # Separate features and target
    feature_names = ['Attendance (%)', 'Study Hours per Day', 'Previous Marks (%)', 'Assignment Score']
    X = dataset[feature_names]  # Features
    y = dataset['Result']       # Target variable
    
    # Optional: Scale features for better performance
    scaler = StandardScaler()
    X_scaled = scaler.fit_transform(X)
    X_scaled = pd.DataFrame(X_scaled, columns=feature_names)
    
    return X_scaled, y

def train_prediction_model(X, y):
    """
    Train the student performance prediction model
    
    Args:
        X (pandas.DataFrame): Features dataset
        y (pandas.Series): Target variable
    
    Returns:
        model: Trained machine learning model
    """
    # Split the dataset into training and testing sets
    X_train, X_test, y_train, y_test = train_test_split(
        X, y, test_size=0.25, random_state=42, stratify=y
    )
    
    # Initialize the model with improved parameters
    # Using Random Forest to improve prediction accuracy
    model = RandomForestClassifier(
        n_estimators=200, 
        max_depth=10, 
        min_samples_split=5, 
        min_samples_leaf=2,
        random_state=42
    )
    
    # Train the model
    model.fit(X_train, y_train)
    
    # Make predictions on the test set
    predictions = model.predict(X_test)
    
    # Evaluate model performance
    accuracy = accuracy_score(y_test, predictions)
    print(f"Model Performance:")
    print(f"  Accuracy: {accuracy * 100:.2f}%")
    print(f"  Classification Report:")
    print(classification_report(y_test, predictions, target_names=['Fail', 'Pass']))
    
    # Feature importance analysis
    feature_names = X.columns
    feature_importance = model.feature_importances_
    
    print(f"\nFeature Importance:")
    for feature, importance in zip(feature_names, feature_importance):
        print(f"  {feature}: {importance:.4f}")
    
    return model

def save_model(model, model_path):
    """
    Save the trained model to a file for later use
    
    Args:
        model: Trained machine learning model
        model_path (str): File path to save the model
    """
    joblib.dump(model, model_path)
    print(f"\nModel saved successfully to: {model_path}")

def main():
    """
    Main execution function for the model training process
    """
    print("Starting Student Performance Prediction Model Training")
    print("="*55)
    
    try:
        # Load dataset
        dataset = load_student_data("./student_performance_dataset.csv")
        
        # Preprocess data
        X, y = preprocess_data(dataset)
        
        # Train the model
        trained_model = train_prediction_model(X, y)
        
        # Save the trained model
        save_model(trained_model, './student_performance_model.joblib')
        
        print("\nModel training process completed successfully!")
        
    except Exception as e:
        print(f"An error occurred during model training: {str(e)}")

if __name__ == "__main__":
    main()
