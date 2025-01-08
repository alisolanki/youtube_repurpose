## This converts any YouTube video to LinkedIn post

### How it works?
- First fetches the transcript of the YouTube video.
- Uses the transcript, settings.py and prompt in prompts.py file to generate a response from Claude AI (Anthropic).
- Stores the response in  `response.txt` and transcript in `transcript.txt`.
- It sends the response to Claude AI to generate an image, saving it as `image.svg`.

### How to install and run?
- Create a .env file.
- Add your ANTHROPIC_API_KEY in it (get it from here: https://console.anthropic.com/settings/keys).
- Tweak settings.py and image_settings.py based on preference.
- Run ```pip3 install requirements.txt``` in the terminal.
- Run ```python3 transcript_to_linkedin.py``` in the terminal.
- To create an image for the post, run ```python3 image_for_post.py``` in the terminal.
