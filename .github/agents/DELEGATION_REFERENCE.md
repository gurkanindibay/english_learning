# TOEFL Tutor Agent - Delegation Reference

## How Delegation Works

The TOEFL Tutor agent acts as a **coordinator** that delegates specialized tasks to expert agents using the `runSubagent` tool.

## Delegation Flow

```
User Request → TOEFL Tutor Identifies Task Type → Shows Delegation Message → Calls runSubagent → Expert Agent Handles Task
```

## Example: Listening Practice Request

### User Says:
```
"Create listening practice for February 11"
```

### TOEFL Tutor Should:

1. **Recognize** the keywords: "listening practice", "create listening"
2. **Display** explicit delegation message:
   ```
   🎧 **Delegating to Listening Tutor Agent** for specialized listening practice
   
   The Listening Tutor is specifically designed to create high-quality TOEFL listening 
   materials with academic lectures, campus conversations, and properly formatted questions.
   ```

3. **Execute** delegation using runSubagent:
   ```javascript
   runSubagent({
     description: "Create TOEFL listening practice",
     prompt: "Create listening practice for February 11, 2026 following the existing pattern in toefl/practice/2026-02-XX directories. Include an academic lecture and a campus conversation with questions and answers."
   })
   ```

4. **Result**: The listening_tutor agent receives the request and creates the materials

## Verification Checklist

✅ Delegation message is visible to user (with emoji)
✅ runSubagent tool is called (not just mentioned)
✅ Appropriate expert agent name is used (listening_tutor, writing_coach, etc.)
✅ Full context is passed in the prompt parameter

## Common Delegation Triggers

| User Request Contains | Delegate To | Emoji |
|----------------------|-------------|-------|
| "listening practice", "audio", "lecture" | listening_tutor | 🎧 |
| "writing review", "essay", "score my writing" | writing_coach | ✍️ |
| "speaking practice", "pronunciation" | conversation_partner | 💬 |
| "grammar", "grammar mistake" | grammar_expert | 📖 |
| "add vocabulary", "save words" | vocabulary_expert | 📝 |

## What TOEFL Tutor Handles Directly

- Creating study plans
- Analyzing scores across all sections
- General TOEFL strategies
- Test format guidance
- Progress tracking toward 102+ goal
- Reading practice materials (can create these directly)

## Testing

To verify delegation is working, ask the TOEFL Tutor:
- "I need listening practice" → Should see 🎧 delegation message
- "Review my essay" → Should see ✍️ delegation message
- "Help me practice speaking" → Should see 💬 delegation message

You should see the delegation message BEFORE the specialized agent takes over.
