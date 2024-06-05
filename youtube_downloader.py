import tkinter
import customtkinter
from pytube import YouTube

# System Settings
customtkinter.set_appearance_mode("System")
customtkinter.set_default_color_theme("blue")

# Function to update progress bar
def on_progress(stream, chunk, bytes_remaining):
    total_size = stream.filesize
    bytes_downloaded = total_size - bytes_remaining
    percentage_of_completion = (bytes_downloaded / total_size) * 100
    progress_var.set(percentage_of_completion)
    percentage_label.configure(text=f"{percentage_of_completion:.2f}%")

# Function to download video
def download_video():
    url = url_entry.get()
    if url:
        try:
            yt = YouTube(url, on_progress_callback=on_progress)
            stream = yt.streams.get_highest_resolution()
            status_text.set("Downloading...")
            stream.download()
            status_text.set("Download Complete!")
        except Exception as e:
            status_text.set(f"Error: {e}")
    else:
        status_text.set("Please enter a URL")

# App Frame
app = customtkinter.CTk()
app.geometry("720x480")
app.title("YouTube Downloader")

# URL Entry
url_entry = customtkinter.CTkEntry(app, width=400)
url_entry.pack(pady=20)

# Download Button
download_button = customtkinter.CTkButton(app, text="Download", command=download_video)
download_button.pack(pady=20)

# Progress Bar
progress_var = tkinter.DoubleVar()
progress_bar = customtkinter.CTkProgressBar(app, variable=progress_var, width=400)
progress_bar.set(0)  # Initial value
progress_bar.pack(pady=20)

# Percentage Label
percentage_label = customtkinter.CTkLabel(app, text="0.00%")
percentage_label.pack(pady=20)

# Status Label
status_text = tkinter.StringVar()
status_label = customtkinter.CTkLabel(app, textvariable=status_text)
status_label.pack(pady=20)

# Run App
app.mainloop()