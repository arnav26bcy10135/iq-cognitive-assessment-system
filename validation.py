def validate_name(name):
    """Validate the participant name."""
    name = name.strip()

    if not name:
        return False, "Name cannot be empty."

    if len(name) < 2:
        return False, "Name must contain at least 2 characters."

    if len(name) > 50:
        return False, "Name is too long."

    if not all(character.isalpha() or character.isspace() for character in name):
        return False, "Name should contain letters and spaces only."

    return True, name


def get_valid_name():
    """Keep asking until a valid participant name is entered."""
    while True:
        name = input("Enter participant name: ")
        valid, result = validate_name(name)

        if valid:
            return result

        print(f"Invalid name: {result}")