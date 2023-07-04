from datetime import date
from forms import PlaylistForm, RecommendationForm
from app import app
from flask import render_template, url_for, redirect, session
from dotenv import load_dotenv
import os
import spotipy

from spotipy.oauth2 import SpotifyOAuth

load_dotenv()  # load the environment variables

# storing environment variables
CLIENT_ID = os.getenv('CLIENT_ID')
CLIENT_SECRET = os.getenv('CLIENT_SECRET')
SPOTIFY_REDIRECT_URI = os.getenv('SPOTIFY_REDIRECT_URI')
SPOTIFY_USER_ID = os.getenv('SPOTIFY_USER_ID')
PLAYLIST_ID = os.getenv('PLAYLIST_ID')

# set scope for app authorization
SCOPE = "user-library-read user-top-read playlist-modify-public user-follow-read user-library-read " \
        "playlist-read-private playlist-modify-private "


# home page route for vibe check
@app.route('/', methods=["GET", "POST"])
def try_playlist():
    form = PlaylistForm()  # instantiating a new form
    artist_list = []  # this empty list will hold the 5 artists entered

    if form.validate_on_submit():
        # getting the entered artists and appending them to the list
        artist1 = form.artist1.data
        artist_list.append(artist1)

        artist2 = form.artist2.data
        artist_list.append(artist2)

        artist3 = form.artist3.data
        artist_list.append(artist3)

        artist4 = form.artist4.data
        artist_list.append(artist4)

        artist5 = form.artist5.data
        artist_list.append(artist5)

        session['artist_list'] = artist_list  # saving artist list to use for next route

        return redirect(url_for('playlist'))  # redirect to playlist route

    return render_template('index.html', form=form)


# route which will take you to your playlist page on Spotify after entering artists
@app.route('/playlist', methods=["GET", "POST"])
def playlist():
    sp = spotipy.Spotify(auth_manager=SpotifyOAuth(scope=SCOPE, client_id=CLIENT_ID, client_secret=CLIENT_SECRET,
                                                   username=SPOTIFY_USER_ID, redirect_uri=SPOTIFY_REDIRECT_URI))

    # pick a playlist to add the songs to
    # To find the Spotify playlist id enter the playlist page, click the (...) button near the play button
    # Click "Copy Playlist Link" under the Share menu. The playlist id is the string right after "playlist/"
    playlist_id = PLAYLIST_ID

    # getting today's date
    current_date = (date.today()).strftime('%m-%d-%Y')

    # saving playlist name with today's date
    playlist_name = f'Vibe Check -> {current_date}'

    artists_ids = []  # spotify's recommended artist IDs will be added to this list
    tracks = []  # the recommended tracks will be added to this list
    artist_list = session['artist_list']  # calling the artist list from the previous route

    # putting artist ids in a list so we can use them in the recommendations function
    for artist in artist_list:
        # search for the artist
        name_result = sp.search(artist, limit=1, type='artist', market='US')

        # get artist ID
        artist_info = name_result['artists']['items'][0]
        artist_id = artist_info['id']

        # add artist to list
        artists_ids.append(artist_id)

    # getting 5 song recommendation and appending them to tracks
    result = sp.recommendations(seed_artists=artists_ids, limit=5, country='US')
    for item in result['tracks']:
        # append the track['uri']
        tracks.append(item['uri'])

    # adding songs to our playlist
    sp.playlist_add_items(playlist_id=playlist_id, items=[song for song in tracks])

    # updating the playlist name with last updated date
    sp.playlist_change_details(name=playlist_name, playlist_id=playlist_id)

    # takes you to playlist page on Spotify
    return redirect('https://open.spotify.com/playlist/138EKhzuYuww8DKcRC69ox')


# route for getting recommendations
@app.route('/recommendations', methods=["GET", "POST"])
def choose_genre():
    # recommendation dropdown form
    form = RecommendationForm()
    if form.validate_on_submit():
        selected_option = form.dropdown.data

        # redirect to your_playlists route
        return redirect(url_for("your_playlists", selected_option=selected_option))

    return render_template('recommendations.html', form=form, )


# this route will show all the playlists we have recommended to the user
@app.route('/<selected_option>-playlists')
def your_playlists(selected_option):
    sp = spotipy.Spotify(auth_manager=SpotifyOAuth(scope=SCOPE, client_id=CLIENT_ID, client_secret=CLIENT_SECRET,
                                                   username=SPOTIFY_USER_ID, redirect_uri=SPOTIFY_REDIRECT_URI))

    categories = {}  # will hold music categories and playlist ids
    recommendations = {}  # will hold playlist name, image, link and description

    tunes = sp.categories(country='US')  # get category list
    tunes1 = tunes['categories']['items']  # gives us access to genre & id keys

    for item in tunes1:

        # setting our items to variables
        genre = item['name']
        genre_id = item['id']

        # adding items to dictionary
        categories[genre] = genre_id

    # search for category in dictionary
    if selected_option in categories.keys():

        # get playlist id using dictionary key (category)
        playlist_id = categories[selected_option]

        # get 5 playlist recommendations
        playlists = sp.category_playlists(category_id=playlist_id, limit=5)

    else:
        # take back to home page if we don't get 5 playlists or if the category is missing from the dictionary
        return redirect(url_for('try_playlist'))

    # getting access to our essential information
    play_list_info = playlists['playlists']['items']

    for info in play_list_info:

        # setting our information to variables
        playlist_name = info['name']
        description = info['description']
        link = info['external_urls']['spotify']
        image = info['images'][0]['url']

        # adding our information using the playlist name as a key and a list of the other info as value
        recommendations[playlist_name] = [description, link, image]

    return render_template("playlists.html", recommendations=recommendations, selected_option=selected_option)
