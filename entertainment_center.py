import fresh_tomatoes
import media

# create Movie instances
# Including title, summary, poster art, and then trailer url
toy_story = media.Movie(
    "Toy Story",
    "A story of a boy and his toys that come to life",
    "https://upload.wikimedia.org/wikipedia/en/1/13/Toy_Story.jpg",
    "https://www.youtube.com/watch?v=KYz2wyBy3kc")

avatar = media.Movie(
    "Avatar",
    "A marine on an alien planet",
    "https://upload.wikimedia.org/wikipedia/en/b/b0/Avatar-Teaser-Poster.jpg",
    "https://www.youtube.com/watch?v=5PSNL1qE6VY")

finding_dory = media.Movie(
    "Finding Dory",
    "Finding Dory focuses on the amnesiac fish Dory.",
    "https://upload.wikimedia.org/wikipedia/en/3/3e/Finding_Dory.jpg",
    "https://www.youtube.com/watch?v=i3kIpCzLzEo")

harry_potter = media.Movie(
    "Harry Potter and the Deathly Hallows - Part 2",
    "Harry Potter's quest to find and destroy Lord Voldemort's Horcruxes.",
    "http://bit.ly/29PLJVD",
    "https://www.youtube.com/watch?v=_EC2tmFVNNE")

the_hobbit = media.Movie(
    "The Hobbit: The Battle of the Five Armies",
    "The fate of Middle Earth.",
    "http://bit.ly/29QO7X1",
    "https://www.youtube.com/watch?v=iVAgTiBrrDA")

twenty_twelve = media.Movie(
    "2012",
    "The Mayanism cataclysmic event of 2012.",
    "https://upload.wikimedia.org/wikipedia/en/d/dd/2012_Poster.jpg",
    "https://www.youtube.com/watch?v=sFXGrTng0gQ")

# store all of the movie instances into an array
movies = [
    toy_story,
    avatar,
    finding_dory,
    harry_potter,
    the_hobbit,
    twenty_twelve]

# call fresh_tomatoes.open_movies_page with the movies array
# stored from line 41
fresh_tomatoes.open_movies_page(movies)
