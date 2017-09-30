"""
CP1404 Practical
Kivy GUI program to add list of names to a label
"""

from kivy.app import App
from kivy.lang import Builder
from kivy.core.window import Window
from kivy.uix.button import Label

__author__ = 'Greg McLindon'

NAME_LABELS = ("Greg", "John", "Michael", "Peter")


class NameLabels(App):
    """ NameLabels is a Kivy App for displaying names as labels"""
    def build(self):
        """ build the Kivy app from the kv file """
        Window.size = (500, 250)
        self.title = "Display names as labels"
        self.root = Builder.load_file('label_add.kv')
        self.create_widgets()
        return self.root

    def create_widgets(self):
        """
        Create labels from dictionary entries and add them to the GUI
        :return: None
        """
        for name in NAME_LABELS:
            # create a label for each name entry
            temp_label = Label(text=name)
            self.root.ids.entriesBox.add_widget(temp_label)

NameLabels().run()
