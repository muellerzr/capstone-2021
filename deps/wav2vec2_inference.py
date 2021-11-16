### ORIGINALLY FROM: https://github.com/oliverguhr/wav2vec2-live/blob/main/wav2vec2_inference.py

import soundfile as sf
import torch
from transformers import Wav2Vec2Processor, Wav2Vec2ForCTC
from fastcore.script import call_parse

# Improvements: 
# - gpu / cpu flag
# - convert non 16 khz sample rates
# - inference time log

class Wave2Vec2Inference():
    "Small inference module to call Wav2Vec2 and get results"
    def __init__(self,model_name):
        self.processor = Wav2Vec2Processor.from_pretrained(model_name) 
        self.model = Wav2Vec2ForCTC.from_pretrained(model_name)

    def buffer_to_text(self,audio_buffer):
        if(len(audio_buffer)==0):
            return ""

        inputs = self.processor([audio_buffer], sampling_rate=16_000, return_tensors="pt", padding=True)

        with torch.no_grad():
            logits = self.model(inputs.input_values, attention_mask=torch.ones(len(inputs.input_values[0]))).logits

        predicted_ids = torch.argmax(logits, dim=-1)        
        transcription = self.processor.batch_decode(predicted_ids)[0]
        return transcription.lower()

    def file_to_text(self,filename):
        audio_input, samplerate = sf.read(filename)
        assert samplerate == 16000
        return self.buffer_to_text(audio_input)

@call_parse
def main():
    print("Model test")
    asr = Wave2Vec2Inference("maxidl/wav2vec2-large-xlsr-german")
    text = asr.file_to_text("test.wav")
    print(text)