def count_words(filepath, words_list):
    with open(filepath) as file:
        text = file.read()
    n = 0
    for word in text.split():
        if word.lower() in words_list:
            n += 1
    return n