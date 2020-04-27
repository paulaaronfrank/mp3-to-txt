#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
MP3 to TEXT
"""

from google.cloud import speech_v1p1beta1
from google.cloud.speech_v1p1beta1 import enums
from google.cloud import storage
from google.api_core.exceptions import Conflict
from pydub.utils import mediainfo
import easygui

__author__ = "Aaron Frank"
__copyright__ = "Copyright 2020"
__credits__ = ["Aaron Frank"]

__license__ = "MIT"
__version__ = "0.0.1"

# use easygui to get filepath and file name
fp = easygui.fileopenbox("Select Audio File", "MP3 to TXT", filetypes=['*.mp3'])
fl = easygui.choicebox("Select a Language", "MP3 to TXT", choices=['de-DE', 'en-US', 'en-CA', 'es-ES'])
fn = fp.split('/')[-1].split('.')[0]
fi = mediainfo(fp)

# Connect To storage client an upload file to bucket.
storage_client = storage.Client()
speech_client = speech_v1p1beta1.SpeechClient()

try:
    bucket_name = 'mp3-to-speech-audio'  # TODO: Set unique bucket name. [within your organisation]
    bucket = storage_client.create_bucket(bucket_name)
except Conflict:
    bucket = storage_client.get_bucket(bucket_name)
finally:
    blob = bucket.blob('%s.mp3' % fn)
    with open(fp, 'rb') as file:
        blob.upload_from_file(file)

# start gstt in async mode and write to file
operation = speech_client.long_running_recognize({
        "language_code": fl,
        "sample_rate_hertz": int(fi['sample_rate']),
        "encoding": enums.RecognitionConfig.AudioEncoding.MP3,
        "enable_automatic_punctuation": True
    },
    {"uri": 'gs://%s/%s.mp3' % (bucket_name, fn)})


response = operation.result()
with open('./%s.txt' % fn, 'wb') as file:
    for result in response.results:
        file.write(result.alternatives[0].transcript.encode())
