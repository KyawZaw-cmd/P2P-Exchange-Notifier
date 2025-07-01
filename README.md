# P2P-Exchange-Notifier (KyatMax Exchange Bot)

![Python Version](https://img.shields.io/badge/python-3.8%2B-blue.svg)
![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)

Automate the calculation, formatting, and posting of cryptocurrency exchange rates (USDT/MMK, USDT/THB) to Telegram and Facebook. This project is designed for currency exchange businesses and individuals who want to share up-to-date rates with their audience automatically.

---

## Features
- Fetches P2P exchange rates from Binance (via Node.js, not included here)
- Calculates rates with profit margins and tiered pricing
- Generates formatted text and image tables
- Posts rates automatically to Telegram and Facebook (text and image)
- Highly configurable via simple config and text files
- Sample config and data files provided for easy setup

---

## Project Structure
- **Python scripts**: All automation, calculation, and posting logic
- **Sample config/data files**: `.sample.txt` and `.sample.ini` files for safe public sharing
- **No sensitive data or images**: Real data and credentials are excluded by `.gitignore`

---

## Setup

- **Python version required:** 3.8 or higher

1. **Clone the repository**
   ```bash
   git clone https://github.com/KyawZaw-cmd/P2P-Exchange-Notifier.git
   cd P2P-Exchange-Notifier
   ```

2. **Install Python dependencies**
   ```bash
   pip install -r requirements.txt
   ```

3. **Prepare your configuration and data files**
   - Copy the sample files and rename them (remove `.sample`):
     ```bash
     cp config.sample.ini config.ini
     cp buy_answers.sample.txt buy_answers.txt
     cp sell_answers.sample.txt sell_answers.txt
     cp custom_text.sample.txt custom_text.txt
     cp custom_text1.sample.txt custom_text1.txt
     ```
   - Edit `config.ini` and the `.txt` files with your real credentials and custom text.

4. **Add your own image template**
   - Place your `original_image.jpg` in the project root (used for image generation).

---

## Usage

- **Generate and post rates to Telegram (text):**
  ```bash
  python textbot.py
  ```
- **Generate and post rates to Facebook (text):**
  ```bash
  python fbpost.py
  ```
- **Generate image with rates:**
  ```bash
  python photogenerate.py
  ```
- **Post image to Telegram:**
  ```bash
  python telephoto.py
  ```
- **Post image to Facebook:**
  ```bash
  python fbphoto.py
  ```
- **Automate the full workflow:**
  - See scripts like `fbautopost.py`, `fbautophoto.py`, `tautopost.py`, `tautophoto.py`

---

## Configuration

- **config.ini**: API tokens and IDs for Telegram and Facebook
- **buy_answers.txt / sell_answers.txt**: Median price data (from Binance P2P)
- **custom_text.txt / custom_text1.txt**: Custom header/footer for your posts

> **Never commit your real config or data files to public repositories! Use the provided sample files for sharing.**

---

## Security
- All sensitive data is loaded from config files, not hardcoded
- `.gitignore` ensures no real data, credentials, or images are uploaded

---

## License
MIT License

---

## Credits
Developed by KyatMax Exchange. Inspired by the needs of currency exchange automation.
