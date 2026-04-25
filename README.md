# Music Visualizer

A pipeline that transforms a song into a painting. It analyzes emotions from lyrics and musical characteristics from audio, then uses a multi-agent GPT-4o loop to generate a detailed description for a painter — which is finally rendered by DALL-E 3.

## How It Works

```
Lyrics → Emotion Analysis (HuggingFace)  ─┐
Audio  → Music Analysis (librosa)         ─┼→ GPT-4o Describer → Critic Loop → DALL-E 3
                                           ┘
```

1. **Emotion analysis** — `j-hartmann/emotion-english-distilroberta-base` classifies emotions from the song's lyrics (anger, joy, sadness, fear, disgust, surprise, neutral)
2. **Music analysis** — librosa extracts tempo (BPM), key, mode (major/minor), and energy level from the audio file
3. **First description** — GPT-4o generates a detailed visual description for a painter based on emotions + music characteristics + lyrics
4. **Critic loop** — GPT-4o critiques the description, then improves it based on the feedback (N iterations)
5. **Image generation** — DALL-E 3 renders the final description

## Example Outputs

### Rammstein — Du Hast
*Emotion: anger 89% | Tempo: 123 BPM | Key: E major | Energy: high*

![Du Hast](examples/du_hast.png)

### Kde domov můj (Czech National Anthem) + Du Hast audio
*Emotion: joy 82% | Tempo: 123 BPM | Key: E major | Energy: high*

![Kde domov muj](examples/kde_domov_muj.png)

## Installation

```bash
pip install transformers torch librosa openai python-dotenv numpy
```

## Configuration

**`.env`** — API key (never commit this file):
```
API_key=your_openai_api_key
```

**`config.ini`** — song and model settings:
```ini
[Song]
Text_of_song = your lyrics here
Path_to_song = /path/to/song.mp3

[Models]
Emotions = j-hartmann/emotion-english-distilroberta-base
Text = gpt-4o
Image = dall-e-3

[General]
Number_of_iterations = 3
```

Prompts for each stage (first description, iterative improvement, critic) are also configurable in `config.ini` under `[Prompts]`.

## Usage

```bash
python Engine.py
```

The script prints emotion analysis, music analysis, each iteration of the description/critique, and the final DALL-E 3 image URL.

## Supported Audio Formats

WAV, MP3, FLAC, OGG. For M4A/AAC install `ffmpeg`.

## Project Structure

```
├── Engine.py               # Orchestrates the full pipeline
├── Configuration_loader.py # Loads config.ini and .env
├── EmotionAnalyzer.py      # Emotion + audio analysis
├── DescriptionMaker.py     # Assembles prompts from templates
├── APIHandler.py           # OpenAI API wrapper
├── config.ini              # Configuration and prompts
└── .env                    # API key (not committed)
```

## Notes

- The emotion model is trained on English — non-English lyrics will produce less accurate results
- DALL-E 3 image URLs expire after 2 hours — save the image locally if needed
- Running costs depend on GPT-4o and DALL-E 3 API usage

## License

MIT
