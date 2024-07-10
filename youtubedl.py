import yt_dlp

def download_video(video_url, save_path):
    ydl_opts = {
        'outtmpl': save_path + '/%(title)s.%(ext)s',
        'format': 'best'
    }

    with yt_dlp.YoutubeDL(ydl_opts) as ydl:
        ydl.download([video_url])

if __name__ == "__main__":
    video_url = input("Enter the URL of the YouTube video: ")
    save_path = input("Enter the path to save the downloaded video: ")

    download_video(video_url, save_path)