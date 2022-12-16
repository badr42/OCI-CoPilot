import openai
import sys
import subprocess
from subprocess import getoutput

# Get the command from the command line argument
command = sys.argv[1]


#openai.api_key = os.getenv("OPENAI_API_KEY")

# Run the OCI-CLI command and store the output

output = getoutput("oci {VAR}".format(VAR=command))
prompt=output
print(prompt)

if "Error" in output:
    prompt= "explain the following Oracle OCI error in simple english and how to solve it "+prompt.split('\n', 1)[1]
else:
    prompt = "Explain the OCI output "+prompt

# print(prompt)

# Pass the output of the OCI-CLI command as the prompt to the chatGPT API
response = openai.Completion.create(
    engine="text-davinci-002",
    prompt=prompt,
    temperature=0.5,
    max_tokens=1024,
    top_p=1,
    frequency_penalty=0,
    presence_penalty=0
)

# Print the response from the chatGPT API
# print(response["choices"][0]["text"])


# Print the response from the chatGPT API
print("ChatGPT Explenation:  ")
print(response["choices"][0]["text"])