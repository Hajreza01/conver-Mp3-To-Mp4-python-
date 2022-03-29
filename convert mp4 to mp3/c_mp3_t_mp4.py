import moviepy.editor
film = moviepy.editor.VideoFileClip("Shadow.mp4")
audio = film.audio 
audio.write_audiofile("defult_.mp3")


#create by Hajreza