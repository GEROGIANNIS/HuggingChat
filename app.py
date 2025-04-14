from flask import Flask, render_template, request, jsonify
import requests
import json

app = Flask(__name__)

# Define your Hugging Face API token
API_TOKEN = 'your-api-token-here'  # Replace with your actual token

headers = {
    "Authorization": f"Bearer {API_TOKEN}"
}

# Define available models and their base URLs
MODELS = {
    "mistralai/Mistral-7B-Instruct-v0.1": "https://api-inference.huggingface.co/models/mistralai/Mistral-7B-Instruct-v0.1",
    "meta-llama/Llama-2-7b-chat-hf": "https://api-inference.huggingface.co/models/meta-llama/Llama-2-7b-chat-hf",
    "google/gemma-7b-it": "https://api-inference.huggingface.co/models/google/gemma-7b-it",
    "tiiuae/falcon-7b-instruct": "https://api-inference.huggingface.co/models/tiiuae/falcon-7b-instruct",
    "distilbert/distilgpt2": "https://api-inference.huggingface.co/models/distilbert/distilgpt2",
    "google/flan-t5-small": "https://api-inference.huggingface.co/models/google/flan-t5-small",
    "tiiuae/falcon-rw-1b": "https://api-inference.huggingface.co/models/tiiuae/falcon-rw-1b"
}

def query_huggingface_api(prompt, model_id):
    """Send a query to the Hugging Face API with the selected model."""
    api_url = MODELS.get(model_id, MODELS["mistralai/Mistral-7B-Instruct-v0.1"])
    
    # Format the prompt properly based on model
    if "mistral" in model_id.lower():
        formatted_prompt = f"<s>[INST] {prompt} [/INST]"
    else:
        formatted_prompt = prompt
    
    payload = {"inputs": formatted_prompt, "parameters": {"max_new_tokens": 512, "return_full_text": False}}
    
    try:
        response = requests.post(api_url, headers=headers, json=payload, timeout=90)
        
        if response.status_code == 200:
            try:
                result = response.json()
                
                # Extract the generated text based on response format
                if isinstance(result, list) and len(result) > 0:
                    if 'generated_text' in result[0]:
                        return result[0]['generated_text']
                    else:
                        return str(result[0])
                elif isinstance(result, dict):
                    if 'generated_text' in result:
                        return result['generated_text']
                    else:
                        return str(result)
                else:
                    return str(result)
            except Exception as e:
                return f"Error processing response: {str(e)}"
        else:
            if response.status_code == 503:
                return "The model is currently loading. Please try again in a moment."
            return f"Error: {response.status_code} - {response.text}"
    except requests.exceptions.Timeout:
        return "Request timed out. The model might be loading or experiencing high traffic."
    except Exception as e:
        return f"Error connecting to API: {str(e)}"

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/query', methods=['POST'])
def query():
    user_input = request.form.get('inputs', '')
    model_id = request.form.get('model', 'mistralai/Mistral-7B-Instruct-v0.1')
    
    response = query_huggingface_api(user_input, model_id)
    
    # Check if this is an AJAX request
    if request.headers.get('X-Requested-With') == 'XMLHttpRequest':
        return jsonify({'response': response})
    else:
        return render_template('index.html', response=response, user_input=user_input)

if __name__ == "__main__":
    app.run(debug=True)