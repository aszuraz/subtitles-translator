from pathlib import Path

import deepl

APIKEY = "YOUR_DEEPL_API_KEY"
translator = deepl.Translator(APIKEY)

path_str = input("Path to the .srt file to translate: ").strip().strip('"\'')
srt_path = Path(path_str).expanduser().resolve()

if not srt_path.is_file():
    raise SystemExit(f"Not a file or does not exist: {srt_path}")

out_path = srt_path.with_name(f"{srt_path.stem}.translated{srt_path.suffix}")

result = translator.translate_document_from_filepath(
    str(srt_path),
    output_path=str(out_path),
    target_lang="NL",  # Dutch, or FR, DE, ES, etc.
)
print(f"Saved: {out_path}")



