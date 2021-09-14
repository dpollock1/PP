import unittest
import sentence


class testSentence(unittest.TestCase):

    def test_capital(self):
        # First Capital letter testing
        self.assertEqual(sentence.sentence_validate("The quick brown fox said hello Mr lazy dog."), True)
        self.assertEqual(sentence.sentence_validate("the quick brown fox said hello Mr lazy dog."), False)

    def test_period_end(self):
        # Test for period at the end of the sentence
        self.assertEqual(sentence.sentence_validate("The quick brown fox said hello Mr lazy dog."), True)
        self.assertEqual(sentence.sentence_validate("the quick brown fox said hello Mr lazy dog"), False)

    def test_period_middle(self):
        # Test a period isn't contained in middle.
        self.assertEqual(sentence.sentence_validate("The quick brown fox said hello Mr lazy dog."), True)
        self.assertEqual(sentence.sentence_validate("the quick brown fox said .hello Mr lazy dog."), False)

    def test_even_quotations(self):
        # Test that quotations are closed correctly.
        self.assertEqual(sentence.sentence_validate("The quick brown fox said \"hello Mr lazy dog\"."), True)
        self.assertEqual(sentence.sentence_validate("the quick brown fox said \"hello Mr lazy dog."), False)

    def test_numbers_spelled(self):
        # Test that numbers below 13 are spelled out
        self.assertEqual(sentence.sentence_validate("One lazy dog is too few, 13 is too many."), True)
        self.assertEqual(sentence.sentence_validate("One lazy dog is too few, thirteen is too many."), True)
        self.assertEqual(sentence.sentence_validate("One lazy dog is too few, 12 is too many."), False)
        self.assertEqual(sentence.sentence_validate("One lazy dog is too few, twelve is too many."), True)


if __name__ == '__main__':
    unittest.main()
