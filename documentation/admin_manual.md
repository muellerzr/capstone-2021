# Administrator Manual

## Speech2Text
To debug issues in relation to the script, adjust `audio2text.py` with the following at the end:

```python
  gradio_ui.launch(debug=True)
```
This will print any errors that occured during inference to the terminal, for you to open a git issue for and report what went wrong