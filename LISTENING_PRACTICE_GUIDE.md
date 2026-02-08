# Quick Start Guide - Listening Practice System

## 📋 Overview

Your listening practice is now organized into **3 separate files** to prevent accidental peeking at answers while practicing!

## 📁 File Structure

```
toefl/practice/
├── scripts/           # Audio scripts (input for audio generation)
├── questions/         # ⭐ Use this during practice!
├── answers/           # Check only AFTER finishing
└── README.md          # Detailed guide
```

## 🎯 How to Practice

### 1. Start Your Practice Session

Open: `questions/listening_practice_[date]_questions.md`

This file contains:
- ✅ Instructions
- ✅ Audio file paths
- ✅ All questions
- ❌ NO transcripts
- ❌ NO answers

### 2. Listen & Take Notes

```bash
# Play audio from:
scripts/audio_output/Library_Research_Consultation.mp3
scripts/audio_output/Sociology_Gentrification.mp3
```

- Use Cornell-style notes
- Focus on main ideas
- Don't pause or replay!

### 3. Answer Questions

- Answer all questions in the questions file
- Use only your notes
- Calculate your score: ___/16

### 4. Check Your Work

Open: `answers/listening_practice_[date]_answers.md`

This file contains:
- ✅ All answers with explanations
- ✅ Full transcripts
- ✅ Error analysis worksheet
- ✅ Vocabulary lists

## 🎧 Audio Generation

### For New Practice Sessions

When @listening_tutor creates new practice:

```bash
cd scripts
venv/bin/python generate_listening_audio.py \
  ../toefl/practice/scripts/listening_practice_[date]_script.md
```

Output: `scripts/audio_output/[Passage_Name].mp3`

## 📊 Current Practice Available

**February 8, 2026 Practice:**
- 📝 Questions: `questions/listening_practice_feb8_2026_questions.md`
- ✅ Answers: `answers/listening_practice_feb8_2026_answers.md`
- 🎧 Audio: `scripts/audio_output/Library_Research_Consultation.mp3` (4:40)
- 🎧 Audio: `scripts/audio_output/Sociology_Gentrification.mp3` (2:00)

## 💡 Key Benefits

1. **No Cheating:** Can't accidentally see answers during practice
2. **Proper Testing:** Simulates real test conditions
3. **Better Learning:** Forces you to rely on listening skills
4. **Easy Review:** Full transcripts available after practice
5. **Organized:** Clear separation of materials

## 🤖 For @listening_tutor Agent

When creating new practice:

1. Create script: `scripts/listening_practice_[date]_script.md`
2. Generate audio: Run `generate_listening_audio.py`
3. Create questions: `questions/listening_practice_[date]_questions.md` (NO transcripts!)
4. Create answers: `answers/listening_practice_[date]_answers.md` (WITH transcripts)

See detailed workflow in `.github/agents/listening_tutor.agent.md`

## 📚 Related Files

- **[Practice Organization Guide](toefl/practice/README.md)** - Detailed explanation
- **[Audio Generation Guide](scripts/README.md)** - Audio tool documentation
- **[TOEFL Study Plan](toefl_study_plan.md)** - Weekly schedule
- **[Listening Tutor Agent](.github/agents/listening_tutor.agent.md)** - Agent instructions

---

**Remember:** The key to improvement is honest self-evaluation. Don't peek at answers until you finish! 🎯
