from IPython.display import HTML, Audio
from google.colab.output import eval_js
from base64 import b64decode
import numpy as np
from scipy.io.wavfile import read as wav_read
import io
import ffmpeg
import scipy
import whisper
import os
import torch




def get_audio():
  display(HTML(AUDIO_HTML))
  data = eval_js("data")
  binary = b64decode(data.split(',')[1])
  
  process = (ffmpeg
    .input('pipe:0')
    .output('pipe:1', format='wav')
    .run_async(pipe_stdin=True, pipe_stdout=True, pipe_stderr=True, quiet=True, overwrite_output=True)
  )
  output, err = process.communicate(input=binary)
  
  riff_chunk_size = len(output) - 8
  # Break up the chunk size into four bytes, held in b.
  q = riff_chunk_size
  b = []
  for i in range(4):
      q, r = divmod(q, 256)
      b.append(r)

  # Replace bytes 4:8 in proc.stdout with the actual size of the RIFF chunk.
  riff = output[:4] + bytes(b) + output[8:]

  sr, audio = wav_read(io.BytesIO(riff))

  return audio, sr



audio, sr = get_audio()


scipy.io.wavfile.write('recording.wav', sr, audio) 


torch.cuda.is_available()
DEVICE = "cuda" if torch.cuda.is_available() else "cpu"


model = whisper.load_model("medium", device=DEVICE)
print(
    f"Model is {'multilingual' if model.is_multilingual else 'English-only'} "
    f"and has {sum(np.prod(p.shape) for p in model.parameters()):,} parameters."
)


audio = whisper.load_audio("recording.wav")
audio = whisper.pad_or_trim(audio)
mel = whisper.log_mel_spectrogram(audio).to(model.device)


# decode the audio
options = whisper.DecodingOptions()
result = whisper.decode(model, mel, options)

# print the recognized text
print(result.text)


from detoxify import Detoxify
import numpy as np
import seaborn as sns
import pandas as pd
import matplotlib.pyplot as plt


# each model takes in either a string or a list of strings

results = Detoxify('original').predict(result.text)
array = ["percentage"]
np.array(array)
import pandas as pd

df = pd.DataFrame(results, index=array)
print(pd.DataFrame(results, index=array).round(5))
plt.figure(figsize=(10,8))
sns.barplot(data=df,palette=sns.color_palette("pastel"))
plt.title('Stats')
plt.xlabel('Label')
plt.ylabel('Percentage')
plt.show
