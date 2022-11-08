import os, openai, json, sys
from random import choices

openai.api_key = os.getenv("OPENAI_API_KEY")

response = openai.Completion.create(
  model="text-davinci-002",
  prompt=sys.argv[1],
  temperature=0.4,
  max_tokens=350,
  top_p=1,
  frequency_penalty=0,
  presence_penalty=0
)
# dump response to json variable
json_response = json.dumps(response, indent=4)

#print text field from json_response
print(json.loads(json_response)['choices'][0]['text'])

# An elaborate, high quality docstring for the above code:
"""
This script is designed to take a prompt from the command line and pass it to the GPT-3 API.
It will then return the top choice from the API as a string to the command line.
The prompt must be wrapped in quotes, and the script should be run from the command line as follows:
python3 askGPT-3.py "This is a prompt for GPT-3"
"""
