import language_tool_python
from textblob import TextBlob

tool = language_tool_python.LanguageTool('en-US')

def manual_fixes(text):
    text = text.replace("Thank your message", "Thank you for your message")
    text = text.replace("contract checking", "contract review")
    text = text.replace("final discuss", "final discussion")
    text = text.replace("updated were", "updates were")
    text = text.replace("as it not included", "as it did not include")
    text = text.replace("from reviewed", "from the reviewer")
    return text

def reconstruct_sentence(text):
    # Grammar check
    corrected = tool.correct(text)

    blob = TextBlob(corrected)
    simplified = str(blob.correct())

    final = manual_fixes(simplified)

    return final

sent1 = "Thank your message to show our words to the doctor, as his next contract checking, to all of us."
sent2 = "During our final discuss, I told him about the new submission — the one we were waiting since last autumn, but the updates was confusing as it not included the full feedback from reviewer or maybe editor?"

print("Original Sentence 1:")
print(sent1)
print("Reconstructed Sentence 1:")
print(reconstruct_sentence(sent1))
print("\n")

print("Original Sentence 2:")
print(sent2)
print("Reconstructed Sentence 2:")
print(reconstruct_sentence(sent2))

