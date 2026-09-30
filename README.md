# IQ & Cognitive Assessment System

## Project Overview

The IQ & Cognitive Assessment System is a command-line Python application designed to provide a short educational cognitive quiz and record user performance.

The system presents randomized multiple-choice questions from different categories including:

- Number Series
- Logical Reasoning
- Pattern Recognition
- Verbal Reasoning

After completing the test, the application calculates the score and percentage, assigns a performance band, and stores the attempt in an SQLite database.

> **Note:** This project is an educational quiz system and is not a professionally or clinically validated IQ assessment.

---

## Features

- Randomized cognitive questions
- Multiple-choice questions
- Number series questions
- Logical reasoning questions
- Pattern recognition questions
- Verbal reasoning questions
- Automatic score calculation
- Percentage calculation
- Performance classification
- SQLite attempt history
- Statistics for previous attempts
- Participant name validation
- Invalid input handling
- Automated unit testing

---

## Technologies Used

- Python 3
- SQLite
- Python `unittest`
- Git
- GitHub
- Visual Studio Code

---

## Project Structure

```text
iq-cognitive-assessment-system/
│
├── main.py
├── database.py
├── questions.py
├── quiz.py
├── scoring.py
├── reports.py
├── validation.py
├── statement.md
├── README.md
│
├── tests/
│   └── test_iq_tester.py
│
└── docs/
    └── design.md