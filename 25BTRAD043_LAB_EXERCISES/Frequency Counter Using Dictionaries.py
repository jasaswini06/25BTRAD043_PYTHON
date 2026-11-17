import string


def count_word_frequency(text):
    # Remove punctuation and normalize to lowercase
    cleaned_text = text.translate(str.maketrans("", "", string.punctuation)).lower()
    words = cleaned_text.split()

    frequency = {}
    for word in words:
        frequency[word] = frequency.get(word, 0) + 1

    return frequency


def count_element_frequency(elements):
    frequency = {}
    for item in elements:
        item = item.strip()
        frequency[item] = frequency.get(item, 0) + 1
    return frequency


def main():
    print("--- FREQUENCY COUNTER ---")
    print("1. Count word frequency in a sentence")
    print("2. Count element frequency in a custom list/survey responses")
    choice = input("Enter choice (1/2): ").strip()

    if choice == "1":
        sentence = input("\nEnter a sentence:\n")
        freq = count_word_frequency(sentence)
        print("\n" + "-" * 30)
        print(f"{'Word':<18} {'Frequency':<10}")
        print("-" * 30)
        for word, count in sorted(freq.items()):
            print(f"{word:<18} {count:<10}")
        print("-" * 30)

    elif choice == "2":
        raw_items = input(
            "\nEnter items/feedback separated by commas (e.g. Good, Poor, Good, Average):\n"
        )
        items = raw_items.split(",")
        freq = count_element_frequency(items)
        print("\n" + "-" * 30)
        print(f"{'Item':<18} {'Count':<10}")
        print("-" * 30)
        for item, count in sorted(freq.items()):
            print(f"{item:<18} {count:<10}")
        print("-" * 30)

    else:
        print("Invalid choice.")


if __name__ == "__main__":
    main()