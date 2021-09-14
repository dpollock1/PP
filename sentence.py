"""
Requests a user defined string which is validated against a set of rules.
Determines whether the sentence is valid or not.
"""


def check_even(num):
    # Returns True if even
    if (num % 2) == 0:
        return True
    else:
        return False


def search(sentence):
    # Check that numbers below 13 are spelled.
    # splits words by space and compares each string list to forbidden string list.
    numbers = ["1", "2", "3", "4", "5", "6", "7", "8", "9", "10", "11", "12"]
    for x in numbers:
        for y in sentence.split(" "):
            if x == y:
                return False
    return True


def sentence_validate(sentence):
    # This function returns true if all checks are met.
    if sentence[0].isupper() and \
            check_even(sentence.count('\"')) and \
            sentence[-1] == "." and \
            sentence[:-1].find(".") == -1 and \
            search(sentence[:-1]):
        return True
    else:
        return False


def main():
    # main function requests user input and executes program. True indicates valid sentence.
    sentence = input("Sentence: ")
    if sentence_validate(sentence) == True:
        return "Sentence is valid"
    else:
        return "Sentence is not valid"


if __name__ == '__main__':
    print(main())

