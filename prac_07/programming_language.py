class ProgrammingLanguage:
    """CP1403 programming language class"""

    def __init__(self, name: str = "", typing: str = "", reflection: bool = False, year: int = "0000"):
        """initialise a language type

        Reflection: boolean, False = 'No', True = 'Yes'
        """
        self.name = name
        self.typing = typing
        self.reflection = reflection
        self.year = year

    def __is_dynamic__(self):
        """returns True if programming language is dynamic (as opposed to static)"""
        return "{}".format(True if self.typing == "Dynamic" else False)

    def __str__(self):
        """Used for printing programming language details"""
        return "{}, {}, Reflection={}, First appeared in {}".format(self.name, "Dynamic Typing" if self.__is_dynamic__()
        else "Static Typing", self.reflection, self.year)
