# GPT-3 Prompt Generator

This project is a simple Python script that uses the OpenAI GPT-3 API to generate text based on a given prompt. The script takes a prompt as a command line argument, passes it to the GPT-3 API, and returns the top choice from the API as a string to the command line.

## Installation

To use this script, you will need to have an OpenAI API key. You can sign up for an API key [here](https://beta.openai.com/signup/).

Once you have your API key, you can set it as an environment variable in your terminal:

```
export OPENAI_API_KEY='your_api_key_here'
```

You will also need to install the `openai` Python package. You can do this using `pip`:

```
pip install openai
```

## Usage

To use the script, simply run it from the command line with a prompt wrapped in quotes:

```
python3 askGPT-3.py "This is a prompt for GPT-3"
```

The script will then pass the prompt to the GPT-3 API and return the top choice as a string to the command line.

## Contributing

If you would like to contribute to this project, feel free to submit a pull request. 

## References

- [OpenAI API documentation](https://beta.openai.com/docs/api-reference/introduction)