from pytube import Playlist, YouTube


def download_playlist(playlist_url, output_path):
    playlist = Playlist(playlist_url)
    print(f"Downloading playlist: {playlist.title}")

    for video_url in playlist.video_urls:
        try:
            video = YouTube(video_url)
            print(f"Downloading: {video.title}")
            video.streams.get_highest_resolution().download(output_path)
        except Exception as e:
            print(f"Error downloading {video_url}: {str(e)}")

    print("Download completed!")

'''
 Note: How to use the script to download all videos from the playlist of Youtube

    You need to change the playlist url.
    Copy url from the youtube and paste here.
    Execute the script and it will download complete playlist.

'''

if __name__ == "__main__":
    import os

    current_directory = os.getcwd()
    current_directory = current_directory + '/Azure Data eng/technical_guptgu'
    playlist_url = "https://www.youtube.com/watch?v=BequsOVM2aA&list=PLBGx66SQNZ8b9BSratoxD6F1d4llBn-0W"  # Replace with the URL of the YouTube playlist
    output_path = current_directory  # Replace with the directory where you want to save the videos
    download_playlist(playlist_url, output_path)
