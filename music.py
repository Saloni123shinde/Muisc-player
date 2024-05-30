import tkinter as tk
from tkinter import filedialog
import pygame

class MusicPlayer:
    def __init__(self, master):
        self.master = master
        self.master.title("Music Player")
        
        # Initialize Pygame
        pygame.init()
        
        # Create Pygame mixer object
        pygame.mixer.init()
        
        # Variables
        self.song_name = tk.StringVar()
        self.song_name.set("No Song Selected")
        self.volume = tk.DoubleVar()
        self.volume.set(0.5)  # Default volume
        
        # Create Widgets
        self.song_label = tk.Label(master, textvariable=self.song_name)
        self.song_label.pack()
        
        self.play_button = tk.Button(master, text="Play", command=self.play_song)
        self.play_button.pack(side=tk.LEFT)
        
        self.pause_button = tk.Button(master, text="Pause", command=self.pause_song)
        self.pause_button.pack(side=tk.LEFT)
        
        self.stop_button = tk.Button(master, text="Stop", command=self.stop_song)
        self.stop_button.pack(side=tk.LEFT)
        
        self.volume_slider = tk.Scale(master, from_=0, to=1, resolution=0.01, orient=tk.HORIZONTAL, label="Volume", variable=self.volume, command=self.set_volume)
        self.volume_slider.pack(side=tk.LEFT)
        
        self.select_button = tk.Button(master, text="Select Song", command=self.select_song)
        self.select_button.pack(side=tk.LEFT)
        
        # Equalizer controls (Not implemented in this simplified version)
        
    def play_song(self):
        pygame.mixer.music.unpause()
        
    def pause_song(self):
        pygame.mixer.music.pause()
        
    def stop_song(self):
        pygame.mixer.music.stop()
        self.song_name.set("No Song Selected")
        
    def set_volume(self, volume):
        pygame.mixer.music.set_volume(float(volume))
        
    def select_song(self):
        song_path = filedialog.askopenfilename(filetypes=[("MP3 files", "*.mp3")])
        if song_path:
            pygame.mixer.music.load(song_path)
            pygame.mixer.music.play()  # Start playing the song
            self.song_name.set(song_path.split("/")[-1])  # Display only the song name
        
def main():
    root = tk.Tk()
    app = MusicPlayer(root)
    root.mainloop()

if __name__ == "__main__":
    main()
