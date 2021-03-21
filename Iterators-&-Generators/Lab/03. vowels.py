class vowels:
    __VOWELS = ["A", "a", "E", "e",
              "I", "i", "O", "o",
              "U", "u", "Y", "y"]

    def __init__(self, text):
        self.text = text
        self.start = 0

    @staticmethod
    def is_vowel(char):
        return char in vowels.__VOWELS

    def __iter__(self):
        return self

    def __next__(self):
        index = self.start
        if index > len(self.text) - 1:
            raise StopIteration
        char = self.text[index]
        self.start += 1
        if not self.is_vowel(char):
            return self.__next__()
        return char

# test code
my_string = vowels('Abcedifuty0o')
for char in my_string:
    print(char)
