#Dahan, Regine Fae M. Dahan BSCPE 1-5 ( Introduction to OOP )

#create a class TV

class Tv:
    #constructor
    def __init__(self, channel, volumeLevel, power):
        self.channel = channel 
        self.volume_level = volumeLevel
        self.power = power

    def turn_on(self):
        self.power = True
    
    def turn_off(self):
        self.power = False

    def get_channel(self):
        return self.channel 

    def set_channel(self, channel):
        self.channel = channel

    def get_volume(self):
        return self.volume_level
    
    def set_volume(self, volumeLevel):
        self.volume_level = volumeLevel
    
    def channel_up(self):
        self.channel += 1
    
    def channel_down(self):
        self.channel -= 1
    
    def volume_up(self):
        self.volume_level += 1
    
    def volume_down(self):
        self.volume_level -= 1


