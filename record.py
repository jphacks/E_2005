DEVICE_INDEX = 0
CHUNK = 1024
FORMAT = pyaudio.paInt16 # 16bit
CHANNELS = 1             # monaural
RATE = 44100             # sampling frequency [Hz]

time = 5 # record time [s]       
output_path = "proken.wav"

p = pyaudio.PyAudio()

stream = p.open(format=FORMAT,
                channels=CHANNELS,
                rate=RATE,
                input=True,
                input_device_index = DEVICE_INDEX,
                frames_per_buffer=CHUNK)

print("recording ...")

frames = []

while True:
    try:
        data = stream.read(CHUNK)
        frames.append(data)
    except KeyboardInterrupt:
        break
        
        
print("done.")

stream.stop_stream()
stream.close()
p.terminate()

wf = wave.open(output_path, 'wb')
wf.setnchannels(CHANNELS)
wf.setsampwidth(p.get_sample_size(FORMAT))
wf.setframerate(RATE)
wf.writeframes(b''.join(frames))
wf.close()
