import random
from questions import get_questions


def run_quiz():
    """Run a randomized 10-question cognitive test."""
    questions = get_questions()
    selected_questions = random.sample(questions, 10)

    score = 0
    category_results = {}

    print("\n" + "=" * 50)
    print("          IQ & COGNITIVE TEST")
    print("=" * 50)

    for number, question in enumerate(selected_questions, start=1):
        print(f"\nQuestion {number}/10")
        print(f"Category: {question['category']}")
        print(question["question"])

        for index, option in enumerate(question["options"], start=1):
            print(f"{index}. {option}")

        while True:
            try:
                answer = int(input("Your answer (1-4): "))

                if answer not in range(1, 5):
                    print("Please enter a number from 1 to 4.")
                    continue

                break

            except ValueError:
                print("Please enter a valid number.")

        category = question["category"]

        if category not in category_results:
            category_results[category] = {"correct": 0, "total": 0}

        category_results[category]["total"] += 1

        if answer == question["answer"]:
            print("✓ Correct!")
            score += 1
            category_results[category]["correct"] += 1
        else:
            print(f"✗ Incorrect. Correct answer: {question['answer']}")

    percentage = (score / len(selected_questions)) * 100

    print("\n" + "=" * 50)
    print("              TEST COMPLETE")
    print("=" * 50)
    print(f"Score: {score}/{len(selected_questions)}")
    print(f"Percentage: {percentage:.1f}%")

    print("\nCategory Performance:")
    for category, result in category_results.items():
        print(
            f"{category}: "
            f"{result['correct']}/{result['total']}"
        )

    return {
        "score": score,
        "total": len(selected_questions),
        "percentage": percentage,
        "category_results": category_results
    }