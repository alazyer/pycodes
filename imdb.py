#!/usr/bin/env python
# Script to gather IMDB keywords from 2013's top grossing movies.
# following the step of Jeff Knupp, with the post in his blog.
# "starting-a-python-project-the-right-way"

import sys
import requests
from bs4 import BeautifulSoup
import csv

URL = "http://www.imdb.com/search/title?at=0&sort=boxoffice_gross_us,desc&start=1&year=2013,2013"

def main():
    movies = get_top_grossing_movie_links(URL)
    with open('output.csv', 'w') as output:
        csvwriter = csv.writer(output)
        for title, url in movies:
            keywords = get_keywords_for_movie('http://www.imdb.com{}keywords/'.format(url))
            csvwriter.writerow([title, keywords])

def get_top_grossing_movie_links(url):
    response = requests.get(url)
    movies = []
    soup = BeautifulSoup(response.text)
    for movie_url in soup.select('.title a[href*="title"]'):
        movie = movie_url.text
        if movie != 'X':
            movies.append((movie, movie_url['href']))
    return movies

def get_keywords_for_movie(url):
    keywords = []
    response = requests.get(url)
    soup = BeautifulSoup(response.text)
    tables = soup.find_all('table', class_='dataTable')
    table = tables[0]
    keywords = [td.text for tr in table.find_all('tr') for td in tr.find_all('td')]

    return keywords

if __name__ == '__main__':
    sys.exit(main())
