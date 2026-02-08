# English Learning Resources

Personal repository for English language learning materials, focusing on TOEFL preparation and C1-level proficiency.

## 📁 Directory Structure

```
english_learning/
├── grammar/                    # Grammar rules and structures
│   ├── c1_connectors_discourse_markers.md
│   └── c1_key_grammatical_structures.md
│
├── vocabulary/                 # Vocabulary lists and resources
│   └── vocabulary.md
│
├── study_guides/              # Study methods and techniques
│   └── cornell_notes_guide.md
│
├── toefl/                     # TOEFL-specific materials
│   ├── toefl_study_plan.md   # Weekly study plan and strategy
│   ├── practice/             # Practice exercises and tests
│   │   ├── scripts/          # Audio scripts (for generation)
│   │   ├── questions/        # Questions only (for practice)
│   │   ├── answers/          # Answer keys + transcripts (for review)
│   │   └── README.md         # Practice organization guide
│   └── scores/               # Score reports
│       └── TOEFL_Score_Report_1186370.pdf
│
├── scripts/                   # 🎧 Audio generation tools
│   ├── generate_listening_audio.py  # Convert practice to MP3
│   ├── setup.sh              # Quick setup script
│   ├── requirements.txt      # Python dependencies
│   └── README.md             # Detailed usage guide
│
└── .github/
    └── agents/               # GitHub Copilot agent configurations
        ├── grammar_expert.agent.md
        ├── listening_tutor.agent.md
        └── toefl_tutor.agent.md
```

## 📚 Quick Links

### TOEFL Preparation
- **[Study Plan](toefl/toefl_study_plan.md)** - 8-hour weekly plan (10-12 weeks)
- **[Listening Practice Guide](toefl/practice/README.md)** - How to use practice materials
- **[Practice Organization](toefl/practice/)** - Organized into scripts, questions, and answers
  - **Scripts:** Source files for audio generation
  - **Questions:** Practice files (no answers/transcripts)
  - **Answers:** Answer keys with full transcripts for review
- **Current Score:** 90/120 → **Target:** 102/120

### Grammar & Writing
- **[C1 Connectors & Discourse Markers](grammar/c1_connectors_discourse_markers.md)**
- **[C1 Key Grammatical Structures](grammar/c1_key_grammatical_structures.md)**

### Study Resources
- **[Cornell Notes Guide](study_guides/cornell_notes_guide.md)** - Note-taking methodology
- **[Vocabulary](vocabulary/vocabulary.md)** - Word lists and definitions

### 🎧 Audio Generation Tools
- **[Audio Scripts](scripts/)** - Convert listening practice to MP3 with **multiple natural voices**
- **Features:**
  - ✅ Different voices for male/female speakers (auto-detect or custom)
  - ✅ High-quality Microsoft Edge TTS (neural voices)
  - ✅ Natural pauses between speakers
  - ✅ Smart voice assignment (auto-detect from labels or alternate)
  - ✅ Free and open source
- **Quick Start:**
  ```bash
  cd scripts
  python3 -m venv venv  # First time only
  venv/bin/pip install -r requirements.txt  # First time only
  venv/bin/python generate_listening_audio.py ../toefl/practice/scripts/listening_practice_[date]_script.md
  ```
- **See [scripts/README.md](scripts/README.md)** for detailed usage and customization

## 🎯 Current Focus

**Priority Areas:**
- 🎧 **Listening:** 19/30 → 25/30 (CRITICAL)
- 🗣️ **Speaking:** 18/30 → 24/30 (CRITICAL)
- 📖 **Reading:** 25/30 (Maintain)
- ✍️ **Writing:** 28/30 (Maintain)

**Weekly Schedule:** 8 hours
- Weekdays: 1 hour/day
- Weekends: 1.5 hours/day

## 📅 Progress Tracking

| Date | Listening | Speaking | Notes |
|------|-----------|----------|-------|
| Feb 8, 2026 | Started weekly plan | - | Initial organization |

## 🤖 AI Agents

Custom GitHub Copilot agents available in `.github/agents/`:
- **grammar_expert** - Grammar consultation and corrections
- **listening_tutor** - Listening practice and feedback
- **toefl_tutor** - TOEFL-specific guidance and strategies

---

**Last Updated:** February 8, 2026
