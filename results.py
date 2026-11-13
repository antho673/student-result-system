def validate_score(score_str):
    """Validates that a score input is a number between 0 and 100."""
    try:
        score = float(score_str)
        if 0 <= score <= 100:
            return score
        print("Error: Score must be between 0 and 100.")
        return None
    except ValueError:
        print("Error: Please enter a valid numerical score.")
        return None