"""CP1404 Practical week 5: look up color codes"""

color_names = {"AliceBlue": "#f0f8ff", "AntiqueWhite1": "#ffefdb", "azure4": "#838b8b", "beige": "#f5f5dc",
               "bisque1": "#ffe4c4", "bisque2": "#eed5b7", "bisque3": "#cdb79e", "bisque4": "#8b7d6b",
               "black": "#000000", "BlanchedAlmond": "#ffebcd", "cyan1": "#00ffff", "cyan2": "#00eeee",
               "cyan3": "#00cdcd", "cyan4": "#008b8b", "DarkGoldenrod": "#b8860b", "DarkGoldenrod1": "#ffb90f",
               "DarkGoldenrod2": "#eead0e"}
color_name = input("Enter color name: ")
while color_name!="":
    print(color_names[color_name])
    color_name = input("Enter color name: ")
