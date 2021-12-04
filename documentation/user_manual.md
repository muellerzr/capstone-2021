# User Manual

**Note: Before beginning, ensure you have followed the steps in install_directions.md to ensure you have a stable environment**

## Viewing the Local Interface

**Nick needs to fill out**

## Running the Speech2Text Framework

To start up the server, run the following from the root of the repository:

```bash
python3 deps/audio2text.py
```
You should then see a variety of set up messages appear in your terminal, concluded with "Running on local URL: http://XXX.Y.Z.A:BCDE"

Navigate to that webpage and you will be greeted by a Gradio app.

Potentially enable microphone usage in your web browser.

When you are ready to enter a passphrase of your choosing (it can be anything), hit the "Record" button to start, and again to finish. 

Afterwards hit the yellow "Submit" button.

Once it is done transcribing, you will be greeted with a note that it is being processed by the system (though we are not there yet).

If you now go back to your cloned repository, you should see a "transcription.txt" file, which contains your transcribed text!