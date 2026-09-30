def calculate_percentage(score, total):
    """Calculate the test percentage."""
    if total <= 0:
        return 0.0

    return (score / total) * 100


def get_performance_band(percentage):
    """Return a performance band based on the test percentage."""
    if percentage >= 90:
        return "Excellent"
    elif percentage >= 75:
        return "Strong"
    elif percentage >= 60:
        return "Good"
    elif percentage >= 40:
        return "Average"
    else:
        return "Needs Improvement"


def calculate_category_percentages(category_results):
    """Calculate percentages for each question category."""
    results = {}

    for category, data in category_results.items():
        total = data["total"]
        correct = data["correct"]

        if total == 0:
            results[category] = 0.0
        else:
            results[category] = (correct / total) * 100

    return results