from .base import FunctionalTest
from unittest import skip

class ItemValidationTest(FunctionalTest):

    def test_cannot_add_empty_list_items(self):
        # Edith goes to the home page and accidently  ttries to submit an empty
        # list item. She hits enter on the empty input box.

        # The home page refreshes, and there is an error message saying thata
        # the list item cannot be blank

        # She tries again for the item, which now works

        # Perversely, she now decides to enter a second blank list item

        # She recieves a similar warning on the list pag

        # And she can correct it by filling in some text
        self.fail('Write me!')
