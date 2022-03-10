# Youtube-Thingspeak python analysis

## Requirements:
+ Python (--version 3.x.x).
+ Requests - Python package (Run `pip install requests` or `pip3 install requests`).

## How to ?:
+ Create a API key from Google cloud platform, Under `APIs & Services` with `Youtube Data API` enabled.
+ Paste the video id (`the last 11 characters of video url`) in the ytVideoid field of `analysis.py` file.
+ Create your Thingspeak channel with `4` fields (viewsCount, likesCount, commentsCount, viewsIncrement).
+ Paste your Google API, Thingspeak APIs and urls in the fields of `analysis.py` file.
+ Run `analysis.py ` file.
+ View video statistics in your Thingspeak channel.
