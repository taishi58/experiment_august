import streamlit as st
import sounddevice as sd
import numpy as np
import scipy.io.wavfile as wav

fs = 44100  # サンプリングレート
duration = 5  # 録音する秒数

print("録音開始...")
recording = sd.rec(int(duration * fs), samplerate=fs, channels=2, dtype=np.int16)
sd.wait()
print("録音終了")

# wavファイルとして保存
wav.write('output.wav', fs, recording)
