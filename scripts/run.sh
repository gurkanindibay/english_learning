#!/bin/bash
# Quick run script for generating today's listening practice audio

SCRIPT_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"
INPUT_FILE="$SCRIPT_DIR/../toefl/practice/listening_practice_feb8_2026.md"

echo "🎧 Generating audio for today's listening practice..."
echo ""

python3 "$SCRIPT_DIR/generate_listening_audio.py" "$INPUT_FILE"

if [ $? -eq 0 ]; then
    echo ""
    echo "✓ Audio files ready!"
    echo ""
    echo "Play with:"
    echo "  vlc audio_output/*.mp3"
    echo "  or"
    echo "  ffplay audio_output/Library_Research_Consultation.mp3"
fi
