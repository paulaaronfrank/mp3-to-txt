# MP3 to TXT

My sister asked me if there is a way to transcribe audio files. Since I already
have used the Google-Text-to-Speech option I decided to write a quick script. 
This is a simple project to transcribe MP3 files to text.

## Functionality

The program works as follows:

1. Select local mp3 file *
2. Select file audio language *
3. Uploads MP3 to Google Bucket
4. Run Async Speech To Text
5. Download Context
6. Export as text

_\* User action required._

## Getting Started

Create a virtual environment and install the requirements.

> $ virtualenv venv  
> $ source venv/bin/activate
> $ pip install -r requirements.txt

Make sure you have installed tkinter. (available at [python.org](https://www.python.org/))
It is used to create the dialogue fields.

Set your [Google Credentials](https://cloud.google.com/docs/authentication/getting-started) in your environment.

Run the program by calling the `main.py` file.

Afterwards, close your terminal session or `deactivate` the virtual environment. 

### Languages

Languages support can be found in the [Google Documentation](https://cloud.google.com/speech-to-text/docs/languages).
Just add the language options in the list:

> Ln 24 at src/main.py  
`fl = easygui.choicebox("Select a Language", "MP3 to TXT", choices=['de-DE', 'en-US', 'en-CA', 'es-ES'])`

Alternatively, you can modify the script to sample the first 30 seconds of the audio file and 
[detect the language](https://cloud.google.com/translate/docs/basic/detecting-language).

### Encodings

The google API allows different audio encodings. Checkout the enums in "speech_v1p1beta1".
Alternatively, you can modify the script to allow any audio file type and convert the file before uploading.


# MIT License

Copyright (c) 2020 Paul Frank

Permission is hereby granted, free of charge, to any person obtaining a copy
of this software and associated documentation files (the "Software"), to deal
in the Software without restriction, including without limitation the rights
to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
copies of the Software, and to permit persons to whom the Software is
furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all
copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
SOFTWARE.
