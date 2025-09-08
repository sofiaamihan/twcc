from flask import Flask, render_template, request, jsonify, redirect
import random, time
from threading import Thread

try:
    from gpiozero import LED, Button
    red_led = LED(16)
    green_led = LED(20)
    reset_button = Button(17)
except (ImportError, RuntimeError):
    print("GPIO not available, running in mock mode.")
    class MockLED:
        def on(self): print("LED ON")
        def off(self): print("LED OFF")
    class MockButton:
        # Note: Ignore errors that will run as there is no function to call 
        # Development should still carry out
        pass

    red_led = MockLED()
    green_led = MockLED()
    reset_button = MockButton()


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

def blink_led(led, duration=0.5):
    led.on()
    time.sleep(duration)
    led.off()

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

@app.route('/api/blink', methods=['POST'])
def blink():
    """Blink LEDs depending on match result from frontend"""
    data = request.json
    result = data.get("result") 

    if result == "match":
        Thread(target=blink_led, args=(green_led,)).start()
    else:
        Thread(target=blink_led, args=(red_led,)).start()

    return jsonify({"status": "ok"})

reset_flag = False

def reset_listener():
    global reset_flag
    while True:
        reset_button.wait_for_press()
        print("Reset button pressed ? restarting game")
        blink_led(red_led, 0.2)
        blink_led(green_led, 0.2)
        reset_flag = True   

@app.route('/api/reset-check')
def reset_check():
    global reset_flag
    if reset_flag:
        reset_flag = False
        return jsonify({"reset": True})
    return jsonify({"reset": False})

Thread(target=reset_listener, daemon=True).start()

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5001)
