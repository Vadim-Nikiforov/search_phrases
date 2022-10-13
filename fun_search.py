list_of_phrases = [
    ["a деньги", "100% кэш", "aденьги", "мкк"]
]


def search_word(phrase):
    return all(map(lambda s: any(map(lambda word: word in phrase.lower(), s)), list_of_phrases))
