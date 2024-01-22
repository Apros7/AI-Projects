import time
import os
from transformers import SpeechT5Processor, SpeechT5ForTextToSpeech, SpeechT5HifiGan
import torch
from datasets import load_dataset
import pydub
from pydub.playback import play
import soundfile as sf

class Speaker():

    """
    Todo:
    - [ ] Implement natural speech (https://github.com/heatz123/naturalspeech, https://arxiv.org/pdf/2306.07691.pdf)
    - [ ] Use TTS (https://github.com/coqui-ai/TTS) 
    - [ ] Other TTS? (https://github.com/keithito/tacotron?tab=readme-ov-file)
    - [ ] https://ai.gopubby.com/write-for-ai-advances-1c617ad8b28a
    """

    def __init__(self) -> None:
        self.processor = SpeechT5Processor.from_pretrained("microsoft/speecht5_tts")
        self.model = SpeechT5ForTextToSpeech.from_pretrained("microsoft/speecht5_tts")
        self.vocoder = SpeechT5HifiGan.from_pretrained("microsoft/speecht5_hifigan")
        self._load_voice()

    def _load_voice(self):
        embeddings_dataset = load_dataset("Matthijs/cmu-arctic-xvectors", split="validation")
        self.speaker_embeddings = torch.tensor(embeddings_dataset[7306]["xvector"]).unsqueeze(0)

    def speak(self, text, out_loud = True):
        inputs = self.processor(text=text, return_tensors="pt")
        embeddings_dataset = load_dataset("Matthijs/cmu-arctic-xvectors", split="validation")
        speaker_embeddings = torch.tensor(embeddings_dataset[7306]["xvector"]).unsqueeze(0)
        speech = self.model.generate_speech(inputs["input_ids"], speaker_embeddings, vocoder=self.vocoder)
        if out_loud: 
            sf.write("speech.wav", speech.numpy(), samplerate=16000)
            sound = pydub.AudioSegment.from_wav("speech.wav")
            play(sound)

class Aura():
    """
    AURA - Advanced Unrivalled Robotic Advisor
    """
    def __init__(self) -> None:
        self.speaker = Speaker()
        self.speaker.speak("Welcome home! I'm Aura, your personal assistant. I'm here to make your life easier by helping with tasks, providing information, and keeping you organized. If there's anything you need assistance with, feel free to ask!")
        self.speaker.speak("Yoyo")
        self.speaker.speak("Welcome home! I'm Aura, your personal assistant. I'm here to make your life easier by helping with tasks, providing information, and keeping you organized. If there's anything you need assistance with, feel free to ask!")

if __name__ == "__main__":
    Aura()