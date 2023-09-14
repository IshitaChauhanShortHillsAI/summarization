import spacy

from spacypdfreader.spacypdfreader import pdf_reader
from spacypdfreader.parsers.pytesseract import PytesseractParser
import re
import json

nlp = spacy.load("en_core_web_sm")
doc = pdf_reader("data/gst-ct-38-2023.pdf", nlp, PytesseractParser)


target_page_number = 2
page_text = " ".join(
    token.text for token in doc if token._.page_number == target_page_number
)

paragraphs = re.split(r"\. \n|\n\n", page_text)

formatted_paragraphs = []

print(doc, "\n", paragraphs)

for i, paragraph in enumerate(paragraphs, start=1):
    formatted_paragraph = paragraph.replace("\n", "").strip()
    formatted_paragraphs.append({"index": i, "content": formatted_paragraph})

output_json_file = (
    f"output/ex_pytesseract_formatted_paragraphs_{target_page_number}.json"
)
with open(output_json_file, "w", encoding="utf-8") as json_file:
    json.dump(formatted_paragraphs, json_file, ensure_ascii=False, indent=4)

print(f"Saved {len(formatted_paragraphs)} paragraphs to {output_json_file}")
