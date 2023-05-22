import os
import openai
from config import apikey

openai.api_key = apikey
response = openai.Completion.create(
  model="text-davinci-003",
  prompt="write a leave apllication to boss\n\nDear [Boss],\n\nI am writing to request an extended leave of absence from [date] to [date]. I must attend to an urgent family matter that cannot wait.\n\nI am happy to work as much as possible in advance of the leave start date to minimize the impact it will have on our team.\n\nThank you for your consideration and I look forward to hearing from you.\n\nSincerely, \n[Your Name]",
  temperature=1,
  max_tokens=256,
  top_p=1,
  frequency_penalty=0,
  presence_penalty=0
)

print(response)
'''
{
  "choices": [
    {
      "finish_reason": "stop",
      "index": 0,
      "logprobs": null,
      "text": ""
    }
  ],
  "created": 1684773702,
  "id": "cmpl-7J2tKzB32EIODDlCZIiFvTOQdtB5T",
  "model": "text-davinci-003",
  "object": "text_completion",
  "usage": {
    "prompt_tokens": 102,
    "total_tokens": 102
  }
}
'''