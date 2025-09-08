#!/usr/bin/env python3
"""
Run script for the ITSIG TWCC Game Flask application
This script makes it easy to run the application on a Raspberry Pi
"""

from app import app

if __name__ == '__main__':
    # Run on all interfaces so it can be accessed from other devices on the network
    # Use port 5000 by default, but can be changed if needed
    app.run(host='0.0.0.0', port=5001, debug=False)
