class SpaceAge:
    def __init__(self, seconds):
        self.seconds=seconds
    def on_mercury(self):
        year_sec_mer = (31557600)*(0.2408467)
        return round((self.seconds)/(year_sec_mer),2)
    def on_venus(self):
        year_sec_ven = (31557600)*(0.61519726)
        return round((self.seconds)/(year_sec_ven),2)
    def on_earth(self):
        year_sec_ear = (31557600)*(1)
        return round((self.seconds)/(year_sec_ear),2)
    def on_mars(self):
        year_sec_mar = (31557600)*(1.8808158)
        return round((self.seconds)/(year_sec_mar),2)
    def on_jupiter(self):
        year_sec_jup = (31557600)*(11.862615)
        return round((self.seconds)/(year_sec_jup),2)
    def on_saturn(self):
        year_sec_sat = (31557600)*(29.447498)
        return round((self.seconds)/(year_sec_sat),2)
    def on_uranus(self):
        year_sec_ura = (31557600)*(84.016846)
        return round((self.seconds)/(year_sec_ura),2)
    def on_neptune(self):
        year_sec_nep = (31557600)*(164.79132)
        return round((self.seconds)/(year_sec_nep),2)
