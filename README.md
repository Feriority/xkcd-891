xkcd-891
========

xkcd 891: Movie Ages, pulled dynamically from IMDB to stay up to date.

Requires beautiful-soup-4.

To run, just call the script with the age you want, ie `python xkcd_891.py 25`.
It will find a movie to make you feel old, if your age is between 16 and 35.

Based on https://xkcd.com/891/.  The xkcd comic has gotten out of date, and
that will only get worse.  This takes the concept and guarantees it stays up to
date by fetching the most popular movie from IMDB for the right number of years
ago, using the same offsets as the comic.
