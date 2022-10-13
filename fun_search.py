list_of_phrases = [
    ["кредит", "кредиты", "кридит"],
    ["погасит", "закрыть", "оплатить"],
    ["карта", "карту", "карты", "карт"]
]


def search_word(phrase):
    return all(map(lambda s: any(map(lambda word: word in phrase.lower(), s)), list_of_phrases))
