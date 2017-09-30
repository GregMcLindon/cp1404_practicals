"""CP1404 Practical week 5: look up color codes"""

color_dict = {"AliceBlue": "#f0f8ff", "AntiqueWhite1": "#ffefdb", "azure4": "#838b8b", "beige": "#f5f5dc",
               "bisque1": "#ffe4c4", "bisque2": "#eed5b7", "bisque3": "#cdb79e", "bisque4": "#8b7d6b",
               "black": "#000000", "BlanchedAlmond": "#ffebcd", "cyan1": "#00ffff", "cyan2": "#00eeee",
               "cyan3": "#00cdcd", "cyan4": "#008b8b", "DarkGoldenrod": "#b8860b", "DarkGoldenrod1": "#ffb90f",
               "DarkGoldenrod2": "#eead0e"}
color_search = input("Enter color name: ")
while color_search != "":
    try:
        print(color_dict[color_search])
    except:
        print("Enter valid name from following list:")
        for color in sorted(color_dict):
            print("{:5}{}".format("", color))
    color_search = input("Enter color name: ")
