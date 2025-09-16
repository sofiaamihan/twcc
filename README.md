# Tech Explorer by ITSIG
A **Digital Kampong Carnival Booth Game** designed and engineered by the **Information Technology Student Interest Group (ITSIG)** of Temasek Polytechnic for the [Tampines West Community Club](https://www.facebook.com/tampineswest/).

This project implements a memory-matching game centred on Information Technology career pathways, architected using Python Flask as the web framework, hosted directly on Raspberry Pi hardware with GPIO-driven LED indicators and button configurations. The system combines lightweight web deployment with embedded hardware interaction to demonstrate the application of the Diploma of Information Technology's application of physical computing and digital interactivity.

<p align="center"> <img src="https://github.com/Troaxx/twcc/blob/main/data/ui.png" alt="UI Screen" height="200px" /> <img src="https://github.com/Troaxx/twcc/blob/main/data/hardware.png" alt="Hardware" height="200px" /> </p>

## Features
- Memory game that pairs IT career roles with their descriptions
- Fully responsive interface, optimised for desktop and mobile browsers
- Clean, dark-themed UI without reliance on external CSS/JS libraries (minimalist inline assets)
- RaspberryPi Hardware integration:
   - LED outputs signal for game match status
   - Reset button inputs
- Lightweight Flask deployment suitable for the same network demonstrations

## Deployment on Normal Desktop
1. Create Virtual Environment
   ```bash
   python3 -m venv development
   ```

2. Run Virtual Environment
   ```bash
   source ./development/bin/activate
   ```

3. Install Dependencies
   ```bash
   pip install -r requirements.txt
   ```

4. Running Code on Terminal
   ```bash
   python3 run.py
   ```

5. Access on Same Device
   - Open your web browser and go to `http://localhost:5001`

6. Access on a Different Device on the SAME Network
   - Open your web browser and go to `http://[PI_IP_ADDRESS]:5000`

7. Housekeeping - Deactivation
   ```bash
   deactivate
   ```

## Deployment on RaspberryPi GUI 
This is dependent on the network connection of your RaspberryPi.
1. Running Code on Terminal
   ```bash
   python3 app.py
   ```

2. Access on Same Device
   - Screen 1: Open your web browser and go to `http://localhost:5001`
   - Screen 2: Open your web browser and go to `http://localhost:5002`

6. Access on a Different Device on the SAME Network
   - Screen 1: Open your web browser and go to `http://http://172.20.10.11/:5001`
   - Screen 2: Open your web browser and go to `http://http://172.20.10.11/:5002`

## Software Packages
This modular integration allows synchronous web interaction while maintaining asynchronous hardware event loops, ensuring smooth gameplay without blocking network I/O.
- `flask` - Provides the HTTP server, routing, JSON-based AJAX endpoints, and templating engine for rendering the UI
- `gpiozero` - Interfaces with Raspberry Pi GPIO pins, allowing LEDs to act as hardware-based feedback mechanisms for user interactions
- `threading` - Enables non-blocking concurrency to manage simultaneous hardware signalling and web request handling
- `random`, `time` - Core Python libraries to generate randomised game states and implement timing controls for animations and LED toggling


## How to Play
1. Click on any card to reveal its hidden role/description
2. Try to match each tech role with its description
3. Cards will turn green and the LED will flash GREEN when correctly matched, otherwise RED
4. Complete all matches to win the game
5. Click "Play again" to start over or click the physical Restart Button 

## Tech Roles Included
- Frontend Developer
- Data Analyst
- DevOps Engineer
- Product Manager
- UX Designer
- Cybersecurity Analyst

## Licensing
This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## Developers
- Daniella Han Xue En [@Troaxx](https://github.com/Troaxx)
- Respeto Sofia Amihan Molase [@sofiaamihan](https://github.com/sofiaamihan)




