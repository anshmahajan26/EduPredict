"""
Student Performance Dataset Generator
Author: [Your Name]
Date: 2025-01-01
Description: Creates synthetic student performance data with realistic relationships between variables
"""

import pandas as pd
import numpy as np
import random

def calculate_student_outcome(attendance, study_hours, previous_marks, assignment_score):
    """
    Calculate student outcome based on academic factors with realistic weights
    
    Args:
        attendance (int): Attendance percentage
        study_hours (float): Hours studied per day
        previous_marks (int): Previous academic performance
        assignment_score (int): Assignment completion score
    
    Returns:
        str: 'Pass' or 'Fail' outcome
    """
    # Calculate weighted performance score
    # Attendance contributes 20%, study hours 30%, previous marks 30%, assignment score 20%
    performance_score = (
        (attendance * 0.20) +
        (study_hours * 10 * 0.30) +  # Scale study hours appropriately
        (previous_marks * 0.30) +
        (assignment_score * 0.20)
    )
    
    # Apply a threshold for passing with slight randomness for realism
    passing_threshold = 75  # Lower than previous 100 for more realistic pass rate
    outcome_probability = (performance_score - 50) / 100  # Normalize to 0-1 range
    
    # Add some randomness to simulate real-world variations
    outcome_probability = max(0.1, min(0.9, outcome_probability + random.uniform(-0.1, 0.1)))
    
    return 'Pass' if random.random() < outcome_probability else 'Fail'

def create_synthetic_dataset(num_students=1000):
    """
    Generate a synthetic dataset of student records
    
    Args:
        num_students (int): Number of student records to generate
    
    Returns:
        pandas.DataFrame: Dataset with student information and outcomes
    """
    student_records = []
    
    for student_id in range(1, num_students + 1):
        # Generate realistic student characteristics
        attendance = random.randint(40, 100)  # Attendance percentage (40-100%)
        study_hours = round(random.uniform(0.5, 8), 1)  # Study hours (0.5-8 hours)
        previous_marks = random.randint(30, 100)  # Previous academic performance
        assignment_score = random.randint(30, 100)  # Assignment performance score
        
        # Determine academic outcome
        academic_result = calculate_student_outcome(attendance, study_hours, previous_marks, assignment_score)
        
        # Add record to the dataset
        student_records.append({
            'StudentID': f'STU{student_id:04d}',  # Added ID for better tracking
            'Attendance (%)': attendance,
            'Study Hours per Day': study_hours,
            'Previous Marks (%)': previous_marks,
            'Assignment Score': assignment_score,
            'Result': academic_result
        })
    
    return pd.DataFrame(student_records)

def main():
    """
    Main execution function for dataset generation
    """
    print("Generating synthetic student performance dataset...")
    print("Creating 1000 student records with realistic academic relationships")
    
    # Generate the dataset
    student_dataset = create_synthetic_dataset(1000)
    
    # Display summary statistics
    print(f"\nDataset created with {len(student_dataset)} records")
    print("\nFirst 5 records:")
    print(student_dataset.head())
    
    print(f"\nResult distribution:")
    print(student_dataset['Result'].value_counts())
    
    # Save the dataset to CSV
    output_filename = 'student_performance_dataset.csv'
    student_dataset.to_csv(output_filename, index=False)
    print(f"\nDataset saved as '{output_filename}'")
    
    print("Dataset generation completed successfully!")

if __name__ == "__main__":
    main()
