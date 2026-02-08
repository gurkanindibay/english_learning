# Audio Generation Scripts

Python scripts to convert TOEFL listening practice materials into audio files with **multiple natural voices** (male & female).

## Prerequisites

### System Dependencies

**On Ubuntu/Debian:**
```bash
sudo apt-get update
sudo apt-get install -y python3-pip python3-venv ffmpeg
```

**On macOS:**
```bash
brew install ffmpeg
```

### Python Dependencies

```bash
# Create virtual environment (first time only)
python3 -m venv venv

# Install required packages
venv/bin/pip install -r requirements.txt
```

**Note:** Uses Microsoft Edge TTS - requires internet connection for first use, then caches voices.

## Quick Start

### Basic Usage

```bash
# Activate virtual environment and generate audio
cd scripts
venv/bin/python generate_listening_audio.py ../toefl/practice/listening_practice_feb8_2026.md

# Or use the quick run script
./run.sh
```

### Expected Output

```
audio_output/
├── Library_Research_Consultation.mp3
└── Sociology_Gentrification.mp3
```

## Features

✅ **Realistic multi-voice support** - Different natural voices for male and female speakers  
✅ **High-quality neural TTS** - Microsoft Edge TTS with natural-sounding voices  
✅ **Automatic speaker detection** - Parses markdown and identifies speakers  
✅ **Smart voice assignment** - Auto-detects gender from labels or alternates voices  
✅ **Flexible configuration** - Custom voice mappings via JSON or command-line  
✅ **Natural pauses** - Adds realistic pauses between speakers  
✅ **MP3 output** - Compressed audio files for easy sharing  
✅ **Free and open source** - No API keys or paid services required

### Voice Assignment Strategy

The script assigns voices intelligently using this priority order:

1. **Custom config file** - Your speaker-to-gender mappings (optional)
2. **Auto-detect from labels** - Extracts gender from `"Speaker (Female)"` or `"Speaker (Male)"`
3. **Alternating voices** - Automatically alternates male/female for unknown speakers
4. **Default voice** - Falls back to default (female) if all else fails

**Available voices:**
- **Female**: `en-US-AriaNeural` - Clear, friendly
- **Male**: `en-US-GuyNeural` - Professional, clear  

## Usage Examples

### Basic Usage (Auto-detect or Alternate)

The script automatically detects gender from speaker labels or alternates voices:

```bash
cd scripts
venv/bin/python generate_listening_audio.py ../toefl/practice/listening_practice_feb8_2026.md
```

### Using Custom Voice Configuration

Create a JSON file with your preferred speaker-to-gender mappings:

```bash
# Create voice_config.json
cat > voice_config.json << 'EOF'
{
  "Student": "male",
  "Professor": "female",
  "Librarian": "female",
  "Teaching Assistant": "male"
}
EOF

# Use the config file
venv/bin/python generate_listening_audio.py \
  ../toefl/practice/listening_practice_feb8_2026.md \
  --config voice_config.json
```

See [voice_config.example.json](voice_config.example.json) for a complete example.

### Use Single Voice for All Speakers

If you want all speakers to use the same voice:

```bash
# All female voice
venv/bin/python generate_listening_audio.py practice.md --default-voice female --no-alternate

# All male voice
venv/bin/python generate_listening_audio.py practice.md --default-voice male --no-alternate
```

### Custom Output Directory

```bash
venv/bin/python generate_listening_audio.py practice.md -o my_custom_audio
```

### See All Options

```bash
venv/bin/python generate_listening_audio.py --help
```

### Output will be in `audio_output/` directory

```bash
ls audio_output/
# Library_Research_Consultation.mp3
# Sociology_Gentrification.mp3
```

### Play the audio

```bash
# Using ffplay (from ffmpeg)
ffplay audio_output/Library_Research_Consultation.mp3

# Using VLC
vlc audio_output/*.mp3

# Using any media player
xdg-open audio_output/Library_Research_Consultation.mp3
```

## Customization

### Changing Voice Models

To see all available Edge TTS voices:

```bash
venv/bin/python -c "import asyncio; import edge_tts; asyncio.run(edge_tts.list_voices())"
```

