def main():
    book_path = "books/frankenstein.txt"
    text = get_book_text(book_path)
    num_words = get_num_words(text)
    print(f"{num_words} words found in the document")

    dict_count = letter_count(text)
    sorted_char_freq = dict(
        sorted(dict_count.items(), key=lambda item: item[1], reverse=True)
    )
    for key in sorted_char_freq:
        print(f"The '{key}' character was found {sorted_char_freq[key]} times.")


def get_num_words(text):
    words = text.split()
    return len(words)


def get_book_text(path):
    with open(path) as f:
        return f.read()


def letter_count(text):
    letter_counts = {}
    for char in text.lower():
        if char.isalpha():
            letter_counts[char] = letter_counts.get(char, 0) + 1
    return letter_counts


main()
