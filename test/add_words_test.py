import unittest


class Words(object):

    def __init__(self):
        self.Word = []

    def count(self):
        return len(self.Word)

    def add(self, single_word):
        self.Word.append(single_word)

    def return_list(self):
        return self.Word

    def find(self, finding_word):
        if finding_word in self.Word:
            return True
        else:
            return False

    def update(self, find_a_word, change_to):
        if self.find(find_a_word):
            self.Word = list(map(lambda x: x.replace(find_a_word, change_to), self.Word))
            return True
        else:
            return False

    def delete(self, delete_a_word):
        if self.find(delete_a_word):
            self.Word.remove(delete_a_word)
            return True
        else:
            return False


class AddingWordsTest(unittest.TestCase):
    def test_empty_words(self):
        word = Words()
        self.assertEqual(word.count(), 0)

    def test_add_one_word(self):
        word = Words()
        word.add("Prince")
        self.assertEqual(word.count(), 1)

    def test_add_two_word(self):
        word = Words()
        word.add("Prince")
        word.add("Mahesh")
        self.assertEqual(word.count(), 2)

    def test_read_a_word(self):
        word = Words()
        word.add("Prince")
        word.add("Mahesh")
        self.assertTrue(word.find("Mahesh"))
        self.assertFalse(word.find("Kaleja"))

    def test_update_a_word(self):
        word = Words()
        word.add("Prince")
        word.add("Mahesh")
        self.assertTrue(word.update("Prince", "Aaron"))
        self.assertTrue(word.find("Aaron"))

    def test_delete_a_word(self):
        word = Words()
        word.add("Prince")
        word.add("Mahesh")
        self.assertTrue(word.delete("Mahesh"))
        self.assertFalse(word.find("Mahesh"))
