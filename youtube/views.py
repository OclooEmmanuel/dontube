from django.shortcuts import render,redirect
from django.http import HttpResponse
from .forms import Youtube

import yt_dlp

# Create your views here.

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
    
    
def home(request):
    if request.method == 'POST':
        form = Youtube(request.POST)
        if form.is_valid():
            url = form.cleaned_data['urlbox']
            try:
                 ydl_opts = {
                    'format': 'best',
                    'outtmpl': 'downloads/%(title)s.%(ext)s',
                }

                 with yt_dlp.YoutubeDL(ydl_opts) as ydl:
                    ydl.download([url])
                    return redirect('home')
                
                
            except Exception as e:
                return HttpResponse(f'an error has occured: {e} ')
            
    context = {'form': Youtube}
    return render(request, "index.html",context)




