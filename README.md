# Health Index GUI

## Overview
This Streamlit application provides a comprehensive health index assessment tool that evaluates various health parameters and generates a health status based on predefined thresholds.

## Features
- Interactive GUI for health parameter input
- Real-time health status evaluation
- Multiple health metrics tracking
- Range-based health assessment
- Visual warnings for out-of-range parameters

## Health Parameters Tracked
1. Cholesterol
2. Glucose
3. Hemoglobin
4. BMI
5. Systolic Blood Pressure
6. Diastolic Blood Pressure
7. Additional custom parameters (a, b, c, d)

## Health Status Categories
- Extremely Good Health
- Good Health
- Average Health
- Poor Health
- Extremely Poor Health
- Insufficient Data

## Technical Details
- **Language**: Python
- **Framework**: Streamlit
- **Dependencies**: 
  - streamlit
  - pandas (implied)

## Installation

### Prerequisites
- Python 3.7+
- pip package manager

### Setup
1. Clone the repository
2. Create a virtual environment (optional but recommended)
3. Install dependencies:
```bash
pip install streamlit
```

## Usage
1. Run the Streamlit application:
```bash
streamlit run health_index_gui.py
```
2. Input your health parameters in the form
3. Click 'Submit' to get your health index
4. Review the health status and parameter ranges

## Customization
- Adjust `poor_health_threshold` and `average_health_threshold` in the `fitness_index_MT_model2()` function to modify health status criteria
- Modify parameter limits in the `parameter_limits` dictionary

## Input Guidelines
- Enter numeric values for each health parameter
- Zero (0.0) indicates no data provided
- Values outside specified ranges will trigger warnings

## Limitations
- Requires manual input of all parameters
- Uses predefined static thresholds
- Not a substitute for professional medical advice

## Future Improvements
- Add data persistence
- Implement more sophisticated health scoring
- Create visualization of health metrics
- Add export functionality

## Disclaimer
This tool is for educational purposes only and should not replace professional medical consultation.
