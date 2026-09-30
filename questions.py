QUESTIONS = [
    {
        "category": "Number Series",
        "question": "What number comes next: 2, 4, 8, 16, ?",
        "options": ["20", "24", "32", "36"],
        "answer": 3
    },
    {
        "category": "Number Series",
        "question": "What number comes next: 5, 10, 15, 20, ?",
        "options": ["22", "25", "30", "35"],
        "answer": 2
    },
    {
        "category": "Logical Reasoning",
        "question": "If all cats are animals and some animals are black, which statement is definitely true?",
        "options": [
            "All cats are black",
            "Some cats are black",
            "All cats are animals",
            "No cats are black"
        ],
        "answer": 3
    },
    {
        "category": "Pattern Recognition",
        "question": "Which symbol should come next: ▲ ● ▲ ● ▲ ?",
        "options": ["▲", "●", "■", "◆"],
        "answer": 2
    },
    {
        "category": "Number Series",
        "question": "What number comes next: 3, 6, 12, 24, ?",
        "options": ["36", "42", "48", "54"],
        "answer": 3
    },
    {
        "category": "Logical Reasoning",
        "question": "A clock shows 3:00. What is the angle between the hour and minute hands?",
        "options": ["45°", "90°", "120°", "180°"],
        "answer": 2
    },
    {
        "category": "Verbal Reasoning",
        "question": "Which word does not belong with the others?",
        "options": ["Apple", "Mango", "Carrot", "Banana"],
        "answer": 3
    },
    {
        "category": "Pattern Recognition",
        "question": "If A = 1, B = 2, C = 3, what is the value of CAB?",
        "options": ["5", "6", "7", "8"],
        "answer": 2
    },
    {
        "category": "Logical Reasoning",
        "question": "If today is Monday, what day will it be after 10 days?",
        "options": ["Wednesday", "Thursday", "Friday", "Saturday"],
        "answer": 2
    },
    {
        "category": "Number Series",
        "question": "What number is missing: 1, 4, 9, 16, ?",
        "options": ["20", "24", "25", "30"],
        "answer": 3
    },
    {
        "category": "Verbal Reasoning",
        "question": "Book is to Reading as Fork is to:",
        "options": ["Cooking", "Eating", "Writing", "Cutting"],
        "answer": 2
    },
    {
        "category": "Pattern Recognition",
        "question": "Which number is different from the others?",
        "options": ["9", "16", "25", "30"],
        "answer": 4
    }
]


def get_questions():
    """Return the complete question bank."""
    return QUESTIONS.copy()