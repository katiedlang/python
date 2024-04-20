import pytest
from television import Television

class Test:
    def setup_method(self):
        self.tv = Television()


    def test_init(self):
        assert self.tv.__str__() == 'Power: Off, Channel: 0, Volume: 0, Mute: Not Muted'


    def test_power(self):
        self.tv.power()
        assert self.tv.__str__() == 'Power: On, Channel: 0, Volume: 0, Mute: Not Muted'


    def test_mute(self):
        self.tv.power()  # Turn the TV on
        self.tv.mute()  # Mute the TV
        assert self.tv.__str__() == 'Power: On, Channel: 0, Volume: 0, Mute: Muted'


    def test_channel_up(self):
        self.tv.power()
        self.tv.channel_up()
        assert self.tv.__str__() == 'Power: On, Channel: 1, Volume: 0, Mute: Not Muted'


    def test_channel_down(self):
        self.tv.power()
        self.tv.channel_down()
        assert self.tv.__str__() == 'Power: On, Channel: 3, Volume: 0, Mute: Not Muted'


    def test_volume_up(self):
        self.tv.power()
        self.tv.volume_up()
        assert self.tv.__str__() == 'Power: On, Channel: 0, Volume: 1, Mute: Not Muted'


    def test_volume_down(self):
        self.tv.power()
        self.tv.volume_down()
        assert self.tv.__str__() == 'Power: On, Channel: 0, Volume: 0, Mute: Not Muted'

