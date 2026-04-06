# SRT Translator (DeepL)

Easily translate your subtitles to a native language of choice using the DeepL API. The DeepL free API-plan offers 500K Chars per month free which is better than using a paid service like ChatGPT or something.
Translation works just as good if not better and based on the 500K Chars you can easily translate multiple films (currently translated well over 10H+ of movies including endings). 

See more here: https://www.deepl.com/en/pro/change-plan#developer

## What This Project Does

- Translates an `.srt` subtitle file with DeepL.
- Prompts you for the subtitle file path each time you run it.
- Saves the translated subtitle next to the original file.
- Includes a helper script to count subtitle characters.

## Files

- `translate.py` - Translate a subtitle file using DeepL.
- `srt_char_count.py` - Count characters in an `.srt` file.

## Requirements

- Python 3.9+
- A DeepL API key
- Python package: `deepl`

Install dependency:

```bash
pip install deepl
```

## Setup

Open `translate.py` and set your API key at the top:

```python
APIKEY = "YOUR_DEEPL_API_KEY"
```

## Usage

Run the translator:

```bash
python3 translate.py
```

Then paste/type the path to your `.srt` file when prompted.

Current default target language in `translate.py`:

```python
target_lang="NL" #as as example. 
```

The output filename format is:

- `<original_name>.translated.srt`

Example:

- `movie.srt` -> `movie.nl.srt`

## Character Counter (Optional)

Count total characters in the file:

```bash
python3 srt_char_count.py /path/to/file.srt
```

Count subtitle text only (excluding cue numbers/timestamps):

```bash
python3 srt_char_count.py --text-only /path/to/file.srt
```

## Notes

- Keep your API key private.
- If needed, change `target_lang` in `translate.py` to another DeepL language code.
