import gradio as gr
import librosa
import soundfile as sf
import torch
import warnings

from transformers import Wav2Vec2ForCTC, Wav2Vec2Tokenizer

from fastcore.script import call_parse

warnings.filterwarnings("ignore")

#load wav2vec2 tokenizer and model
tokenizer = Wav2Vec2Tokenizer.from_pretrained("facebook/wav2vec2-base-960h")

model = Wav2Vec2ForCTC.from_pretrained("facebook/wav2vec2-base-960h")

# define speech-to-text function
def asr_transcript(audio_file):
    transcript = ""
    speech, fs = sf.read(audio_file.name)
    if len(speech.shape) > 1: 
        speech = speech[:,0] + speech[:,1]
    if fs != 16000:
        speech = librosa.resample(speech, fs, 16000)
    input_values = tokenizer(speech, return_tensors="pt").input_values
    logits = model(input_values).logits
    predicted_ids = torch.argmax(logits, dim=-1)
    transcription = tokenizer.batch_decode(predicted_ids)[0]
    transcript += transcription.lower() + " "
    with open('transcript.txt', 'w+') as f:
        f.write(transcript)
    return "Audio processed! Validating now against our database..."

@call_parse
def main():
  "Launch app"
  gradio_ui = gr.Interface(
      fn=asr_transcript,
      title="Speech-to-Text with HuggingFace+Wav2Vec2",
      description="Upload an audio clip, and let AI do the hard work of transcribing",
      inputs=gr.inputs.Audio(label="Upload Audio File", type="file", source='microphone'),
      outputs=gr.outputs.Textbox(label="Auto-Transcript"),
  )

  gradio_ui.launch()
