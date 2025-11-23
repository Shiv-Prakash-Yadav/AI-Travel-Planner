# project/app.py
from flask import Flask, render_template, request, jsonify
import requests

app = Flask(__name__)

API_KEY = "AIzaSyChnCtzn1Y1L-cuwoHM58xCAenbTIyoKSE"  # Replace with your actual API key
API_URL = f"https://generativelanguage.googleapis.com/v1beta/models/gemini-2.0-flash:generateContent?key={API_KEY}"

def get_itinerary(prompt):
    headers = {
        "Content-Type": "application/json"
    }

    data = {
        "contents": [
            {
                "parts": [
                    {
                        "text": prompt
                    }
                ]
            }
        ]
    }

    try:
        response = requests.post(API_URL, headers=headers, json=data)
        response.raise_for_status()  # Raise HTTPError for bad responses (4xx or 5xx)

        content = response.json()
        return content['candidates'][0]['content']['parts'][0]['text']

    except requests.exceptions.RequestException as e:
        print(f"API Request Error: {e}")
        return f"API Request Error: {e}"
    except (KeyError, IndexError, TypeError, ValueError) as e:
        print(f"Parsing Error: {e}")
        return f"Parsing Error: {e}"
    except Exception as e:
        print(f"General Error: {e}")
        return f"General Error: {e}"

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/plan', methods=['POST'])
def plan_trip():
    data = request.get_json()
    city = data.get('city')
    days = data.get('days', 3)

    prompt = f"Create a {days}-day travel itinerary for {city}, including attractions, food suggestions, and local experiences." # Revert to original prompt.
    itinerary = get_itinerary(prompt)

    return jsonify({"itinerary": itinerary})

if __name__ == '__main__':
    app.run(debug=True)
