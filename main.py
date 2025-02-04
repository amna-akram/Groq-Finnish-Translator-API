from flask import Flask, request, jsonify
import os
from groq import Client

app = Flask(__name__)

groq_api_key = '<api_key>'

client = Client(api_key=groq_api_key)

@app.route('/translate', methods=['POST'])
def translate_text():
    data = request.get_json()
    english_text = data.get('text', '')

    if not english_text:
        return jsonify({'error': 'No text provided for translation'}), 400

    prompt = f"Translate the following text into Finnish, only return the translation: \"{english_text}\""

    try:
        chat_completion = client.chat.completions.create(
        messages=[
            {
                "role": "user",
                "content": prompt,
            }
        ],
            model="llama3-8b-8192",
        )
        print(chat_completion)
        return jsonify({'translated_text': chat_completion.choices[0].message.content.strip()})
    except Exception as e:
        return jsonify({'error': 'Translation failed', 'details': str(e)}), 500

if __name__ == '__main__':
    app.run(debug=True)
