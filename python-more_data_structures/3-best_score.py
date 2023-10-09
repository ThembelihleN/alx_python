def best_score(a_dictionary):
    if not a_dictionary:
        return None
    
    highest_score = int("0")
    best_key = None

    for key, value in a_dictionary.items():
        if value > highest_score:
            highest_score = value
            best_key = key

    return best_key