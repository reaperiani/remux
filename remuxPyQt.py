import os
import subprocess
from PyQt5.QtWidgets import QApplication, QMainWindow, QVBoxLayout, QPushButton, QLabel, QLineEdit, QFileDialog, QMessageBox
from PyQt5.QtCore import Qt

video_file = ""
audio_file = ""
rimuovi = ""
script_directory = os.getcwd()
ffmpeg_executable = os.path.join(script_directory, "ffmpeg.exe")

class MainApp(QMainWindow):
    def __init__(self):
        super().__init__()

        self.resize(500, 200)

        self.video_label = QLabel("File Video:", self)
        self.video_label.move(20, 20)
        self.video_label.resize(100, 30)

        self.video_entry = QLineEdit(self)
        self.video_entry.move(130, 20)
        self.video_entry.resize(200, 30)
        self.video_entry.setAccessibleName("Campo file Video")  # Set accessible name

        self.video_button = QPushButton("Scegli", self)
        self.video_button.move(350, 20)
        self.video_button.clicked.connect(self.browse_video)
        self.video_button.setAccessibleName("Browse file Video")  # Set accessible name

        self.audio_label = QLabel("File Audio:", self)
        self.audio_label.move(20, 70)
        self.audio_label.resize(100, 30)

        self.audio_entry = QLineEdit(self)
        self.audio_entry.move(130, 70)
        self.audio_entry.resize(200, 30)
        self.audio_entry.setAccessibleName("Campo file Audio")  # Set accessible name

        self.audio_button = QPushButton("Scegli", self)
        self.audio_button.move(350, 70)
        self.audio_button.clicked.connect(self.browse_audio)
        self.audio_button.setAccessibleName("Browse file audio")  # Set accessible name

        self.merge_button = QPushButton("Metti il Wav nel Video", self)
        self.merge_button.resize(200, self.merge_button.height())  # Resizing the button
        self.merge_button.move(130, 120)
        self.merge_button.clicked.connect(self.merge_video_and_audio)
        self.merge_button.setAccessibleName("Tasto esecuzione Metti il Wav nel Video")  # Set accessible name

    def browse_video(self):
        global video_file
        video_file, _ = QFileDialog.getOpenFileName(self, "Scegli il Video", "", "Video Files (*.avi *.mp4 *.mkv *.mov *.wmv *.flv *.webm *.mpeg *.mpg);;All Files (*)")
        self.video_entry.setText(video_file)

    def browse_audio(self):
        global audio_file
        audio_file, _ = QFileDialog.getOpenFileName(self, "Scegli l'audio", "", "Audio Files (*.wav *.aiff *.aif *.aifc);;All Files (*)")
        self.audio_entry.setText(audio_file)

    def run_ffmpeg_remove_audio(self, video_file):
        output_file = os.path.splitext(video_file)[0] + "_noaudio.mkv"
        cmd = f'"{ffmpeg_executable}" -i "{video_file}" -c copy -an "{output_file}"'
        print(cmd)
        subprocess.run(cmd, shell=True)

    def run_ffmpeg_add_audio(self, video_file, audio_file):
        output_file = os.path.splitext(video_file)[0] + "_output.mkv"
        noau = os.path.splitext(video_file)[0] + "_noaudio.mkv"
        cmd = f'"{ffmpeg_executable}" -i "{noau}" -i "{audio_file}" -c copy -map 0 -map 1:a "{output_file}"'
        print(cmd)
        subprocess.run(cmd, shell=True)

    def merge_video_and_audio(self):
        global video_file, audio_file, rimuovi
        self.run_ffmpeg_remove_audio(video_file)
        self.run_ffmpeg_add_audio(video_file, audio_file)
        rimuovi = os.path.splitext(video_file)[0] + "_noaudio.mkv"
        os.remove(rimuovi)
        QMessageBox.information(self, "Il mio lavoro qui è finito!", "Video e audio ora SONO UNA COSA SOLA.")
        self.close()


if __name__ == "__main__":
    app = QApplication([])
    main = MainApp()
    main.setWindowTitle("Metti un WAV nel tuo VIDEO! Cretino!")
    main.show()
    app.exec_()
