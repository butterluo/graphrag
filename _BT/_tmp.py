import os
from openai import AzureOpenAI

client = AzureOpenAI(
  api_key = 'ab31f8caee164b7391f761955cdf0904',  
  api_version = "2024-02-01",
  azure_endpoint = 'https://aoai-tst1.openai.azure.com/'
)

response = client.chat.completions.create(
    model="gpt-4", # model = "deployment_name".
    messages=[
        {"role": "system", "content": "Assistant is a large language model trained by OpenAI."},
        {"role": "user", "content": "Who were the founders of Microsoft?"}
    ]
)

#print(response)
print(response.model_dump_json(indent=2))
print(response.choices[0].message.content)