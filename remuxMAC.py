import sys
import os
import subprocess
import shutil
from PyQt5.QtWidgets import (
    QApplication,
    QWidget,
    QVBoxLayout,
    QLabel,
    QLineEdit,
    QPushButton,
    QFileDialog,
    QMessageBox,
    QDialog
)

from PyQt5.QtCore import (
    QThread,
    QObject,
)

import urllib.request

video_file = ""
audio_file = ""
rimuovi = ""
script_directory = os.getcwd()
ffmpeg_executable = os.path.join(script_directory, "ffmpeg")

class Worker(QObject):
    def __init__(self, window) -> None:
        super().__init__()
        self.window = window

    def run(self) -> None:
        # do jobs
        self.download_ffmpeg()

        # close window
        self.window.close()

    def download_ffmpeg(self) -> None:
        # download and unpack logic
        ffmpeg_zipfile = os.path.join(script_directory, "ffmpeg.zip")
        urllib.request.urlretrieve("https://evermeet.cx/ffmpeg/getrelease/zip", ffmpeg_zipfile)
        shutil.unpack_archive(ffmpeg_zipfile)

        # cleanup
        os.remove(ffmpeg_zipfile)

class DownloadDependencies(QDialog):
    def __init__(self) -> None:
        super().__init__()

        self.setWindowTitle("Downloading ffmpeg")
        self.setFixedSize(270, 70)

        # prevent the user from closing the dialog by accident
        self.setWindowFlag(Qt.WindowCloseButtonHint, False) # type: ignore

        layout = QVBoxLayout()

        label = QLabel("Downloading ffmpeg...\nPlease wait, this may take a while...")
        label.setAccessibleName("Downloading ffmpeg. Please wait, this may take a while...")  # Set accessible name
        layout.addWidget(label)

        self.setLayout(layout)

        self.thread = QThread() # type: ignore
        self.worker = Worker(self)
        self.worker.moveToThread(self.thread) # type: ignore
        self.thread.started.connect(self.worker.run) # type: ignore
        self.thread.start() # type: ignore

def browse_video() -> None:
    global video_file
    video_file, _ = QFileDialog.getOpenFileName(None, "Scegli il Video", "", "Video files (*.avi *.mp4 *.mkv *.mov *.wmv *.flv *.webm *.mpeg *.mpg);;All files (*)")
    video_entry.setText(video_file)
    video_file = f'"{video_file}"'

def browse_audio() -> None:
    global audio_file
    audio_file, _ = QFileDialog.getOpenFileName(None, "Scegli l'audio", "", "Audio files (*.wav *.aiff *.aif *.aifc);;All files (*)")
    audio_entry.setText(audio_file)
    audio_file = f'"{audio_file}"'


def run_ffmpeg_remove_audio(video_file) -> None:
    output_file = os.path.splitext(video_file)[0] + "_noaudio.mkv"
    cmd = [ffmpeg_executable, "-i", video_file, "-c", "copy", "-an", output_file]
    print("XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX")
    print(' '.join(cmd))
    subprocess.run(cmd)

def run_ffmpeg_add_audio(video_file, audio_file) -> None:
    output_file = os.path.splitext(video_file)[0] + "_output.mkv"
    noau = os.path.splitext(video_file)[0] + "_noaudio.mkv"
    cmd = [ffmpeg_executable, "-i", noau, "-i", audio_file, "-c", "copy", "-map", "0", "-map", "1:a", output_file]
    print("XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX")
    print(' '.join(cmd))
    subprocess.run(cmd)

def merge_video_and_audio() -> None:
    global video_file, audio_file, rimuovi
    run_ffmpeg_remove_audio(video_file)
    run_ffmpeg_add_audio(video_file, audio_file)
    rimuovi = os.path.splitext(video_file)[0] + "_noaudio.mkv"
    print("XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX")
    print(rimuovi)
    os.remove(rimuovi)
    QMessageBox.information(None, "Il mio lavoro qui è finito!", "Video e audio ora SONO UNA COSA SOLA.")
    sys.exit()


app = QApplication(sys.argv)
window = QWidget()
window.setWindowTitle("Metti un WAV nel tuo VIDEO! Cretino!")
layout = QVBoxLayout(window)

video_label = QLabel("file Video:")
layout.addWidget(video_label)

video_entry = QLineEdit()
layout.addWidget(video_entry)

video_browse_button = QPushButton("Scegli")
video_browse_button.clicked.connect(browse_video)
layout.addWidget(video_browse_button)

audio_label = QLabel("file Audio:")
layout.addWidget(audio_label)

audio_entry = QLineEdit()
layout.addWidget(audio_entry)

audio_browse_button = QPushButton("Scegli")
audio_browse_button.clicked.connect(browse_audio)
layout.addWidget(audio_browse_button)

merge_button = QPushButton("Metti il Wav nel Video")
merge_button.clicked.connect(merge_video_and_audio)
layout.addWidget(merge_button)

window.show()
sys.exit(app.exec_())