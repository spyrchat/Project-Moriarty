# Project-Moriarty
![logo](https://user-images.githubusercontent.com/79098250/196054331-e06a169e-a848-4266-9943-b5424eccd63d.png)

We are building solutions to stop harrashment and hate speech in online voice communication. The project's goal in this state, is to take user input using the default system microphone and transcode the speech to text. After that a model (unitaryai/detoxify) is used to classify the text produced from whisper as toxic, severe_toxic, obscene, threat, insult, identity_atttack.
## OpenAI Whisper Hackathon

This project was build as project for openAI's Whisper hackathon. We intend to continue working on it in order to implement more useful features such as Real Time Speech Recognition, Multilinguality and more

Here is a link with our presentation: https://www.canva.com/design/DAFPGvMqwIk/KbN69ps29X0USU02Uip_wA/view?website#4:intro

## Whisper 

Whisper is a general-purpose speech recognition model. It is trained on a large dataset of diverse audio and is also a multi-task model that can perform multilingual speech recognition as well as speech translation and language identification.

![image](https://user-images.githubusercontent.com/79098250/196047216-c2974db6-b355-4cd1-b27a-551e3bca8b40.png)

A Transformer sequence-to-sequence model is trained on various speech processing tasks, including multilingual speech recognition, speech translation, spoken language identification, and voice activity detection. All of these tasks are jointly represented as a sequence of tokens to be predicted by the decoder, allowing for a single model to replace many different stages of a traditional speech processing pipeline. The multitask training format uses a set of special tokens that serve as task specifiers or classification targets.


## Available models and languages

There are five model sizes, four with English-only versions, offering speed and accuracy tradeoffs. Below are the names of the available models and their approximate memory requirements and relative speed. 


|  Size  | Parameters | English-only model | Multilingual model | Required VRAM | Relative speed |
|:------:|:----------:|:------------------:|:------------------:|:-------------:|:--------------:|
|  tiny  |    39 M    |     `tiny.en`      |       `tiny`       |     ~1 GB     |      ~32x      |
|  base  |    74 M    |     `base.en`      |       `base`       |     ~1 GB     |      ~16x      |
| small  |   244 M    |     `small.en`     |      `small`       |     ~2 GB     |      ~6x       |
| medium |   769 M    |    `medium.en`     |      `medium`      |     ~5 GB     |      ~2x       |
| large  |   1550 M   |        N/A         |      `large`       |    ~10 GB     |       1x       |

For English-only applications, the `.en` models tend to perform better, especially for the `tiny.en` and `base.en` models. We observed that the difference becomes less significant for the `small.en` and `medium.en` models. 
## Credits
Athanasiadou Christina ECE AUTH, https://github.com/christina-ath

Chatzigeorgiou Spiros ECE AUTH, https://github.com/Themanwhosoldtheworldd 

Whisper: https://github.com/openai/whisper

Detoxify: https://github.com/unitaryai/detoxify






