import openai

# Set your OpenAI API key
openai.api_key = "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"

# Create an OpenAI client
client = openai.Completion.create(model='gpt-3.5-turbo-instruct')

# Access the generated text and other information
print(client.choices[0].text)
print(dict(client).get('usage'))
print(client.model_dump_json(indent=2))