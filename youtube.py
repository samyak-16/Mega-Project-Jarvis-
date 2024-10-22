from youtubesearchpython import VideosSearch
from musiclibrary import music  # Import the music dictionary directly

def add_music_to_library(music_name):
    """Search for the music on YouTube and add it to the music library."""
    if music_name in music:
        print(f"'{music_name}' is already in the library.")
        return music_name  # Return the music name if it already exists

    # Search for the music on YouTube
    search = VideosSearch(music_name, limit=1)
    result = search.result()

    if result["result"]:
        # Get the first video result
        video = result["result"][0]
        title = video['title']
        url = video['link']

        # Add the new music to the library
        music[title] = url
        print(f"Added {title}: {url} to the music library.")

        # Save changes back to the file
        save_library()
        return title  # Return the title of the added music
    else:
        print("No results found on YouTube.")
        return None  # Return None if no results are found

def save_library():
    """Save the updated music library back to musiclibrary.py."""
    with open("musiclibrary.py", "w") as f:
        f.write(f"music = {music}")  # Use the imported music directly
