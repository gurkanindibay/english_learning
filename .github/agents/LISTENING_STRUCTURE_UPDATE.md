# Listening Practice File Structure Update

## Summary of Changes

The listening_tutor agent has been updated to create **a separate directory for each recording** with all related files self-contained within that directory.

## Old Structure ❌

```
toefl/practice/2026-02-08/
├── script.md                    (ALL recordings combined)
├── questions.md                 (ALL recordings combined)
├── answers.md                   (ALL recordings combined)
└── audio/
    ├── Library_Reference_Desk.mp3
    └── Biology_Photosynthesis.mp3
```

**Problems:**
- Hard to find specific recordings
- Must process all recordings together
- Can't practice recordings independently
- Difficult to search for specific content

## New Structure ✅

```
toefl/practice/2026-02-08/
└── listening/
    ├── Library_Reference_Desk/
    │   ├── 1-Library_Reference_Desk-script.md
    │   ├── 2-Library_Reference_Desk-questions.md
    │   ├── 3-Library_Reference_Desk-answers.md
    │   └── Library_Reference_Desk.mp3
    └── Biology_Photosynthesis/
        ├── 1-Biology_Photosynthesis-script.md
        ├── 2-Biology_Photosynthesis-questions.md
        ├── 3-Biology_Photosynthesis-answers.md
        └── Biology_Photosynthesis.mp3
```

**Benefits:**
- ✅ Each recording is completely self-contained
- ✅ Audio file is in the same directory as its materials
- ✅ Easy to search by recording name
- ✅ Numeric prefixes show usage order (1→2→3)
- ✅ Practice recordings independently
- ✅ Clean, logical organization

## File Naming Convention

For each recording, create a dedicated directory containing 4 files:

### **Directory: `listening/[RecordingName]/`**
Each recording gets its own directory under the date's listening folder.

### **`1-[RecordingName]-script.md`**
- **Purpose:** Script for audio generation
- **Use:** FIRST - to generate the audio file
- **Contains:** Only dialogue/lecture with speaker labels
- **Location:** `toefl/practice/YYYY-MM-DD/listening/[RecordingName]/1-[RecordingName]-script.md`
- **Example:** `listening/Library_Reference_Desk/1-Library_Reference_Desk-script.md`

### **`2-[RecordingName]-questions.md`**
- **Purpose:** Practice questions
- **Use:** SECOND - during practice session
- **Contains:** Instructions, questions, note template
- **Does NOT contain:** Transcript or answers
- **Location:** `toefl/practice/YYYY-MM-DD/listening/[RecordingName]/2-[RecordingName]-questions.md`
- **Example:** `listening/Library_Reference_Desk/2-Library_Reference_Desk-questions.md`

### **`3-[RecordingName]-answers.md`**
- **Purpose:** Answer key and review
- **Use:** LAST - after completing practice
- **Contains:** Answers with explanations + full transcript
- **Location:** `toefl/practice/YYYY-MM-DD/listening/[RecordingName]/3-[RecordingName]-answers.md`
- **Example:** `listening/Library_Reference_Desk/3-Library_Reference_Desk-answers.md`

### **`[RecordingName].mp3`**
- **Generated from:** The corresponding `1-[RecordingName]-script.md`
- **Location:** `toefl/practice/YYYY-MM-DD/listening/[RecordingName]/[RecordingName].mp3`
- **Example:** `listening/Library_Reference_Desk/Library_Reference_Desk.mp3`

## Workflow for Creating Practice

### Directory Setup:

1. **Create date and listening directories:**
   ```bash
   mkdir -p toefl/practice/YYYY-MM-DD/listening
   ```

### For Each Recording:

1. **Create recording directory:**
   ```bash
   mkdir -p toefl/practice/YYYY-MM-DD/listening/[RecordingName]
   ```

2. **Create script file:**
   ```bash
   toefl/practice/YYYY-MM-DD/listening/[RecordingName]/1-[RecordingName]-script.md
   ```

3. **Generate audio:**
   ```bash
   cd scripts
   venv/bin/python generate_listening_audio.py \
     ../toefl/practice/YYYY-MM-DD/listening/[RecordingName]/1-[RecordingName]-script.md \
     -o ../toefl/practice/YYYY-MM-DD/listening/[RecordingName]
   ```

4. **Create questions file:**
   ```bash
   toefl/practice/YYYY-MM-DD/listening/[RecordingName]/2-[RecordingName]-questions.md
   ```

5. **Create answers file:**
   ```bash
   toefl/practice/YYYY-MM-DD/listening/[RecordingName]/3-[RecordingName]-answers.md
   ```

6. **Repeat for next recording**

## Student Usage Order

For each recording, students work within its dedicated directory:

```
Navigate to: listening/[RecordingName]/
         ↓
1️⃣ Script (generate audio)
         ↓
    🔊 Audio Generated
         ↓
2️⃣ Questions (practice)
         ↓
    📝 Answer Questions
         ↓
3️⃣ Answers (review)
```

All files for one recording are in one place!

## Search Benefits

Students can now easily search for:
- **All script files:** `find . -name "1-*-script.md"`
- **All question files:** `find . -name "2-*-questions.md"`
- **All answer files:** `find . -name "3-*-answers.md"`
- **Specific recording (all files):** `ls listening/Library_Reference_Desk/*`
- **All recordings for a date:** `ls listening/*/`
- **By usage order:** Files are automatically sorted by prefix within each directory

## Example Search Commands

```bash
# Find all question files across all dates
find toefl/practice -name "2-*-questions.md"

# Find all files for a specific recording across all dates
find toefl/practice -type d -name "Library_Reference_Desk"

# List all recordings for February 8, 2026
ls toefl/practice/2026-02-08/listening/

Output:
Biology_Photosynthesis/
Library_Reference_Desk/

# List all files in a specific recording directory
ls toefl/practice/2026-02-08/listening/Library_Reference_Desk/

Output:
1-Library_Reference_Desk-script.md
2-Library_Reference_Desk-questions.md
3-Library_Reference_Desk-answers.md
Library_Reference_Desk.mp3
```

## Migration Notes

Existing practice files (2026-02-08, 2026-02-09, 2026-02-10) use older structures. New practices from the updated agent will use the new directory-per-recording structure where each recording is completely self-contained in its own directory.

---

**Updated:** February 8, 2026  
**Agent:** listening_tutor  
**Version:** 3.0 - Directory per recording with all files self-contained
