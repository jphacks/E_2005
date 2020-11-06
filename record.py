import pyaudio
import wave
def record():
    chunk = 8194
    FORMAT = pyaudio.paInt16
    CHANNELS = 1
    #サンプリングレート
    RATE = 44100
    p = pyaudio.PyAudio()
    stream = p.open(
        format = FORMAT,
        channels = CHANNELS,
        rate = RATE,
        input = True,
        frames_per_buffer = chunk
    )
    print("=====RECORD START=====")
    all = []
    while True:
        try:
            data = stream.read(chunk)
            all.append(data)
        except KeyboardInterrupt:
            break
    print("=====RECORD END=====")
    stream.close()
    p.terminate()
    data = b''.join(all)
    #保存するファイル名、wは書き込みモード
    out = wave.open('proken.wav','w')
    out.setnchannels(1)
    out.setsampwidth(2)
    out.setframerate(RATE)
    out.writeframes(data)
    out.close()

def transcribe_file():
    from google.cloud import speech
    import io
    client = speech.SpeechClient()

    with io.open('proken.wav', 'rb') as audio_file:
        content = audio_file.read()

    audio = speech.RecognitionAudio(content=content)
    config = speech.RecognitionConfig(
        encoding=speech.RecognitionConfig.AudioEncoding.LINEAR16,
        sample_rate_hertz=44100,
        language_code='ja-JP',
        #audio_channel_count=2,
        enable_separate_recognition_per_channel=True
    )

    operation = client.long_running_recognize(
        request={"config": config, "audio": audio}
    )
    operation = client.long_running_recognize(config=config, audio=audio)
    response = operation.result(timeout=90)

    with io.open("proken.txt", "w", encoding="utf-8") as f:
        for result in response.results:
            f.write(u'{}'.format(result.alternatives[0].transcript))

def send_push_message():
    import requests
    import json
    import io

    with io.open('proken.txt', 'r') as f:
        content = f.read()
        f.close()

    url = 'https://fraud-checker-test.herokuapp.com/raspi'
    headers =  {'Content-Type': 'application/json'}
    payload = {'raspi_id': 'jphacks-e2005-kokokatu', 'content': content}

    res = requests.post(url, data=json.dumps(payload), headers=headers)
    print(res)

if __name__ == '__main__':
    record()
    transcribe_file()
    send_push_message()

