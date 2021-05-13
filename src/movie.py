class Movie:

    def __init__(self, title):
        self.title = title

    def use_prop(self, prop):
        return f"The Movie {self.title} is using the {prop.name} prop making the sound {prop.make_sound()}"