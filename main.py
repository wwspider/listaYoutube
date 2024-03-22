from pytube.contrib.playlist import Playlist
from pytube import YouTube
from pytube.cli import on_progress
import os
import re
from pathlib import Path
import shutil

url = input('Cole o link da lista:\n')
playlist = Playlist(url)
# nome da lista de vídeos
print(f'{playlist.title}')
# total de vídeos da lista
print('Total de vídeos: ', len(playlist.video_urls))
num = 1
# cria pasta com nome da lista
pasta = playlist.title+'/'

if(not os.path.exists(pasta)):
    os.mkdir(pasta)

for video_url in playlist.video_urls:
    yt = YouTube(video_url, on_progress_callback=on_progress)
    stream = yt.streams.get_highest_resolution()
    print(f'{num} - {yt.title}')
    re_yt = yt.title
    re_yt = re.sub(r'[^a-zA-Z0-9]', ' ', yt.title)

    stream.download(filename=str(num) + '-' + re_yt + '.mp4')
    num += 1

# recortar arquivos para pasta criada
caminho = os.getcwd()
origem = caminho
destino = caminho+'\\'+pasta

arquivos = os.listdir(origem)
for nome in arquivos:
    if nome.endswith('.mp4'):
        print(nome)
        origem_full = origem+'\\'+nome
        #print(origem_full)
        shutil.move(origem_full, destino)

# https://www.youtube.com/watch?v=nScOzRZjoiA&t=124s