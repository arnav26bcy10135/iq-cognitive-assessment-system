from database import get_attempts


def show_attempt_history(participant=None):
    """Display previous test attempts."""
    attempts = get_attempts(participant)

    print("\n" + "=" * 70)
    print("                     ATTEMPT HISTORY")
    print("=" * 70)

    if not attempts:
        print("No previous attempts found.")
        return

    for attempt in attempts:
        attempt_id, name, score, total, percentage, performance, date = attempt

        print(
            f"#{attempt_id} | {name} | "
            f"{score}/{total} | {percentage:.1f}% | "
            f"{performance} | {date}"
        )


def show_statistics(participant=None):
    """Display basic statistics from saved attempts."""
    attempts = get_attempts(participant)

    print("\n" + "=" * 50)
    print("                 STATISTICS")
    print("=" * 50)

    if not attempts:
        print("No test data available.")
        return

    scores = [attempt[4] for attempt in attempts]

    highest = max(scores)
    average = sum(scores) / len(scores)

    print(f"Total Attempts : {len(attempts)}")
    print(f"Highest Score  : {highest:.1f}%")
    print(f"Average Score  : {average:.1f}%")