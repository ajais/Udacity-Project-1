import media
import fresh_tomatoes

toy_story = media.Movie("Toy Story",
                        "A Story of a boy and his toys that come to life",
                        "http://www.impawards.com/1995/posters/toy_story_ver1_xlg.jpg",
                        "https://www.youtube.com/watch?v=KYz2wyBy3kc")

avatar = media.Movie("Avatar",
                     "A marine on an alien planet",
                     "http://www.impawards.com/2009/posters/avatar_xlg.jpg",
                     "https://www.youtube.com/watch?v=5PSNL1qE6VY")

ratatouille = media.Movie("Ratatouille",
                     "A mouse becomes a chef",
                     "https://upload.wikimedia.org/wikipedia/en/5/50/RatatouillePoster.jpg",
                     "https://www.youtube.com/watch?v=c3sBBRxDAqk")

school_of_rock = media.Movie("School of Rock",
                     "Kids learn life through rock and roll music",
                     "http://img.moviepostershop.com/the-school-of-rock-movie-poster-2003-1020191888.jpg",
                     "https://www.youtube.com/watch?v=XCwy6lW5Ixc")

midnight_in_paris = media.Movie("Midnight in Paris",
                     "A 21st century man wanders magically in 1920 Paris",
                     "https://images-na.ssl-images-amazon.com/images/I/61uuYEUFw4L._SY450_.jpg",
                     "https://www.youtube.com/watch?v=FAfR8omt-CY")

hunger_games = media.Movie("Hunger Games",
                     "A marine on an alien planet",
                     "https://images-na.ssl-images-amazon.com/images/I/51OGv-AnD6L.jpg",
                     "https://www.youtube.com/watch?v=4S9a5V9ODuY")

movies=[toy_story,avatar,ratatouille,school_of_rock,midnight_in_paris,hunger_games]
fresh_tomatoes.open_movies_page(movies)
