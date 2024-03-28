from pytube import YouTube

downloader = YouTube("https://youtu.be/Uzj3CD0FUhA")
streams = downloader.streams.first()
streams.download(r"C:\Users\ASUS\qt_programs\tic tac toe")
print("downloaded")