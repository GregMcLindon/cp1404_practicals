"""
CP1404 Practical
Kivy GUI program to convert miles to kilometers
"""

from kivy.app import App
from kivy.lang import Builder
from kivy.core.window import Window

__author__ = 'Greg McLindon'

CONVERSION_FACTOR = 1.6093235294117647058823529411765


class MilesToKilometers(App):
    """ MilesToKilometers is a Kivy App for converting miles to kilometers"""
    def build(self):
        """ build the Kivy app from the kv file """
        Window.size = (500, 250)
        self.title = "Convert Miles to Kilometres"
        self.root = Builder.load_file('miles_converter.kv')
        return self.root

    def handle_calculate(self, value):
        """ handle calculation (could be button press or other call), output result to label widget """
        result = "{:.3f}".format(float(value) * CONVERSION_FACTOR)
        self.root.ids.output_label.text = result

MilesToKilometers().run()
