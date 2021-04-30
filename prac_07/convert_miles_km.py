"""Miles to Kilometres Converter"""

from kivy.app import App
from kivy.lang import Builder
from kivy.properties import StringProperty

MILES_TO_KILOMETERS = 1.60934


class MilesConverterApp(App):
    """Kivy App for converting miles to kilometres."""
    output_km = StringProperty()

    def build(self):
        self.title = "miles to kilometers conversion tool"
        self.root = Builder.load_file('convert_miles_km.kv')
        return self.root

    def convert_miles_to_kilometers(self, miles):
        print("convert miles to kilometers")
        kilometers = miles*MILES_TO_KILOMETERS
        print(kilometers)
        self.output_km = self.root.ids.miles.text


MilesConverterApp().run()