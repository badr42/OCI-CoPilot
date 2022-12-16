# ChatGPT for OCI-CLI

This repository contains a Python script that uses the chatGPT API to translate error messages from the Oracle Cloud Infrastructure (OCI) Command Line Interface (CLI).

## Prerequisites

To use this script, you will need:

- An API key for the chatGPT API. You can sign up for an API key at https://beta.openai.com/signup/.
- The OpenAI Python library installed on your machine. You can install the library using `pip install openai`.

## Usage

To use the script, run the following command, passing it the parameters you'd pass the OCI command:

`
python oci-copilot.py "--my-command"
`


Replace `--my-command` with the OCI-CLI command that you want to run. The script will run the OCI-CLI command and capture the output. It will then pass the output to the chatGPT API as the prompt, and print the response from the API to the console.

Example:

`
python3 oci-c2.py "iam compartment list"
`

## Customization

You can customize the behavior of the script by modifying the code. For example, you can adjust the `temperature` or `top_p` parameters to control the level of randomness in the response from the chatGPT API. You can also add additional command line arguments to the script to specify additional parameters for the OCI-CLI command.

## Contributions

We welcome contributions to this repository. If you have an idea for improving the script, please open an issue or submit a pull request.

## License

This repository is licensed under the [MIT License](LICENSE).

