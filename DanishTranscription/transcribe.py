import torch
import torchaudio
from transformers import pipeline
import os

def extract_audio(mp4_file, output_wav):
    print("Extracting Audio...")
    video, sample_rate = torchaudio.load(mp4_file)
    torchaudio.save(output_wav, video, sample_rate)

def transcribe_audio(audio_file, model_name):
    print("Transcribing...")
    transcription_pipeline = pipeline(task="automatic-speech-recognition", model=model_name)
    transcript = transcription_pipeline(audio_file)
    print("Done Transcribing")
    return transcript

def main():
    mp4_file = os.path.join("DanishTranscription", "test_video1.mp4")
    output_wav = "output_audio.wav"
    model_name = "openai/whisper-large-v3"
    extract_audio(mp4_file, output_wav)

    transcript = transcribe_audio(output_wav, model_name)

    print("Transcription:")
    print(transcript)

if __name__ == "__main__":
    main()