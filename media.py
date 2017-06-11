'''
Defines the Movie class for this project.
Each movie gets a title, storyline, poster image and youtube trailer,
as well as a method to play that trailer.
'''

import webbrowser

class Movie():
    # Constructor and definition of instance variables
    def __init__(self, movie_title, movie_storyline, poster_image, trailer_youtube):
        self.title = movie_title
        self.storyline = movie_storyline
        self.poster_image_url = poster_image
        self.trailer_youtube_url =trailer_youtube

    # Show trailer method
    def show_trailer(self):
        webbrowser.open(self.trailer_youtube_url)
