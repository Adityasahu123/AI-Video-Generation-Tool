from sumy.parsers.plaintext import PlaintextParser
from sumy.nlp.tokenizers import Tokenizer
from sumy.summarizers.text_rank import TextRankSummarizer
import nltk

# Download needed language data (first time only)
nltk.download("punkt", quiet=True)

# Read the news text saved from Step 1
with open("news_text.txt", "r", encoding="utf-8") as f:
    news_text = f.read()

# Summarize into 6 sentences (good for ~30-60 sec voice)
parser = PlaintextParser.from_string(news_text, Tokenizer("english"))
summarizer = TextRankSummarizer()

summary_sentences = summarizer(parser.document, 6)

script = " ".join(str(s) for s in summary_sentences)

print("\n✅ GENERATED SCRIPT:\n")
print(script)

# Save script for next steps
with open("script.txt", "w", encoding="utf-8") as f:
    f.write(script)

print("\nSaved: script.txt")
