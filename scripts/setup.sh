#!/bin/bash
# Quick setup script for audio generation

echo "======================================"
echo "TOEFL Audio Generator - Setup"
echo "======================================"
echo ""

# Check Python
if ! command -v python3 &> /dev/null; then
    echo "❌ Python 3 is not installed. Please install Python 3.8 or higher."
    exit 1
fi

echo "✓ Python 3 found: $(python3 --version)"

# Check pip
if ! command -v pip3 &> /dev/null; then
    echo "❌ pip3 is not installed. Please install pip3."
    exit 1
fi

echo "✓ pip3 found"

# Check ffmpeg
if ! command -v ffmpeg &> /dev/null; then
    echo "⚠️  ffmpeg not found. Installing..."
    
    if [[ "$OSTYPE" == "linux-gnu"* ]]; then
        sudo apt-get update && sudo apt-get install -y ffmpeg espeak-ng
    elif [[ "$OSTYPE" == "darwin"* ]]; then
        brew install ffmpeg espeak-ng
    else
        echo "❌ Unsupported OS. Please install ffmpeg manually."
        exit 1
    fi
fi

echo "✓ ffmpeg found"

# Install Python packages
echo ""
echo "Installing Python packages..."
pip3 install -r requirements.txt

if [ $? -eq 0 ]; then
    echo ""
    echo "======================================"
    echo "✓ Setup complete!"
    echo "======================================"
    echo ""
    echo "Usage:"
    echo "  python3 generate_listening_audio.py <input_file.md>"
    echo ""
    echo "Example:"
    echo "  python3 generate_listening_audio.py ../toefl/practice/listening_practice_feb8_2026.md"
    echo ""
else
    echo "❌ Installation failed. Please check errors above."
    exit 1
fi
