# 🎵 Spotify Artist Analysis
Python script for fetching and displaying information about an artist, including their albums and tracks., via Spotify API.

## ✨ Features

- **Authentication**: Authenticate with the Spotify API using client credentials.
- **Artist Search**: Search for an artist by name.
- **Album and Track Retrieval**: Fetch all albums and tracks for the specified artist.
- **Popularity Sorting**: Sort albums and tracks by popularity.
- **Detailed Output**: Display detailed information about the artist, their albums, and tracks.

## 🛠 Requirements

- Python 3.6 or higher
- `spotipy` library
- `pandas` library

## 📥 Installation

1. Clone the repository:
    ```bash
    git clone https://github.com/dzhaner01/spotify_artist_analysis.git
    cd spotify_artist_analysis
    ```

2. Install the required libraries:
    ```bash
    pip install spotipy pandas
    ```

3. Obtain Spotify API credentials by creating a Spotify Developer account and registering an application.

## 🚀 Usage

1. Open the script and replace the `client_id` and `client_secret` with your Spotify API credentials.
2. Run the script:
    ```bash
    python spotify_artist_analysis.py
    ```
3. Enter the name of the artist when prompted.

## 📋 Example

```plaintext
Enter the artist's name: Preslava

Artist: Preslava
Followers: 232152
Genres: bulgarian pop, chalga
Popularity: 52
Tracks: 101
Albums: 8

All Tracks (sorted by popularity):
1. Ne se iztrivash (Popularity: 42, Year: 2019, Album: Da gori v lyubov)
2. Dyavolsko zhelanie (Popularity: 41, Year: 2005, Album: Dyavolsko zhelanie)
...

All Albums (sorted by popularity):
1. Da gori v lyubov (Popularity: 46, Year: 2019)
2. Ulitsata (Popularity: 45, Year: 2024)
...
