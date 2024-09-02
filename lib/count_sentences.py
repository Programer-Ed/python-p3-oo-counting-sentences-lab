#!/usr/bin/env python3
import re

class MyString:
    def __init__(self, value=''):
        # Use the setter to handle validation on initialization
        self._value = ''  # Initialize with an empty string
        self.value = value  # This will call the setter

    @property
    def value(self):
        '''Getter for value property.'''
        return self._value

    @value.setter
    def value(self, new_value):
        '''Setter for value property. Validates that new_value is a string.'''
        if not isinstance(new_value, str):
            print("The value must be a string.")
        else:
            self._value = new_value

    def is_sentence(self):
        '''Returns True if the value ends with a period and False otherwise.'''
        return self._value.endswith('.')

    def is_question(self):
        '''Returns True if the value ends with a question mark and False otherwise.'''
        return self._value.endswith('?')

    def is_exclamation(self):
        '''Returns True if the value ends with an exclamation mark and False otherwise.'''
        return self._value.endswith('!')

    def count_sentences(self):
        '''Returns the number of sentences in the value.'''
        # Define sentence-ending punctuation marks.
        punctuation = r'[.!?]'
        # Split the string by sentence-ending punctuation.
        sentences = re.split(punctuation, self._value)
        # Filter out empty strings and strip leading/trailing whitespace.
        sentences = [s.strip() for s in sentences if s.strip()]
        # Return the count of sentences.
        return len(sentences)

      




