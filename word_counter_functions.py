"""
Word Counter Program
Handles user input and counts the number of words in a sentence.
"""

def get_sentence_input() -> str:
    """Prompts the user to enter a sentence and returns it as a string."""
    return input("Enter a sentence: ").strip()

def count_words(sentence: str) -> int:
    """Counts the number of words in a given sentence."""
    return len(sentence.split())

if __name__ == "__main__":
    sentence = get_sentence_input()
    word_count = count_words(sentence)
    print(f"The sentence has {word_count} word{'s' if word_count != 1 else ''}.")
