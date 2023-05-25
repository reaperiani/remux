import sys
import os
import subprocess
from PyQt5.QtWidgets import QApplication, QWidget, QVBoxLayout, QHBoxLayout, QLabel, QLineEdit, QPushButton, QFileDialog, QMessageBox

video_file = ""
audio_file = ""
rimuovi = ""
script_directory = os.getcwd()
ffmpeg_executable = os.path.join(script_directory, "ffmpeg")


def browse_video():
    global video_file
    video_file, _ = QFileDialog.getOpenFileName(None, "Scegli il Video", "", "Video files (*.avi *.mp4 *.mkv *.mov *.wmv *.flv *.webm *.mpeg *.mpg);;All files (*)")
    video_entry.setText(video_file)
    video_file = f'"{video_file}"'

def browse_audio():
    global audio_file
    audio_file, _ = QFileDialog.getOpenFileName(None, "Scegli l'audio", "", "Audio files (*.wav *.aiff *.aif *.aifc);;All files (*)")
    audio_entry.setText(audio_file)
    audio_file = f'"{audio_file}"'


def run_ffmpeg_remove_audio(video_file):
    output_file = os.path.splitext(video_file)[0] + "_noaudio.mkv"
    cmd = [ffmpeg_executable, "-i", video_file, "-c", "copy", "-an", output_file]
    print("XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX")
    print(' '.join(cmd))
    subprocess.run(cmd)

def run_ffmpeg_add_audio(video_file, audio_file):
    output_file = os.path.splitext(video_file)[0] + "_output.mkv"
    noau = os.path.splitext(video_file)[0] + "_noaudio.mkv"
    cmd = [ffmpeg_executable, "-i", noau, "-i", audio_file, "-c", "copy", "-map", "0", "-map", "1:a", output_file]
    print("XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX")
    print(' '.join(cmd))
    subprocess.run(cmd)

def merge_video_and_audio():
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