import os
import random
import time
import openai
from config import apikey

# def openaifunc(msg):
#   openai.api_key = apikey

#   response = openai.ChatCompletion.create(
#     model="gpt-3.5-turbo",
#     messages=[
#       {
#         "role": "user",
#         "content": msg
#       }#,
#       # {
#       #   "role": "assistant",
#       #   "content":msg
#       # }
#     ],
#     temperature=1,
#     max_tokens=256,
#     top_p=1,
#     frequency_penalty=0,
#     presence_penalty=0
#   )
#   print(response)
  #print(response["choices"][0]["message"]["content"])

def openaifunc(msg):
    openai.api_key = apikey

    response = openai.ChatCompletion.create(
        model="gpt-3.5-turbo",
        messages=[
            {
                "role": "user",
                "content": msg
            }
        ],
        temperature=1,
        max_tokens=256,
        top_p=1,
        frequency_penalty=0,
        presence_penalty=0
    )
    # speech("Fetching Results from Chat GPT-3.5 Turbo")
    try:
        openai_results=response["choices"][0]["message"]["content"]
        # if not os.path.exists("openai"):
        #     os.mkdir("openai")
        # with open(f"openai/msg-{random.randint(1,987654)}",'w') as f:
        #     f.write(openai_results)
        print(openai_results)
        # speech(openai_results)
    except Exception as e:
        # speech("Unable to fetch results at the moment")
        print("Unable to fetch results at the moment")
if __name__=="__main__":
  msg="High Paying IT Jobs in 2023"
  openaifunc(msg)
'''
  Result Received when 'response' is printed
  "id": "chatcmpl-7lknWFVNil4eWtdhyJvcelPUuZg9E",
  "object": "chat.completion",
  "created": 1691615662,
  "model": "gpt-3.5-turbo-0613",
  "choices": [
    {
      "index": 0,
      "message": {
        "role": "assistant",
        "content": "data and make intelligent decisions. They work on projects involving natural language processing, computer vision, and predictive modeling.\n\n8. Full Stack 
Developer: Full stack developers have a deep understanding of both front-end and back-end development. They can handle all aspects of software development, from designing user interfaces to building server-side logic.\n\n9. Cloud Architect: As businesses move their operations to the cloud, cloud architects are needed to design and manage cloud infrastructure. They create scalable, secure, and cost-effective cloud solutions for businesses.\n\n10. UI/UX Designer: User interface (UI) and user experience (UX) designers play a crucial role in creating intuitive and visually appealing user interfaces for websites and applications. They focus on creating a seamless user experience and enhancing user satisfaction.\n\n11. Renewable Energy Engineer: With the increasing emphasis on sustainability and renewable energy sources, renewable energy engineers are in high demand. They design, develop, and implement clean energy systems.\n\n12. Data Engineer: Data engineers are responsible for designing and maintaining the infrastructure necessary for data storage and processing. They work on tasks like data modeling, data integration, and ETL (extract, transform, load) processes.\n\n13. Mobile App Developer: With the growing popularity of smartphones and mobile applications, mobile app developers are in demand. They"
      },
      "finish_reason": "length"
    }
  ],
  "usage": {
    "prompt_tokens": 267,
    "completion_tokens": 256,
    "total_tokens": 523
  }
}'''

