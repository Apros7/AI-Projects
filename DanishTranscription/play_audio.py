import pydub

sound = pydub.AudioSegment.from_wav("speech.wav")
pydub.playback.play(sound)