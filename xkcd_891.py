import sys
from bs4 import BeautifulSoup
from datetime import date


# Python 2 support means shenanigans
try:
    from urllib import request
except ImportError:
    import urllib2 as request


MOON_LANDING = date(1969, 7, 20)


# Contains exact matches; ranges are handled separately
age_to_offset_and_msg = {
    16: (5, 'half a decade ago'),
    20: (8, 'eight years ago'),
    26: (16, 'over fifteen years ago'),
    27: (17, 'seventeen years ago'),
    28: (18, 'eighteen years ago'),
    29: (20, 'twenty years ago'),
}


def get_movie_for_year(year):
    url = 'http://www.imdb.com/year/%d' % year
    soup = BeautifulSoup(request.urlopen(url))
    results = soup.find('table', 'results')
    for movie in results.find_all('td', 'title'):
        if movie.find('span', 'titlePageSprite')['title'] in ('G', 'PG'):
            return movie.find('a').text
    # If we found no movies rated G or PG, just return the #1 movie
    return results.find('td', 'title').find('a').text


def feel_old(age):
    if age < 16:
        print("It's probably too late to be a child prodigy.")
        return
    elif age > 35:
        print("Hey, did you see this chart?  You match your age to movie - oh, right, sorry, it only goes up to 35.  I guess it's not really aimed at older people.")
        return

    current_year = date.today().year

    if age in age_to_offset_and_msg:
        offset, message = age_to_offset_and_msg[age]
    else:
        if 17 <= age <= 19:
            message = "more than half a decade ago"
            offset = 6
        elif 21 <= age <= 22:
            message = "ten years ago"
            offset = 10
        elif 23 <= age <= 25:
            # This doesn't work so well late in a decade
            message = "not last decade, but the decade before that"
            offset = current_year % 10 + 11
        elif 30 <= age <= 32:
            message = "more than twenty years ago"
            offset = 21
        elif 33 <= age <= 35:
            message = "closer to the moon landing than the present day"
            time_since_moon_landing = date.today() - MOON_LANDING
            halfway_point = time_since_moon_landing / 2
            offset = halfway_point.days // 365 + 1

    movie_year = current_year - offset

    try:
        title = get_movie_for_year(movie_year)
        print("Did you realize that %s came out %s?" % (title, message))
    except:
        print("Unable to load movies from IMDB.")


if __name__ == '__main__':
    #TODO fail gracefully here
    feel_old(int(sys.argv[1]))
