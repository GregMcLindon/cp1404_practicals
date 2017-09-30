"""CP1404 client code to use in the programming language class."""

from prac_07.programming_language import ProgrammingLanguage


def main():
    """Simple programme to test programming language code."""
    ruby = ProgrammingLanguage("Ruby", "Dynamic", True, 1995)
    python = ProgrammingLanguage("Python", "Dynamic", True, 1991)
    visual_basic = ProgrammingLanguage("Visual Basic", "Static", False, 1991)

    print(ruby)
    print(python)
    print(visual_basic)
    languages = [ruby, python, visual_basic]
    # language_display = [language for language in languages if language.is_dynamic()]
    # print(language_display)
    # print("The dynamic languages are:\n:{}\n".format(language_display))

    print("The dynamically typed languages are:")
    for language in languages:
        if language.is_dynamic():
            print(language.name)

main()
