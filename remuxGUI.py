import ffmpeg
import tkinter as tk
from tkinter import filedialog

def select_video():
    input_video_path.set(filedialog.askopenfilename(filetypes=[('Video', ('*.mp4', '*.avi', '*.mkv', '*.mov', '*.flv', '*.wmv', '*.webm', '*.m4v', '*.3gp'))]))

def select_audio():
    input_audio_path.set(filedialog.askopenfilename(filetypes=[('WAV audio', '*.wav')]))

def mux_audio_video():
    input_video = input_video_path.get()
    input_audio = input_audio_path.get()
    output_file = input_video[:-4] + '_output.mkv'

    input_stream = ffmpeg.input(input_video)
    input_audio_stream = ffmpeg.input(input_audio)
    ffmpeg.output(input_stream.video, input_audio_stream.audio, output_file, vcodec='copy', acodec='copy').run(overwrite_output=True)

    status_label.config(text='Hai creato il file MKV pronto per essere caricato su YouTube.')

root = tk.Tk()
root.title('Audio Video Muxer')

input_video_path = tk.StringVar()
input_audio_path = tk.StringVar()

video_button = tk.Button(root, text='Seleziona il video', command=select_video)
video_button.pack(pady=10)

audio_button = tk.Button(root, text='Seleziona il WAV audio', command=select_audio)
audio_button.pack(pady=10)

mux_button = tk.Button(root, text='Mux audio e video', command=mux_audio_video)
mux_button.pack(pady=10)

status_label = tk.Label(root, text='')
status_label.pack(pady=10)

root.mainloop()
