class Cookie:
    """Cookie class."""

    def __init__(self, color):
        self.color = color

    def get_color(self):
        """Returns the color of cookie."""
        return self.color

    def set_color(self, color):
        """Sets the color of cookie."""
        self.color = color


cookie_green = Cookie("green")
cookie_blue = Cookie("blue")

print("cookie one is ", cookie_green.get_color(), "color")
print("cookie two is ", cookie_blue.get_color(), "color")

cookie_green.set_color("red")

print("cookie one is ", cookie_green.get_color(), "color")
print("cookie two is ", cookie_blue.get_color(), "color")
