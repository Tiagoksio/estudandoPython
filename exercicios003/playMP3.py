from pygame import mixer
song = 'arquivo-de-audio.ogg'
mixer.init()
mixer.music.load(song)
mixer.music.play()
mixer.music.set_volume(1)
x = input('Aperte uma tecla para parar...')
