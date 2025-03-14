# Quiz App

## Introduction
This Quiz App is a simple web application built using Streamlit. It presents users with multiple-choice questions and provides immediate feedback on their answers.

## Features
- Multiple-choice questions
- Immediate feedback with emojis for correct and incorrect answers
- Random question selection

## How to Use
1. **Run the Application**: 
   To start the application, navigate to the project directory and run the following command:
   ```bash
   streamlit run quiz_app.py
   ```

2. **Answer Questions**:
   - The app will display a random question with multiple-choice options.
   - Select the correct answer from the Radio menu.
   - Click the "Submit Answer" button to check your answer.

3. **Feedback**:
   - If the answer is correct, a message with a ✅ emoji will be displayed.
   - If the answer is incorrect, a message with a ❌ emoji will be displayed.

## Developer Guide
### Adding New Questions
To add new questions, update the `questions` list in the `quiz_app.py` file. Each question should be a dictionary with the following keys:
- `question`: The question text.
- `options`: A list of possible answers.
- `answer`: The correct answer.

Example:
```python
questions = [
    {
        "question": "What is the capital of Pakistan?",
        "options": ["Karachi", "Islamabad", "Lahore", "Quetta"],
        "answer": "Islamabad"
    },
    # Add more questions here
]
```

### Dependencies
Ensure you have the following dependencies installed:
- `streamlit`

You can install the required dependencies using:
```bash
pip install streamlit
```

## Conclusion
This Quiz App is a simple yet effective tool for testing knowledge on various topics. Feel free to customize the questions and improve the app as needed.