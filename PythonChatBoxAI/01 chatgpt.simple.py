import openai

openai.api_key = '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'

completion = openai.ChatCompletion.create(model="gpt-3.5-turbo", messages=[{"role": "user", "content": "Give me 3 ideas for apps I could buikld with openai apis "}])

print(completion.choices[0].message.content)

