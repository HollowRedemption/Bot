import os
from telegram import Update
from telegram.ext import Application, CommandHandler, CallbackContext
import subprocess
import tempfile
TOKEN = os.getenv('TOKEN')  # Utilise la variable d'environnement

async def download(update: Update, context: CallbackContext) -> None:
    if len(context.args) != 1:
        await update.message.reply_text('Usage: /download <url>')
        return

    url = context.args[0]
    chat_id = update.message.chat_id
    video_path = tempfile.mkdtemp()  # Dossier où les vidéos seront sauvegardées

    if not os.path.exists(video_path):
        os.makedirs(video_path)

    # Exécute le script Python en utilisant subprocess
    result = subprocess.run(['python', 'DownloadMp4Ytb.py', url, video_path], capture_output=True, text=True)

    if result.returncode == 0:
        # Trouve le fichier vidéo téléchargé
        video_file = next((f for f in os.listdir(video_path) if f.endswith('.mp4')), None)
        if video_file:
            video_file_path = os.path.join(video_path, video_file)
            await update.message.reply_document(document=open(video_file_path, 'rb'))


def main() -> None:
    application = Application.builder().token(TOKEN).build()

    application.add_handler(CommandHandler('download', download))

    application.run_polling()

if __name__ == '__main__':
    main()
