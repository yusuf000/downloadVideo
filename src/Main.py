from pytube import YouTube
from youtubesearchpython import VideosSearch

def downloadVideo(url, outputDir):
    yt = YouTube(url)
    yt.streams.filter(progressive=True, file_extension='mp4').order_by('resolution').desc().first().download(output_path=outputDir)
def getSearchResult(searchText):
    videosSearch = VideosSearch('NoCopyrightSounds', limit=2)
    print(videosSearch.result())
if __name__ == '__main__':
    getSearchResult("political toxic speech")

