'''
Movie trailer website server backend that generates a page to show
a selection of movies, with their posters and trailers.

Generated during the course of the "Programming Fundamentals and the Web" lecture
on Udacity
'''

import media
import fresh_tomatoes

# Generate the movie objects by calling the constructor media.Movie()
moana = media.Movie("Moana",
                        "A little girl with a big mission",
                        "http://www.impawards.com/2016/posters/moana_ver6.jpg",
                        "https://www.youtube.com/watch?v=LKFuXETZUsI")

premier_jour = media.Movie("Le Premier Jour...",
                     "The life of a French family",
                     "http://medias.unifrance.org/medias/28/43/76572/format_page/media.jpg",
                     "https://www.youtube.com/watch?v=42qLwz1lVNw")

lalaland = media.Movie("La La Land",
                     "A whimsical tale of two artists and lovers",
                     "https://upload.wikimedia.org/wikipedia/en/a/ab/La_La_Land_%28film%29.png",
                     "ttps://www.youtube.com/watch?v=0pdqf4P9MB8")

apocalypse = media.Movie("Apocalypse Now",
                     "Diving into the horrors of the vietnam war",
                     "http://www.impawards.com/1979/posters/apocalypse_now_ver2_xlg.jpg",
                     "https://www.youtube.com/watch?v=IkrhkUeDCdQ")

whatever = media.Movie("Whatever Works",
                     "Larry David gets confused.",
                     "https://images-na.ssl-images-amazon.com/images/M/MV5BMTU2NTA4NzgyNl5BMl5BanBnXkFtZTcwNzEzMjQ1Mg@@._V1_SY1000_CR0,0,675,1000_AL_.jpg",
                     "https://www.youtube.com/watch?v=7vvDhtfil3U")

harry_potter = media.Movie("Harry Potter and the Prisoner of Azkaban",
                     "Harry gets older and the danger greater",
                     "http://www.gstatic.com/tv/thumb/movieposters/34483/p34483_p_v8_ap.jpg",
                     "https://www.youtube.com/watch?v=lAxgztbYDbs")

# Create a data structure with our movies
movies=[moana,
        premier_jour,
        lalaland,
        apocalypse,
        whatever,
        harry_potter]

# Call the open_movies_page function to generate the html page
fresh_tomatoes.open_movies_page(movies)
