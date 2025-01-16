# Music-player
This Python music player project is designed to allow users to easily play, pause, skip, and manage their music collection through a simple yet powerful graphical user interface (GUI). The project leverages popular Python libraries like tkinter, pygame, and os to implement the essential features needed for an enjoyable music-playing experience.

Features:
  -> Core Features 
    -Play/pause functionality 
    -Song switching controls Progress bar 
    -Playlist management Support for multiple audio formats (MP3, WAV)
Play and Pause:

The player supports both play and pause functionality. Users can play music from their local storage or a specified directory. While a song is playing, the play button turns into a pause button, allowing users to pause the track and resume playback at any time.
The music player uses the pygame.mixer module to handle audio playback, ensuring smooth transitions between different states such as playing and pausing.
Stop:

The stop button stops the currently playing music and resets the player to the beginning of the track. This ensures that the next time a user plays a song, it starts from the beginning, providing a seamless experience.
Forward and Previous Buttons:

The forward button allows users to skip to the next song in the playlist or directory, while the previous button takes the user to the previous track in the list. This feature provides a convenient way to navigate through the playlist without manually selecting tracks.
These buttons are fully integrated with the playlist, meaning when you reach the last song, pressing forward will take you back to the first track, and pressing previous from the first song will take you to the last song.
Playlist Management:

Users can create a dynamic playlist from local directories, which automatically loads all the audio files into the list for easy navigation. The playlist is displayed in a GUI list box, where users can select any track to play.
The music player can automatically update the playlist if new music is added to the directory. The playlist also supports removing songs or manually reordering tracks.
Playlist files can be saved, allowing users to create custom collections of their favorite songs.
Volume Control:

The player comes with a built-in volume control, allowing users to adjust the playback volume to their preference. This can be done using a slider or buttons for finer control over the audio output.
Track Display:

The current song’s title is displayed on the GUI, along with track information like artist name (if available in metadata). This helps users stay informed about the song they are currently listening to.
User-Friendly Interface:

The music player has an intuitive and aesthetically pleasing interface built using tkinter. Buttons for play, pause, stop, forward, and previous are clearly laid out, and the current song is displayed prominently.
The GUI includes a tracklist that users can interact with, along with a progress bar showing the current position of the song.
File Format Support:

The music player supports a wide range of audio file formats such as MP3, WAV, and OGG, making it versatile and capable of playing almost all popular audio files.
Users can add their desired music files to the playlist using the file explorer integrated into the GUI.
Error Handling and User Feedback:

The project includes robust error handling, ensuring that if a file cannot be played or loaded (due to corruption, unsupported format, or missing file), the user is notified with an appropriate error message.
Cross-Platform Compatibility:

This music player project is compatible with all major operating systems such as Windows, MacOS, and Linux. It uses cross-platform libraries like tkinter and pygame, ensuring a consistent user experience regardless of the platform.
Key Python Libraries Used:
tkinter:
tkinter is used for creating the graphical user interface (GUI). It provides an easy way to create buttons, sliders, list boxes, labels, and other GUI elements. This makes the music player highly interactive and visually appealing.

pygame:
pygame is responsible for handling the audio playback. The pygame.mixer module is specifically used to load and play sound files, control the volume, and handle playback events such as pause and stop.

os and glob:
These libraries are used for directory and file management, allowing the music player to load audio files from a specified folder and create a playlist dynamically by scanning the directory for supported formats.

tkinter.filedialog:
This module allows the user to open a file explorer window to browse and select audio files to add to the playlist or load a custom playlist file.

time or threading:
Used to manage the song's playback position, such as for updating the progress bar and handling the playing/pausing of music in the background.
