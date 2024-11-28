from spotipy.oauth2 import SpotifyClientCredentials
import spotipy
import pandas as pd

# Spotify API credentials
client_id = "client_id"
client_secret = "client_secret"

# Authenticate with Spotify using client credentials
def authenticate_spotify(client_id, client_secret):
    auth_manager = SpotifyClientCredentials(client_id=client_id, client_secret=client_secret)
    return spotipy.Spotify(auth_manager=auth_manager)

# Search for an artist by name
def search_artist(sp, artist_name):
    results = sp.search(q='artist:' + artist_name, type='artist')
    if results['artists']['items']:
        artist = results['artists']['items'][0]  # Get the first artist returned
        return artist
    return None

# Fetch albums by artist
def fetch_albums(sp, artist_id):
    return sp.artist_albums(artist_id, album_type='album')['items']

# Fetch tracks from an album
def fetch_album_tracks(sp, album_id):
    return sp.album_tracks(album_id)['items']

# Fetch detailed track info
def fetch_track_info(sp, track_id):
    return sp.track(track_id)

# Get all tracks by artist
def get_all_tracks(sp, artist_id):
    tracks = []
    albums = fetch_albums(sp, artist_id)
    for album in albums:
        album_tracks = fetch_album_tracks(sp, album['id'])
        for track in album_tracks:
            track_info = fetch_track_info(sp, track['id'])
            tracks.append({
                'name': track_info['name'],
                'popularity': track_info['popularity'],
                'year': album['release_date'][:4],  # Only take the year part from release date
                'album': album['name']
            })
    # Sort tracks by popularity in descending order
    return sorted(tracks, key=lambda x: x['popularity'], reverse=True)

# Get all albums by artist
def get_all_albums(sp, artist_id):
    albums = fetch_albums(sp, artist_id)
    album_data = [{
        'name': album['name'],
        'popularity': sp.album(album['id'])['popularity'],
        'year': album['release_date'][:4]  # Only take the year part from release date
    } for album in albums]
    # Sort albums by popularity in descending order
    return sorted(album_data, key=lambda x: x['popularity'], reverse=True)

# Print artist information
def print_artist_info(artist, num_tracks, num_albums):
    print(f"\nArtist: {artist['name']}")
    print(f"Followers: {artist['followers']['total']}")
    print(f"Genres: {', '.join(artist['genres'])}")
    print(f"Popularity: {artist['popularity']}")
    print(f"Tracks: {num_tracks}")
    print(f"Albums: {num_albums}\n")

# Print track list
def print_tracks(df_tracks):
    print("All Tracks (sorted by popularity):")
    for index, track in enumerate(df_tracks.itertuples(), start=1):
        print(f"{index}. {track.name} (Popularity: {track.popularity}, Year: {track.year}, Album: {track.album})")

# Print album list
def print_albums(df_albums):
    print("\nAll Albums (sorted by popularity):")
    for index, album in enumerate(df_albums.itertuples(), start=1):
        print(f"{index}. {album.name} (Popularity: {album.popularity}, Year: {album.year})")

# Main function
def main():
    # Authenticate with Spotify
    sp = authenticate_spotify(client_id, client_secret)
    artist_name = input("Enter the artist's name: ")
    artist = search_artist(sp, artist_name)
    
    if not artist:
        print("Artist not found. Please try again.")
        return

    # Get all tracks and albums for the artist
    all_tracks = get_all_tracks(sp, artist['id'])
    all_albums = get_all_albums(sp, artist['id'])

    # Create DataFrames for tracks and albums
    df_tracks = pd.DataFrame(all_tracks)
    df_albums = pd.DataFrame(all_albums)

    # Print information
    print_artist_info(artist, len(all_tracks), len(all_albums))
    print_tracks(df_tracks)
    print_albums(df_albums)

if __name__ == "__main__":
    main()