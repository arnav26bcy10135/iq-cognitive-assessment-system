import sqlite3
from datetime import datetime

DB_NAME = "iq_test.db"


def connect():
    """Create and return a database connection."""
    return sqlite3.connect(DB_NAME)


def initialize_database():
    """Create the attempts table if it does not exist."""
    connection = connect()

    connection.execute("""
        CREATE TABLE IF NOT EXISTS attempts (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            participant TEXT NOT NULL,
            score INTEGER NOT NULL,
            total INTEGER NOT NULL,
            percentage REAL NOT NULL,
            performance TEXT NOT NULL,
            date TEXT NOT NULL
        )
    """)

    connection.commit()
    connection.close()


def save_attempt(participant, score, total, percentage, performance):
    """Save a completed test attempt."""
    connection = connect()

    connection.execute("""
        INSERT INTO attempts
        (participant, score, total, percentage, performance, date)
        VALUES (?, ?, ?, ?, ?, ?)
    """, (
        participant,
        score,
        total,
        percentage,
        performance,
        datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    ))

    connection.commit()
    connection.close()


def get_attempts(participant=None):
    """Return saved attempts, optionally filtered by participant."""
    connection = connect()

    if participant:
        cursor = connection.execute("""
            SELECT id, participant, score, total,
                   percentage, performance, date
            FROM attempts
            WHERE participant = ?
            ORDER BY id DESC
        """, (participant,))
    else:
        cursor = connection.execute("""
            SELECT id, participant, score, total,
                   percentage, performance, date
            FROM attempts
            ORDER BY id DESC
        """)

    attempts = cursor.fetchall()
    connection.close()

    return attempts