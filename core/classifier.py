from core.scoring import calculate_score


def classify_program(program):

    score = calculate_score(program)

    if score <= 3:
        return "Beginner"

    elif score <= 6:
        return "Intermediate"

    elif score <= 9:
        return "Advanced"

    return "Expert"
