from database import initialize_database, save_attempt
from quiz import run_quiz
from scoring import get_performance_band
from reports import show_attempt_history, show_statistics
from validation import get_valid_name


def start_test():
    """Start a new cognitive assessment."""
    participant = get_valid_name()

    result = run_quiz()

    performance = get_performance_band(result["percentage"])

    save_attempt(
        participant,
        result["score"],
        result["total"],
        result["percentage"],
        performance
    )

    print("\n" + "=" * 50)
    print("                 FINAL RESULT")
    print("=" * 50)
    print(f"Participant : {participant}")
    print(f"Score       : {result['score']}/{result['total']}")
    print(f"Percentage  : {result['percentage']:.1f}%")
    print(f"Performance : {performance}")
    print("\nYour attempt has been saved.")


def main():
    """Display the main application menu."""
    initialize_database()

    while True:
        print("\n" + "=" * 50)
        print("       IQ & COGNITIVE ASSESSMENT SYSTEM")
        print("=" * 50)
        print("1. Start New Test")
        print("2. View Attempt History")
        print("3. View Statistics")
        print("4. Exit")

        choice = input("\nEnter your choice: ").strip()

        if choice == "1":
            start_test()

        elif choice == "2":
            show_attempt_history()

        elif choice == "3":
            show_statistics()

        elif choice == "4":
            print("\nThank you for using the system!")
            break

        else:
            print("Invalid choice. Please enter 1, 2, 3, or 4.")


if __name__ == "__main__":
    main()