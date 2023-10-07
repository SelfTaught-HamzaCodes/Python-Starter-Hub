from pytube import YouTube

# Define a function to download a YouTube video given its URL.
def youtube_video(url):
    # Create a YouTube object with the provided URL.
    video = YouTube(url)

    # Display video information:
    # Title
    print(f'Title: {video.title}.')

    # Length (in seconds, converted to minutes)
    print(f'Length: {video.length // 60} minutes.')

    # Author
    print(f'Author: {video.author}.')

    # Ask the user for permission to download the video.
    download_video = input("\nDownload Now (Y-Yes or N-No): ").upper()

    if download_video == "Y":
        # Get the highest resolution stream of the video.
        video = video.streams.get_highest_resolution()

        # Download the video.
        video.download()
    else:
        pass

# Display a welcome message.
print("\nWelcome to Download this Video")

# Ask the user to paste the URL of the video they want to download.
url = input("\nPaste the URL to download the video: ")

# Call the youtube_video function to process and potentially download the video.
youtube_video(url)

# Display a thank you message.
print("\nThank you for visiting!")
