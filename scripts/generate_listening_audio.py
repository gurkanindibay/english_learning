#!/usr/bin/env python3
"""
TOEFL Listening Practice Audio Generator

Converts markdown listening practice files to audio with multiple voices.
Uses Microsoft Edge TTS for high-quality, natural text-to-speech with multiple voices.
"""

import re
import os
import sys
import asyncio
import json
from pathlib import Path
from typing import List, Tuple, Dict, Optional
from pydub import AudioSegment
import argparse

try:
    import edge_tts
except ImportError:
    print("Error: edge_tts library not found. Install with: pip install edge-tts")
    sys.exit(1)


class ListeningAudioGenerator:
    """Generate audio files from TOEFL listening practice markdown files."""
    
    # Voice assignments - Using Microsoft Edge TTS natural voices
    VOICE_MAPPING = {
        'female': 'en-US-AriaNeural',      # Female, friendly and clear
        'male': 'en-US-GuyNeural',         # Male, professional and clear
    }
    
    def __init__(self, output_dir: str = 'audio_output', 
                 voice_config: Optional[Dict[str, str]] = None,
                 default_voice: str = 'female',
                 alternate_voices: bool = True):
        """
        Initialize the audio generator.
        
        Args:
            output_dir: Directory for output audio files
            voice_config: Optional dict mapping speaker names to 'male'/'female'
            default_voice: Default voice gender ('male' or 'female')
            alternate_voices: If True, alternate between male/female for unknown speakers
        """
        self.output_dir = Path(output_dir)
        self.output_dir.mkdir(exist_ok=True)
        
        # Custom voice configuration (can be loaded from file or passed in)
        self.voice_config = voice_config or {}
        self.default_voice = default_voice
        self.alternate_voices = alternate_voices
        
        # Track speakers we've seen to enable alternating
        self.speaker_assignments = {}
        self.alternating_index = 0
        
        print("Audio generator initialized with Microsoft Edge TTS!")
        print("Using natural neural voices:")
        print(f"  - Female: {self.VOICE_MAPPING['female']}")
        print(f"  - Male: {self.VOICE_MAPPING['male']}")
        print(f"Voice assignment strategy: ", end="")
        if self.alternate_voices:
            print("Alternating (auto-detect from labels or alternate)")
        else:
            print(f"Default ({self.default_voice})")
        print()
    
    def detect_gender_from_label(self, speaker: str) -> Optional[str]:
        """
        Try to detect gender from speaker label.
        
        Looks for patterns like "Speaker (Female)" or "Speaker (Male)".
        
        Returns:
            'male', 'female', or None if not detected
        """
        speaker_lower = speaker.lower()
        
        # Check for explicit gender markers in parentheses
        if '(female)' in speaker_lower or '(f)' in speaker_lower:
            return 'female'
        elif '(male)' in speaker_lower or '(m)' in speaker_lower:
            return 'male'
        
        return None
    
    def get_speaker_voice(self, speaker: str) -> str:
        """
        Determine which voice to use for a speaker.
        
        Priority order:
        1. Exact match in custom voice_config
        2. Gender detected from speaker label (e.g., "Student (Female)")
        3. Previously assigned voice for this speaker (consistency)
        4. Alternating voices (if enabled)
        5. Default voice
        
        Args:
            speaker: Speaker label from markdown
            
        Returns:
            'male' or 'female'
        """
        # Remove gender markers for cleaner speaker name matching
        clean_speaker = re.sub(r'\s*\([^)]*\)', '', speaker).strip()
        
        # Priority 1: Check custom config for exact match
        if speaker in self.voice_config:
            return self.voice_config[speaker]
        if clean_speaker in self.voice_config:
            return self.voice_config[clean_speaker]
        
        # Priority 2: Try to detect gender from label
        detected_gender = self.detect_gender_from_label(speaker)
        if detected_gender:
            # Cache this assignment for consistency
            self.speaker_assignments[speaker] = detected_gender
            return detected_gender
        
        # Priority 3: Return previously assigned voice
        if speaker in self.speaker_assignments:
            return self.speaker_assignments[speaker]
        if clean_speaker in self.speaker_assignments:
            return self.speaker_assignments[clean_speaker]
        
        # Priority 4: Alternate voices
        if self.alternate_voices:
            gender = 'male' if self.alternating_index % 2 == 0 else 'female'
            self.alternating_index += 1
            self.speaker_assignments[speaker] = gender
            return gender
        
        # Priority 5: Use default
        self.speaker_assignments[speaker] = self.default_voice
        return self.default_voice
    
    def load_voice_config_file(self, config_file: Path):
        """
        Load voice configuration from JSON file.
        
        Expected format:
        {
            "Student": "male",
            "Professor": "female",
            "Librarian": "female"
        }
        """
        try:
            with open(config_file, 'r') as f:
                config = json.load(f)
                self.voice_config.update(config)
                print(f"Loaded voice config from {config_file}")
                print(f"Custom mappings: {config}")
        except Exception as e:
            print(f"Warning: Could not load config file {config_file}: {e}")

        
    def parse_dialogue(self, markdown_file: Path) -> List[Tuple[str, str, str]]:
        """
        Parse markdown file and extract dialogue.
        
        Returns:
            List of tuples: (passage_name, speaker, text)
        """
        with open(markdown_file, 'r', encoding='utf-8') as f:
            content = f.read()
        
        dialogues = []
        current_passage = None
        
        # Pattern to match speaker and their dialogue
        # Matches: **Speaker (Gender):** text
        speaker_pattern = re.compile(r'\*\*([^:]+?):\*\*\s*(.+?)(?=\n\n|\*\*[^:]+?:\*\*|---|$)', re.DOTALL)
        
        # Split into passages
        passages = re.split(r'###\s+🎧\s+Audio Script\s+-\s+(.+?)\n', content)
        
        for i in range(1, len(passages), 2):
            if i + 1 < len(passages):
                passage_name = passages[i].strip()
                passage_content = passages[i + 1]
                
                # Stop at the "---" separator (marks end of dialogue section)
                if '---' in passage_content:
                    passage_content = passage_content.split('---')[0]
                
                # Find all speaker dialogues
                matches = speaker_pattern.findall(passage_content)
                
                for speaker, text in matches:
                    # Clean up the text
                    text = text.strip()
                    text = re.sub(r'\n+', ' ', text)  # Replace newlines with spaces
                    text = re.sub(r'\s+', ' ', text)  # Normalize whitespace
                    
                    # Skip if text is empty or looks like a heading/instruction
                    if text and not text.startswith('---') and len(text) > 10:
                        dialogues.append((passage_name, speaker.strip(), text))
        
        return dialogues
    
    def create_pause(self, duration_ms: int = 1000) -> AudioSegment:
        """Create a silent pause."""
        return AudioSegment.silent(duration=duration_ms)
    
    async def text_to_speech(self, text: str, output_file: Path, speaker_gender: str = 'female'):
        """
        Convert text to speech using Microsoft Edge TTS.
        
        Args:
            text: Text to convert
            output_file: Output file path
            speaker_gender: 'male' or 'female'
        """
        voice = self.VOICE_MAPPING.get(speaker_gender, self.VOICE_MAPPING['female'])
        
        # Generate speech using Edge TTS
        communicate = edge_tts.Communicate(text, voice)
        await communicate.save(str(output_file))
    
    async def generate_passage_audio(self, dialogues: List[Tuple[str, str, str]], 
                              passage_name: str, output_file: Path):
        """
        Generate complete audio for a passage with all speakers.
        
        Args:
            dialogues: List of (passage_name, speaker, text) tuples
            passage_name: Name of the passage to generate
            output_file: Output audio file path
        """
        combined_audio = AudioSegment.empty()
        temp_dir = self.output_dir / 'temp'
        temp_dir.mkdir(exist_ok=True)
        
        passage_dialogues = [d for d in dialogues if d[0] == passage_name]
        
        print(f"\nGenerating audio for: {passage_name}")
        print(f"Found {len(passage_dialogues)} dialogue segments")
        
        for idx, (_, speaker, text) in enumerate(passage_dialogues, 1):
            print(f"  [{idx}/{len(passage_dialogues)}] {speaker}: {text[:50]}...")
            
            # Generate audio for this dialogue
            temp_file = temp_dir / f"temp_{idx}.mp3"
            speaker_gender = self.get_speaker_voice(speaker)
            
            try:
                await self.text_to_speech(text, temp_file, speaker_gender)
                
                # Load the generated audio (Edge TTS creates MP3 files)
                audio_segment = AudioSegment.from_mp3(str(temp_file))
                
                # Add to combined audio
                combined_audio += audio_segment
                
                # Add pause between speakers (0.8 seconds)
                combined_audio += self.create_pause(800)
                
                # Clean up temp file
                temp_file.unlink()
                
            except Exception as e:
                print(f"    Warning: Error generating audio for segment {idx}: {e}")
                continue
        
        # Export final audio
        print(f"  Exporting to {output_file}...")
        combined_audio.export(str(output_file), format='mp3', bitrate='128k')
        
        # Clean up temp directory
        if temp_dir.exists():
            temp_dir.rmdir()
        
        print(f"  ✓ Generated: {output_file}")
        print(f"  Duration: {len(combined_audio) / 1000:.1f} seconds")
    
    async def generate_all_audio(self, markdown_file: Path):
        """Generate audio for all passages in the markdown file."""
        print(f"\n{'='*60}")
        print(f"TOEFL Listening Audio Generator")
        print(f"{'='*60}")
        print(f"Input file: {markdown_file}")
        print(f"Output directory: {self.output_dir}")
        print(f"{'='*60}\n")
        
        # Parse the markdown file
        print("Parsing markdown file...")
        dialogues = self.parse_dialogue(markdown_file)
        
        if not dialogues:
            print("Error: No dialogues found in the file!")
            return
        
        print(f"Found {len(dialogues)} total dialogue segments")
        
        # Get unique passages
        passages = list(set(d[0] for d in dialogues))
        print(f"Found {len(passages)} passages:")
        for p in passages:
            print(f"  - {p}")
        
        # Generate audio for each passage
        for passage in passages:
            safe_name = re.sub(r'[^\w\s-]', '', passage).strip().replace(' ', '_')
            output_file = self.output_dir / f"{safe_name}.mp3"
            
            try:
                await self.generate_passage_audio(dialogues, passage, output_file)
            except Exception as e:
                print(f"\nError generating {passage}: {e}")
                continue
        
        print(f"\n{'='*60}")
        print(f"✓ Audio generation complete!")
        print(f"{'='*60}")
        print(f"Output files saved to: {self.output_dir}")


