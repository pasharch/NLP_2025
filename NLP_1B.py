import nltk
from nltk.tokenize import sent_tokenize
from transformers import pipeline
import language_tool_python
from textblob import TextBlob

nltk.download('punkt')

text1 = """Today is our dragon boat festival, in our Chinese culture, to celebrate it with all safe and great in our lives.
Hope you too, to enjoy it as my deepest wishes. Thank your message to show our words to the doctor, as his next contract checking, to all of us.
I got this message to see the approved message. In fact, I have received the message from the professor, to show me, this, a couple of days ago.
I am very appreciated the full support of the professor, for our Springer proceedings publication."""

text2 = """During our final discuss, I told him about the new submission — the one we were waiting since last autumn,
but the updates were confusing as it not included the full feedback from reviewer or maybe editor?
Anyway, I believe the team, although a bit delay and less communication at recent days, they really tried best for paper and cooperation.      
We should be grateful, I mean all of us, for the acceptance and efforts until the Springer link came finally last week, I think.
Also, kindly remind me please, if the doctor still plans for the acknowledgments section edit before he's sending again.
Because I didn’t see that part final yet, or maybe I missed, I apologize if so.
Overall, let us make sure all are safe and celebrate the outcome with strong coffee and future targets."""


print("PIPELINE 1: Grammar Correction (T5 model only)")

grammar = pipeline("text2text-generation", model="vennify/t5-base-grammar-correction")

def pipeline1(text):
    sentences = sent_tokenize(text)
    results = []
    for s in sentences:
        corrected = grammar(s, max_length=128, do_sample=False)[0]['generated_text']
        if not corrected.strip().endswith(('.', '?', '!')):
            corrected = corrected.strip() + '.'
        results.append(corrected[0].upper() + corrected[1:])
    return " ".join(results)

print("\n Pipeline 1 - Text 1 \n", pipeline1(text1))
print("\n Pipeline 1 - Text 2 \n", pipeline1(text2))



print("PIPELINE 2: LanguageTool + TextBlob")

tool = language_tool_python.LanguageTool('en-US')

def pipeline2(text):
    sentences = sent_tokenize(text)
    results = []
    for s in sentences:
        corrected = tool.correct(s)
        blob = TextBlob(corrected)
        result = str(blob)
        if not result.strip().endswith(('.', '?', '!')):
            result = result.strip() + '.'
        results.append(result[0].upper() + result[1:])
    return " ".join(results)

print("\n Pipeline 2 - Text 1 \n", pipeline2(text1))
print("\n Pipeline 2 - Text 2 \n", pipeline2(text2))



print("PIPELINE 3: BART Paraphrasing")


bart = pipeline("text2text-generation", model="eugenesiow/bart-paraphrase")

def pipeline3(text):
    sentences = sent_tokenize(text)
    results = []
    for s in sentences:
        try:
            out = bart(s, max_length=128, do_sample=False)[0]['generated_text']
            if not out.strip().endswith(('.', '?', '!')):
                out = out.strip() + '.'
            results.append(out[0].upper() + out[1:])
        except Exception as e:
            results.append(s)
    return " ".join(results)

print("\n Pipeline 3 - Text 1 \n", pipeline3(text1))
print("\n Pipeline 3 - Text 2 \n", pipeline3(text2))
