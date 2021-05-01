"""Miles to Kilometres Converter"""

from kivy.app import App
from kivy.lang import Builder
from kivy.properties import StringProperty

MILES_TO_KILOMETERS = 1.60934


class MilesConverterApp(App):
    """Kivy App for converting miles to kilometres."""
    output_km = StringProperty()

    def build(self):
        """build application from kv file"""
        self.title = "miles to kilometers conversion tool"
        self.root = Builder.load_file('convert_miles_km.kv')
        return self.root

    def convert_miles_to_kilometers(self, miles):
        """converts miles to kilometers"""
        # print(output_km)
        output_km = miles*MILES_TO_KILOMETERS
        # convert_to_number goes here
        self.root.ids.output_label.text = str(output_km)

    def handle_increment(self, text, change):
        """changes the number by increments of one"""
        # miles = int(text) + int(change)
        miles = int(self.convert_to_number(text)) + int(change)
        self.root.ids.miles.text = str(miles)

    @staticmethod
    def convert_to_number(text):
        """changes invalid input to 0"""
        try:
            return float(text)
        except ValueError:
            return 0.0


MilesConverterApp().run()
