class ProgrammingLanguage:
    """CP1403 programming language class."""

    def __init__(self, name: str="", typing: str="", reflection: bool=False, year: int="0000"):
        """initialise a language type"""
        self.name = name
        self.typing = typing
        self.reflection = reflection
        self.year = year

    def is_dynamic(self):
        """returns True if programming language is dynamic (as opposed to static)"""
        return self.typing == "Dynamic"

    def __str__(self):
        """Used for printing programming language details"""
        return "{}, {} Typing, Reflection={}, First appeared in {}".format(
            self.name, self.typing, self.reflection, self.year)
