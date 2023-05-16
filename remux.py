import tkinter as tk
from tkinter import filedialog, messagebox
import os
import subprocess


video_file = ""
audio_file = ""
rimuovi = ""


def browse_video():
    global video_file
    video_file = filedialog.askopenfilename(title="Scegli il Video", filetypes=(("Video files", "*.avi;*.mp4;*.mkv;*.mov;*.wmv;*.flv;*.webm;*.mpeg;*.mpg"), ("All files", "*.*")))
    video_entry.delete(0, tk.END)
    video_entry.insert(0, video_file)

def browse_audio():
    global audio_file
    audio_file = filedialog.askopenfilename(title="Scegli l'audio", filetypes=(("Audio files", "*.wav;*.aiff;*.aif;*.aifc"), ("All files", "*.*")))
    audio_entry.delete(0, tk.END)
    audio_entry.insert(0, audio_file)

def run_ffmpeg_remove_audio(video_file):
    output_file = os.path.splitext(video_file)[0] + "_noaudio.mkv"
    cmd = f"ffmpeg -i {video_file} -c copy -an {output_file}"
    subprocess.run(cmd, shell=True)

def run_ffmpeg_add_audio(video_file, audio_file):
    output_file = os.path.splitext(video_file)[0] + "_output.mkv"
    noau = os.path.splitext(video_file)[0] + "_noaudio.mkv"
    cmd = f"ffmpeg -i {noau} -i {audio_file} -c copy -map 0 -map 1:a {output_file}"
    subprocess.run(cmd, shell=True)

def merge_video_and_audio():
    global video_file, audio_file, rimuovi
    run_ffmpeg_remove_audio(video_file)
    run_ffmpeg_add_audio(video_file, audio_file)
    rimuovi = os.path.splitext(video_file)[0] + "_noaudio.mkv"
    os.remove(rimuovi)
    messagebox.showinfo("Il mio lavoro qui è finito!", "Video e audio ora SONO UNA COSA SOLA.")
    root.destroy()





root = tk.Tk()
root.title("Metti un WAV nel tuo VIDEO! Cretino!")

frame = tk.Frame(root)
frame.pack(padx=10, pady=10)

video_label = tk.Label(frame, text="file Video:")
video_label.grid(row=0, column=0, sticky="e")

video_entry = tk.Entry(frame, width=40)
video_entry.grid(row=0, column=1)

video_browse_button = tk.Button(frame, text="Scegli", command=browse_video)
video_browse_button.grid(row=0, column=2)

audio_label = tk.Label(frame, text="file Audio:")
audio_label.grid(row=1, column=0, sticky="e")

audio_entry = tk.Entry(frame, width=40)
audio_entry.grid(row=1, column=1)

audio_browse_button = tk.Button(frame, text="Scegli", command=browse_audio)
audio_browse_button.grid(row=1, column=2)

merge_button = tk.Button(frame, text="Metti il Wav nel Video", command=merge_video_and_audio)
merge_button.grid(row=2, column=1, pady=10)

root.mainloop()
