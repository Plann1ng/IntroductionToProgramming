from dataclasses import dataclass


@dataclass
class MultiDisplay:

    # Function which will take string part of the class
    def set_message(self, word):
        self.message = word

    # Function which will take integer part of the class
    def set_count(self, number):
        self.count = number
