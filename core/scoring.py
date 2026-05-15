def calculate_score(program):

    score = 0

    if program.get("mobile"):
        score += 2

    if program.get("graphql"):
        score += 2

    if program.get("waf"):
        score += 2

    if "*" in program.get("scope", ""):
        score += 3

    return score
