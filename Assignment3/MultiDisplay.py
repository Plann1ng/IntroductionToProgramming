from dataclasses import dataclass


@dataclass
class MultiDisplay:

    # Function which will take string part of the class
    def set_message(self, word):
        self.message = word

    # Function which will take integer part of the class
    def set_count(self, number):
        self.count = number
    # Returns the string provided
    def get_message(self):
        return self.message

    # Returns the integer provided
    def get_count(self):
        return self.count

    # Returns the string "x" times while everytime it
    # being printed onto a new line
    def display(self):
        return print(('\n' + self.message) * self.count)

    # Takes string and integer and returns "x" times the string.
    # Each time will be printed onto a new line
    def set_display(self, word, number):
        self.message = word
        self.count = number
        return print(('\n'+word) * number)