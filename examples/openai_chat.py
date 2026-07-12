from openai import OpenAI
import glassbox

glassbox.attach()

client = OpenAI()

while True:
    prompt = input("> ")
    if prompt == "exit":
        break

    response = client.chat.completions.create(
        model="gpt-4.1-mini",
        messages=[{"role": "user", "content": prompt}],
    )

    print(response.choices[0].message.content)