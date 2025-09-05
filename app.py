from flask import Flask, render_template, jsonify
import random

app = Flask(__name__)

# Tech career pairs data
CAREER_PAIRS = [
    {"id": "fe", "title": "Frontend Developer", "description": "Builds websites and web apps you see and click"},
    {"id": "da", "title": "Data Analyst", "description": "Turns data into charts, reports, and insights"},
    {"id": "devops", "title": "DevOps Engineer", "description": "Automates builds, testing, and deployments"},
    {"id": "pm", "title": "Product Manager", "description": "Sets product goals and coordinates the team"},
    {"id": "ux", "title": "UX Designer", "description": "Designs flows and screens that feel easy to use"},
    {"id": "sec", "title": "Cybersecurity Analyst", "description": "Protects systems and data from threats"},
]

def shuffle_array(array):
    """Shuffle a copy of the array"""
    copy = array[:]
    random.shuffle(copy)
    return copy

def build_deck(pairs):
    """Build the card deck from pairs"""
    cards = []
    for pair in pairs:
        cards.append({
            "id": pair["id"] + "-t",
            "pairId": pair["id"],
            "kind": "title",
            "text": pair["title"],
            "matched": False
        })
        cards.append({
            "id": pair["id"] + "-d",
            "pairId": pair["id"],
            "kind": "desc",
            "text": pair["description"],
            "matched": False
        })
    return shuffle_array(cards)

@app.route('/')
def index():
    """Main game page"""
    return render_template('index.html')

@app.route('/api/deck')
def get_deck():
    """API endpoint to get a shuffled deck"""
    deck = build_deck(CAREER_PAIRS)
    return jsonify(deck)

@app.route('/api/check-match')
def check_match():
    """API endpoint to check if two cards match"""
    # This would be used for server-side validation if needed
    # For now, we'll keep the client-side logic
    return jsonify({"message": "Use client-side matching"})

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=True)
