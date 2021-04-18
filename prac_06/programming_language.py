class ProgrammingLanguage:
    """represent type of code"""
    def __init__(self, name, typing, reflection, year):
        """shows information about current programing language"""
        self.name = name
        self.typing = typing
        self.reflection = reflection
        self.year = year

    def __str__(self):
        """returns string"""
        return f"{self.name}, {self.typing} Typing, Reflection={self.reflection}, First appeared in {self.year}"

    def is_dynamic(self):
        """determines if language is dynamic"""
        return self.typing == "Dynamic"
