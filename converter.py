import pykakasi
import sys

text = sys.argv[1]

kks = pykakasi.kakasi()
kks_result = kks.convert(text)

converted_tokens = [item["hira"] for item in kks_result]
print("".join(converted_tokens))