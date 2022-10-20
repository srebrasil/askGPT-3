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
