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
        audio_channel_count=1,
        enable_separate_recognition_per_channel=True)

    response = client.recognize(config=config, audio=audio)

    with io.open("proken.txt", "w", encoding="utf-8") as f:
        for result in response.results:
            f.write(u'Transcript: {}'.format(result.alternatives[0].transcript))


if __name__ == '__main__':
    transcribe_file()