Edit `generate_listening_audio.py` to change the default voices (around line 29):

```python
# Voice assignments - Using Microsoft Edge TTS natural voices
VOICE_MAPPING = {
    'female': 'en-US-AriaNeural',      # Change to any female voice
    'male': 'en-US-GuyNeural',         # Change to any male voice
}
```

### Popular English Voices

**Female voices:**
- `en-US-AriaNeural` - Friendly, clear (default)
- `en-US-JennyNeural` - Professional, warm
- `en-US-MichelleNeural` - Clear, energetic
- `en-GB-SoniaNeural` - British accent

**Male voices:**
- `en-US-GuyNeural` - Professional, clear (default)
- `en-US-EricNeural` - Young, informative
- `en-US-ChristopherNeural` - Mature, authoritative
- `en-GB-RyanNeural` - British accent

### Creating Custom Voice Configurations

Create a JSON file mapping speaker names to genders:

```json
{
  "Student": "male",
  "Professor": "female",
  "Librarian": "female",
  "Teaching Assistant": "male",
  "Advisor": "female"
}
```

Then use it:

```bash
venv/bin/python generate_listening_audio.py practice.md --config my_voices.json
```

**Note:** The script automatically detects gender from labels like `"Student (Female)"` or `"Student (Male)"`, so you only need to configure speakers without explicit gender labels.

### Adjust Speaking Speed

Edge TTS supports rate adjustment. In `generate_listening_audio.py`, modify the `text_to_speech` method:

```python
# Add rate parameter (default: +0%, range: -50% to +100%)
communicate = edge_tts.Communicate(text, voice, rate='+0%')
# Examples: '+10%' (faster), '-10%' (slower)
```

### Adjust Pause Duration

In `generate_listening_audio.py` (around line 190):

```python
# Change pause duration between speakers (in milliseconds)
combined_audio += self.create_pause(800)  # 0.8 seconds (default)
```

## Troubleshooting

### "edge_tts library not found"

```bash
venv/bin/pip install edge-tts
```

### "ffmpeg not found" or audio export fails

```bash
# Ubuntu/Debian
sudo apt-get install ffmpeg

# macOS
brew install ffmpeg
```

### "No dialogues found"

Make sure your markdown file has dialogue in this format:
```markdown
**Speaker (Gender):** Dialogue text here.
```

### First run is slow

Edge TTS downloads voice data on first use. Subsequent runs use cached data and are much faster.

### Want different voice quality

Try different Edge TTS voices:
```bash
# List all available voices
venv/bin/python -c "import asyncio; import edge_tts; asyncio.run(edge_tts.list_voices())"

# Edit VOICE_MAPPING in generate_listening_audio.py
```

## Performance

- **First run**: ~1-2 minutes (downloads voice data)
- **Subsequent runs**: ~20-40 seconds per passage
- **File sizes**: ~1-1.5MB per minute of audio (128kbps MP3)
- **Voice quality**: Neural TTS, very natural sounding

## File Structure

```
scripts/
├── generate_listening_audio.py    # Main script
├── requirements.txt               # Python dependencies
├── voice_config.example.json      # Example voice configuration
├── README.md                      # This file
├── venv/                          # Virtual environment (created by setup)
└── audio_output/                  # Generated audio (created automatically)
    ├── Library_Research_Consultation.mp3
    └── Sociology_Gentrification.mp3
```

## Tips for Best Results

1. **Use headphones** when practicing - better audio quality
2. **Take notes** while listening, just like the real test
3. **Don't replay** - simulate real test conditions
4. **Adjust playback speed** in your media player if needed (0.75x for slower, 1.25x for faster)

## Known Limitations

- Requires internet connection for first use (downloads voice data)
- Cached voices work offline after first download
- Quality depends on internet speed during initial download

## Future Improvements

- [x] Automatic male/female voice assignment ✓
- [x] Natural neural voices ✓
- [ ] Background ambient sounds (library, classroom)
- [ ] Question audio generation
- [ ] Batch processing multiple files
- [ ] Web interface
- [ ] Offline mode (pre-download all voices)

## License

MIT License - Free to use and modify

## Questions or Issues?

Check existing GitHub issues or create a new one in the repository.
