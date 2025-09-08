# Tech Explorer by ITSIG
A **Digital Kampong Carnival Booth Game** created by the **Information Technology Student Interest Group** of Temasek Polytechnic. We developed a memory matching game about Information Technology related Careers, run on Python Flask for Raspberry Pi hosting.

<p align="center"> <img src="https://github.com/Troaxx/twcc/blob/main/data/ui.png" alt="UI Screen" height="200px" /> <img src="https://github.com/Troaxx/twcc/blob/main/data/hardware.png" alt="Hardware" height="200px" /> </p>

## Features
- Match IT career roles with their respective descriptions
- Responsive design that works on mobile and desktop
- Clean, modern UI with dark theme
- No external dependencies (all CSS and JavaScript is inline)
- Connected to simple RaspberryPI Hardware LED Functionalities 

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

6. Access on Different Device on the SAME Network
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

6. Access on Different Device on the SAME Network
   - Screen 1: Open your web browser and go to `http://http://172.20.10.11/:5001`
   - Screen 2: Open your web browser and go to `http://http://172.20.10.11/:5002`

## How to Play

1. Click on any card to reveal its content
2. Try to match each tech role with its description
3. Cards will turn green when correctly matched
4. Complete all matches to win the game
5. Click "Play again" to start over

## Tech Roles Included

- Frontend Developer
- Data Analyst
- DevOps Engineer
- Product Manager
- UX Designer

- Cybersecurity Analyst

