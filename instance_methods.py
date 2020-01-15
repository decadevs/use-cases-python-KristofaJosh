# Document at least 3 use cases of instance methods


class RGB:
    """program saves your favourite colour"""
    def __init__(self):
        self.colour = []

    def add_colours(self, new_colour):
        if isinstance(new_colour, list):
            self.colour.extend(new_colour)
        else:
            self.colour.append(new_colour)

    def change_colour(self, old_colour, new_colour):
        try:
            oci = self.colour.index(old_colour)
            self.colour[oci] = new_colour
        except ValueError:
            ans = input(f'"{old_colour}" not found in the list\nAdd "{new_colour}" to list ? Y / N: ').lower()
            if ans == 'y':
                self.add_colours(new_colour)
            else:
                self.show_colours()

    def show_colours(self):
        return self.colour


test = RGB()
print(test.show_colours())
test.change_colour('red', 'blue')
test.add_colours(['black', 'purple', 'green'])
test.change_colour('purple', 'orange')
test.add_colours(['black', 'purple', 'green'])

print(test.show_colours())