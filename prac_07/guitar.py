class Guitar:
    """CP1403 guitar types class."""

    def __init__(self, name: str="", year: int=0, cost: float=0, current_year: int=0):
        """initialise a guitar type"""
        self.name = name
        self.year = year
        self.cost = cost
        self.current_year = current_year

    def __str__(self):
        """Used for printing guitar details"""
        return "{} ({}) : ${:.2f}".format(
            self.name, self.year, self.cost)

    def get_age(self)->int:
        """calculate age of guitar relative to the current_year input parameter"""
        return self.current_year - self.year

    def is_vintage(self)->bool:
        """returns True if age of guitar is greater than 50"""
        return self.get_age() > 50
