import argparse
from openai import OpenAI
from dotenv import load_dotenv
import os
import sys

load_dotenv()

parser = argparse.ArgumentParser()
parser.add_argument("in_file_path")
parser.add_argument("--out", default="./out.py", type=str)
args = parser.parse_args()
in_file_path = args.in_file_path
out_file_path = args.out

client = OpenAI(
    api_key=os.getenv('OPENAI_KEY')
)

messages = [
    {"role": "system", "content": "You are ENG2PY the world's first English to Python interpreter. You will take a line of English \"code\" one at a time and spit out the compiled python version of it. Do not respond with any extra text, just the code."}
]


text = open(in_file_path).read()
text = text.split("\n\n")
# print(text)
# for t in text: print(t, '\n')

outputs = []

for t in text:
    stripped = t.strip()
    if(stripped == ''): continue

    messages.append({"role": "user", "content": stripped})
    response = client.chat.completions.create(
        model="gpt-3.5-turbo",
        messages=messages
    )

    generated_code = response.choices[0].message.content
    print(generated_code)
    messages.append({"role": "assistant", "content": generated_code})
    outputs.append(generated_code)

with open(out_file_path, "w") as out_file:
    out_file.write("\n\n".join(outputs))
