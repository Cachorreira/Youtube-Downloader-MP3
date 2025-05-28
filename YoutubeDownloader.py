
import yt_dlp
import os

def baixar_mp3(url):
    try:
        pasta_destino = "/home/kaique/Documentos/"
        os.makedirs(pasta_destino, exist_ok=True)  # cria a pasta se não existir

        print("⏬ Iniciando download em MP3...")

        opcoes = {
            'format': 'bestaudio/best',
            'outtmpl': '%(title)s.%(ext)s',  # nome do arquivo será o título do vídeo
            'postprocessors': [{
                'key': 'FFmpegExtractAudio',
                'preferredcodec': 'mp3',
                'preferredquality': '192',
            }],
            'quiet': False,
            'noplaylist': True  # evita baixar playlists inteiras
        }

        with yt_dlp.YoutubeDL(opcoes) as ydl:
            ydl.download([url])

        print("✅ Download e conversão finalizados!")
    except Exception as e:
        print(f"❌ Erro: {e}")

# 🔗 Link do vídeo
url = "https://youtu.be/H7IUS4BkOYI?si=2DPHLsAx1bd_kYkU"

# 🚀 Executa
baixar_mp3(url)
