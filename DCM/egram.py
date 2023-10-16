class Marker:
    def __init(self, marker, time, modifier = None):
        self.marker = marker
        self.modifier = modifier
        self.time = time

    def get_marker(self):
        return self.marker
    
    def get_time(self):
        return self.time
    
    def get_modifier(self):
        return self.modifier