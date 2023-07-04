<img width="1360" alt="Screen Shot 2023-07-04 at 7 59 50 PM" src="https://github.com/Kudzmat/spot_playlists/assets/65554208/dba0f433-836c-47c0-af60-a42c079cca98"># Spotify Playlists

<img width="1470" alt="Screen Shot 2023-05-26 at 4 42 28 PM" src="https://github.com/Kudzmat/spot_playlists/assets/65554208/31cce9a2-2ece-4742-bdd5-4942a2171e07">

This application allows users to interact with Spotify's API to retrieve and manipulate music data. There's so much music available on
Spotify and this can sometimes be overwhelming. This app exists to give you the option to just find music based on what you're feeling at the moment and curate the perfect vibe playlist.


# FEATURES
Vibe Check: Enter 5 artists you’re in the mood to listen to and the application will add 5 new songs to your Spotify playlist that align with the sound of the artists you have entered
<img width="1358" alt="Screen Shot 2023-07-04 at 7 58 37 PM" src="https://github.com/Kudzmat/spot_playlists/assets/65554208/acb36bf6-e78f-4750-82a1-e12fa0d5b90c">

Recommendations: Don’t have any artists in mind? Use the Recommendations feature and select a genre to get 5 playlists recommendations to listen to on your Spotify account
<img width="1360" alt="Screen Shot 2023-07-04 at 7 59 50 PM" src="https://github.com/Kudzmat/spot_playlists/assets/65554208/9830ce9a-5a1c-4f1f-b6a0-d431c2d949aa">

# Prerequisites

Python3
Spotipy
Flask
Spotify API Credentials: Obtain the client ID and client secret by creating a new app in the Spotify Developer Dashboard. Visit https://developer.spotify.com/dashboard to create a new app.

# Getting Started

1. Clone The Repository
  
2. Install dependencies:
   pip install flask
   pip install spotipy
   
3. Set up the Spotify API credentials:
  Open the .env file and replace YOUR_CLIENT_ID and YOUR_CLIENT_SECRET with your actual Spotify API credentials.

4. Start the application with "Flask Run"

# Usage

Home Page: The home page provides the Vibe Check form where users can enter 5 artists that describe their current mood. 5 songs that match your current vibe will be added to your Spotify playlist and you will be taken to your playlist where you can listen to these songs.

Recommendations: This page lets a user select a genre of music from a drop-down list. The application will give the user 5 playlists to listen to full of music from the selected genre. 
<img width="1359" alt="Screen Shot 2023-07-04 at 8 00 45 PM" src="https://github.com/Kudzmat/spot_playlists/assets/65554208/04330fd6-1208-4f0a-b773-6b38fb8ff926">


# Contributions

Contributions are welcome! If you have any ideas, suggestions, or bug reports, please open an issue or submit a pull request.

