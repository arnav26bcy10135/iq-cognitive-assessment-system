# IQ & Cognitive Assessment System - Design

## 1. System Overview

The IQ & Cognitive Assessment System is a command-line Python application that allows users to complete a short cognitive test and review their performance.

The system uses SQLite to store previous test attempts.

## 2. Main Modules

### main.py
Controls the application menu and connects the different modules.

### questions.py
Stores the question bank and provides questions to the quiz system.

### quiz.py
Randomly selects questions, displays them, accepts answers and records the score.

### scoring.py
Calculates percentages and assigns performance bands.

### database.py
Creates the SQLite database and stores and retrieves test attempts.

### validation.py
Validates participant names and prevents invalid input.

### reports.py
Displays previous attempts and overall statistics.

## 3. Database Design

The system contains an `attempts` table.

| Field | Type | Description |
|---|---|---|
| id | INTEGER | Unique attempt ID |
| participant | TEXT | Participant name |
| score | INTEGER | Number of correct answers |
| total | INTEGER | Total questions |
| percentage | REAL | Test percentage |
| performance | TEXT | Performance category |
| date | TEXT | Date and time of attempt |

## 4. Application Workflow

1. The application starts and initializes the database.
2. The user selects an option from the main menu.
3. For a new test, the participant enters their name.
4. Ten questions are randomly selected.
5. The user answers each question.
6. The score and percentage are calculated.
7. A performance band is generated.
8. The attempt is saved in SQLite.
9. The user can view previous attempts and statistics.

## 5. Validation

The system validates:

- Empty participant names
- Names that are too short
- Names that are too long
- Names containing invalid characters
- Invalid menu choices
- Invalid question answers

## 6. Testing

The project contains seven automated unit tests covering:

- Percentage calculation
- Zero-question handling
- Performance classification
- Category percentage calculation
- Valid names
- Empty names
- Invalid names

All seven tests passed successfully during testing.