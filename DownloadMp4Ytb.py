# DownloadMp4Ytb.py
import yt_dlp
import sys
import os

def telecharger_video(url, chemin_de_sauvegarde):
    try:
        ydl_opts = {
            'format': 'bestvideo+bestaudio/best',  # Télécharger la meilleure qualité vidéo et audio
            'outtmpl': os.path.join(chemin_de_sauvegarde, '%(title)s.%(ext)s'),  # Modèle de nom pour le fichier
            'noplaylist': True,  # Ne pas télécharger les vidéos d'une playlist
        }
        with yt_dlp.YoutubeDL(ydl_opts) as ydl:
            info_dict = ydl.extract_info(url, download=True)
            video_title = info_dict.get('title', 'Unknown Title')
            video_file_mp4 = os.path.join(chemin_de_sauvegarde, f"{video_title}.mp4")

            if os.path.exists(video_file_mp4):
                print(f"Vidéo téléchargée avec succès ! Nom de fichier : {video_title}.mp4")
            else:
                print(f"Erreur lors du téléchargement de la vidéo : {video_title}")

    except Exception as e:
        print(f"Erreur lors du téléchargement de la vidéo : {str(e)}")

if __name__ == "__main__":
    if len(sys.argv) != 3:
        print("Usage: python DownloadMp4Ytb.py <url> <chemin_de_sauvegarde>")
        sys.exit(1)

    url = sys.argv[1]
    chemin_de_sauvegarde = sys.argv[2]
    telecharger_video(url, chemin_de_sauvegarde)
