import sounddevice as sd
import soundfile as sf

duration = int(input("Enter the Duration: "))
filename = input("Enter the File name For Saving Your Voice: ")+".mp3"  
sample_rate = 44100  

def record_sound(duration, filename, sample_rate):
    print("Recording...")

    recording = sd.rec(int(duration * sample_rate), samplerate=sample_rate, channels=2, dtype='float64')
    sd.wait()  
    print("Recording finished.")
    
    sf.write(filename, recording, sample_rate)
    print(f"Sound saved as '{filename}'.")

record_sound(duration, filename, sample_rate)