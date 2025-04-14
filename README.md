# HuggingChat Explorer

A simple web application that allows you to test and interact with various language models from Hugging Face's API.

<img src="https://cdn-lfs.hf.co/repos/96/a2/96a2c8468c1546e660ac2609e49404b8588fcf5a748761fa72c154b2836b4c83/9cf16f4f32604eaf76dabbdf47701eea5a768ebcc7296acc1d1758181f71db73?response-content-disposition=inline%3B+filename*%3DUTF-8%27%27hf-logo.png%3B+filename%3D%22hf-logo.png%22%3B&response-content-type=image%2Fpng&Expires=1744635765&Policy=eyJTdGF0ZW1lbnQiOlt7IkNvbmRpdGlvbiI6eyJEYXRlTGVzc1RoYW4iOnsiQVdTOkVwb2NoVGltZSI6MTc0NDYzNTc2NX19LCJSZXNvdXJjZSI6Imh0dHBzOi8vY2RuLWxmcy5oZi5jby9yZXBvcy85Ni9hMi85NmEyYzg0NjhjMTU0NmU2NjBhYzI2MDllNDk0MDRiODU4OGZjZjVhNzQ4NzYxZmE3MmMxNTRiMjgzNmI0YzgzLzljZjE2ZjRmMzI2MDRlYWY3NmRhYmJkZjQ3NzAxZWVhNWE3NjhlYmNjNzI5NmFjYzFkMTc1ODE4MWY3MWRiNzM%7EcmVzcG9uc2UtY29udGVudC1kaXNwb3NpdGlvbj0qJnJlc3BvbnNlLWNvbnRlbnQtdHlwZT0qIn1dfQ__&Signature=kuLQLaI4e0pXAkVPwqlvgFZv9tXGKmFp8H0mezxWZyDCOGWGJO35d3-POkCMOHjGpmYCWExoPy3G0tQSxJ0kdXMkYCG0RiKYaLFXJ1KHAVmV75KlL6HXttmb5ZT2OhzCQTOoGpgUCpIKDMQED1FpKAKQLZ9FC4MVVhYe4%7EQw0wxF-VMaYVF563FAZveWhmP-ToDAbN4EQ-FQvt4JEJGFvoDzUZmuQVdPMETQomNEKlcUgYYCd4d34MktXPq3YRnXbf6p-HPiGPERu6U3D%7EcqSKUGwThheDvg8zvKNlfvxGeITKjCu%7El3-tHNoSh8IUp2UEpa9ZBgLiZzYbzN8rvPkQ__&Key-Pair-Id=K3RPWS32NSSJCE" alt="HuggingChat Explorer Interface" width="150" height="auto" style="display: block; margin: 0 auto;">

## Features

- Chat-like interface for easy interaction with AI models
- Support for multiple Hugging Face language models:
  - Mistral 7B Instruct
  - Llama 2 7B Chat
  - Gemma 7B
  - Falcon 7B Instruct
  - DistilGPT2
  - Flan-T5-Small
  - Falcon RW 1B
- Real-time responses with loading indicator
- Mobile-friendly responsive design
- Simple, clean user interface

## Installation

1. Clone the repository:
   ```
   git clone https://github.com/yourusername/huggingchat-explorer.git
   cd huggingchat-explorer
   ```

2. Create a virtual environment and activate it:
   ```
   python -m venv venv
   source venv/bin/activate  # On Windows: venv\Scripts\activate
   ```

3. Install the required packages:
   ```
   pip install flask requests
   ```

4. Set up your Hugging Face API token:
   - Get your API token from [Hugging Face](https://huggingface.co/settings/tokens)
   - Replace `'your-api-token-here'` in app.py with your actual token

## Usage

1. Run the application:
   ```
   python app.py
   ```

2. Open your web browser and navigate to:
   ```
   http://127.0.0.1:5000/
   ```

3. Select an AI model from the dropdown menu
4. Type your message in the text area
5. Click "Send Message" to get a response from the AI

## Project Structure

```
.
├── app.py                  # Main Flask application
├── templates/              # HTML templates
│   └── index.html          # Main chat interface
└── TESTING/                # Testing directory
    └── api.py              # API testing utilities
```

## Technologies Used

- **Backend**: Flask (Python)
- **Frontend**: HTML, CSS, JavaScript, jQuery, Bootstrap
- **API**: Hugging Face Inference API

## License

[MIT License](LICENSE)


## Acknowledgments

- Built with [Hugging Face](https://huggingface.co/) API
- UI inspired by modern chat applications