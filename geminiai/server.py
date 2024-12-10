from flask import Flask, request, jsonify
from flask_cors import CORS
import google.generativeai as genai

app = Flask(__name__)
CORS(app)  # Allow requests from the React front-end

@app.route('/generate', methods=['POST'])
def generate():
    genai.configure(api_key="API_KEY")
    model = genai.GenerativeModel("gemini-1.5-flash")
    data = request.json
    user_input = data.get("input")
    try:
        result = model.generate_content(user_input)
        response_text = result.text
        
        return jsonify({"response": response_text })
    except Exception as e:
        print(f"Error: {e}")
        return jsonify({"error": "Failed to process the request"}), 500

if __name__ == '__main__':
    app.run(debug=True)