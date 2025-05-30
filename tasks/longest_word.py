def get_longest_word( s: str) -> str:
    words = s.split()
    longest_word = words[0]

    for word in words:
        if len(word) > len(longest_word):
            longest_word = word

    return longest_word
