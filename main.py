import pyaudio_record as record
import spectrum_freq_scale as scale

record
scale
scale.FrequencyScale("voice.wav", "voice_fscale0.4.wav", 1024, 0.4)
scale.FrequencyScale("voice.wav", "voice_fscale0.8.wav", 1024, 0.8)
scale.FrequencyScale("voice.wav", "voice_fscale1.2.wav", 1024, 1.2)
scale.FrequencyScale("voice.wav", "voice_fscale1.6.wav", 1024, 1.6)
scale.FrequencyScale("voice.wav", "voice_fscale2.0.wav", 1024, 2.0)

