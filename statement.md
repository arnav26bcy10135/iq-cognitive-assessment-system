# Project Statement

## Project Title

IQ & Cognitive Assessment System

## Problem Statement

Many simple quiz applications provide questions and scores but do not provide structured performance tracking or attempt history.

The IQ & Cognitive Assessment System is designed as a command-line Python application that provides a short educational cognitive quiz. It allows users to answer randomized multiple-choice questions, receive a score and performance classification, and review previous attempts stored in a database.

The application is intended for educational and programming purposes and is not a professionally validated IQ assessment.

## Objectives

The main objectives of the project are:

1. To develop a modular Python-based cognitive quiz application.
2. To provide questions from multiple reasoning categories.
3. To randomly select questions for each test attempt.
4. To calculate scores and percentages automatically.
5. To classify performance based on the obtained percentage.
6. To store completed attempts using SQLite.
7. To provide attempt history and basic statistics.
8. To validate user input and handle invalid entries.
9. To demonstrate software testing using Python's unittest framework.

## Functional Requirements

### FR1 - Start Test
The system shall allow a participant to start a new cognitive test.

### FR2 - Question Selection
The system shall randomly select ten questions from the available question bank.

### FR3 - Answer Questions
The system shall display multiple-choice questions and accept answers from the participant.

### FR4 - Score Calculation
The system shall calculate the participant's score and percentage after completing the test.

### FR5 - Performance Classification
The system shall assign a performance band based on the participant's percentage.

### FR6 - Store Results
The system shall save completed test attempts in an SQLite database.

### FR7 - View History
The system shall allow users to view previously stored test attempts.

### FR8 - View Statistics
The system shall display basic statistics such as total attempts, highest percentage and average percentage.

### FR9 - Input Validation
The system shall validate participant names and question answers.

## Non-Functional Requirements

### NFR1 - Usability
The application should provide a simple command-line interface that is easy to understand.

### NFR2 - Reliability
The application should handle invalid inputs without terminating unexpectedly.

### NFR3 - Maintainability
The application should be divided into separate modules so that individual components can be modified independently.

### NFR4 - Performance
The application should process questions, scoring and database operations quickly for normal usage.

### NFR5 - Data Persistence
Completed test attempts should remain available after the application is closed.

### NFR6 - Testability
Important application logic should be testable using automated unit tests.

## Scope

The current system includes:

- Multiple-choice cognitive questions
- Four question categories
- Random question selection
- Score and percentage calculation
- Performance classification
- SQLite database storage
- Attempt history
- Basic statistics
- Input validation
- Automated unit tests

The project does not attempt to provide a clinically or professionally validated measurement of intelligence.

## Technology Stack

- Python 3
- SQLite
- Python unittest
- Git and GitHub
- Visual Studio Code

## Expected Outcome

The completed system should provide a functional command-line cognitive quiz where a participant can complete a test, receive a performance result, and access previously stored attempt information.