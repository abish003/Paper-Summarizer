#remove transition sentence.
import extractor
from sys import argv


def print_usage():
    # Display the parameters and what they mean.
    print('''
    Usage:
        filter.py <article.txt>
    ''')


def get_transition_phrases():
    lines = open("word_lists/transition_phrases.txt").readlines()
    result = []
    for line in lines:
        result.append(line.lstrip().rstrip())
    return result


def is_transition_phrase(transition_phrases, sentence):
    lower = sentence.lower()
    for phrase in transition_phrases:
        if lower.startswith(phrase):
            return True
    return False



def omit_transition_sentences(sentences):
    transition_phrases = get_transition_phrases()
    result = []
    for sentence in sentences:
        if not is_transition_phrase(transition_phrases, sentence):
            result.append(sentence)
    return result


if __name__ == "__main__":
    if len(argv) == 2:
        transition_phrases = get_transition_phrases()
        sentences = extractor.get_sentences(argv[1])
        count = 0
        for sentence in sentences:
            for phrase in transition_phrases:
                lower = sentence.lower()
                if lower.startswith(phrase):
                    print("Omitted: " + sentence)
                    count += 1
                    break
        print("Omitted", count, "sentence(s).")
    else:
        print_usage()
