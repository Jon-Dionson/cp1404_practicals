from prac_08.taxi import Taxi


class SilverServiceTaxi(Taxi):
    """SilverServiceTaxi class"""
    flagfall = 4.50

    def __init__(self, name, fuel, fanciness):
        super().__init__(name, fuel)
        self.fanciness = fanciness
        self.price_per_km *= fanciness

    def __str__(self):
        """Return a string like a Car but with current fare distance."""
        return f"{super().__str__()} plus flagfall of ${self.flagfall:.2f}"

    def get_fare(self):
        """Get current fare."""
        return self.flagfall + super().get_fare()