def main():
    """Main entry point."""
    parser = argparse.ArgumentParser(
        description='Generate audio files from TOEFL listening practice markdown files',
        formatter_class=argparse.RawDescriptionHelpFormatter,
        epilog="""
Examples:
  # Basic usage (auto-detect genders from labels or alternate)
  python generate_listening_audio.py practice.md
  
  # Use custom voice config file
  python generate_listening_audio.py practice.md --config voices.json
  
  # Use only female voice for all speakers
  python generate_listening_audio.py practice.md --default-voice female --no-alternate
  
  # Custom output directory
  python generate_listening_audio.py practice.md -o my_audio
  
Voice config JSON format:
  {
    "Student": "male",
    "Professor": "female",
    "Librarian": "female"
  }
        """
    )
    parser.add_argument(
        'input_file',
        type=str,
        help='Path to the markdown file containing listening practice dialogues'
    )
    parser.add_argument(
        '-o', '--output',
        type=str,
        default='audio_output',
        help='Output directory for generated audio files (default: audio_output)'
    )
    parser.add_argument(
        '-c', '--config',
        type=str,
        help='JSON file with speaker-to-gender mappings (optional)'
    )
    parser.add_argument(
        '--default-voice',
        type=str,
        choices=['male', 'female'],
        default='female',
        help='Default voice gender when gender cannot be determined (default: female)'
    )
    parser.add_argument(
        '--no-alternate',
        action='store_true',
        help='Disable alternating voices; use default voice for all unknown speakers'
    )
    
    args = parser.parse_args()
    
    # Validate input file
    input_path = Path(args.input_file)
    if not input_path.exists():
        print(f"Error: Input file not found: {input_path}")
        sys.exit(1)
    
    # Generate audio
    generator = ListeningAudioGenerator(
        output_dir=args.output,
        default_voice=args.default_voice,
        alternate_voices=not args.no_alternate
    )
    
    # Load custom config if provided
    if args.config:
        config_path = Path(args.config)
        if config_path.exists():
            generator.load_voice_config_file(config_path)
        else:
            print(f"Warning: Config file not found: {config_path}")
    
    asyncio.run(generator.generate_all_audio(input_path))


if __name__ == '__main__':
    main()
