# Python Code Documentation - KyatMax Money Exchange Automation System

> **SECURITY WARNING:**
> This documentation assumes you use placeholder values in `config.ini` and never commit real API credentials to public repositories. Always keep your credentials private.

## Project Overview

This project is an automated cryptocurrency exchange rate calculation and posting system for KyatMax Money Exchange. The system fetches real-time USDT exchange rates from Binance P2P, calculates profit margins, generates formatted messages with exchange rates, and automatically posts them to Telegram and Facebook platforms.

## System Architecture

The project consists of several interconnected Python modules that work together to:
1. Fetch exchange rate data from Binance P2P
2. Calculate profit margins and exchange rates
3. Generate formatted text messages
4. Create visual images with rate tables
5. Automatically post content to social media platforms

## Core Modules

### 1. `calculate.py` - Exchange Rate Calculator

**Purpose**: Core calculation engine that processes exchange rate data and computes profit margins.

**Key Functions**:
- `get_median_price(file_path)`: Extracts median price from data files
- `get_rate(profit_pct)`: Calculates exchange rates with profit margins

**Input Files**:
- `buy_answers.txt`: Contains USDT to MMK (Myanmar Kyat) exchange data
- `sell_answers.txt`: Contains USDT to THB (Thai Baht) exchange data

**Output**:
- Calculated exchange rates for different transaction tiers
- Table data saved to `table_data.txt`
- Formatted text for posting

**Key Variables**:
- `first`, `second`, `third`: Selling rates for different Baht amounts
- `cas`: Cash/Special Account buying rates (99% of selling rates)
- `old`: Old Account/Kpay buying rates (99% of selling rates + adjustments)

**Rate Calculation Logic**:
```python
# Base calculation: THB to MMK conversion
thb_to_usdt = 1 / usdt_thb
usdt_to_mmk = usdt_mmk
thb_to_mmk = thb_to_usdt * usdt_to_mmk

# Apply profit margin
profit_amount = new_round * profit_pct / 100
final_rate = new_round + profit_amount
```

### 2. `textgenerator.py` - Message Generator

**Purpose**: Generates formatted text messages with current exchange rates and timestamps.

**Features**:
- Imports calculated rates from `calculate.py`
- Reads custom header and footer text from files
- Adds Myanmar timezone timestamps
- Creates two message variants:
  - `f_text`: Full message with rates
  - `f_text1`: Short message for photo captions

**Input Files**:
- `custom_text.txt`: Header message in Myanmar language
- `custom_text1.txt`: Footer message with service details

**Output**:
- `f_text`: Complete formatted message
- `f_text1`: Short message for photo captions

### 3. `photogenerate.py` - Image Generator

**Purpose**: Creates visual images with exchange rate tables overlaid on a template.

**Features**:
- Uses PIL (Python Imaging Library) for image manipulation
- Reads table data from `table_data.txt`
- Overlays exchange rates on `original_image.jpg`
- Adds timestamp to the image
- Saves result as `new_image.jpg`

**Key Parameters**:
- Font: Arial, 26px for table data, 18px for timestamp
- Table position: (280, 357) with 180px column spacing, 100px row spacing
- Timestamp position: (60, 120)

**Dependencies**:
- PIL (Pillow)
- pytz for timezone handling

### 4. `textbot.py` - Telegram Bot

**Purpose**: Sends text messages to Telegram channels using the Telegram Bot API.

**Features**:
- Reads bot configuration from `config.ini`
- Sends formatted messages to specified chat ID
- Includes comprehensive logging to `tbotlog.log`
- Error handling for API failures

**Configuration**:
- Bot token and chat ID stored in `config.ini`
- Target chat: `-1001744319698`

### 5. `telephoto.py` - Telegram Photo Bot

**Purpose**: Sends generated images with captions to Telegram channels.

**Features**:
- Sends `new_image.jpg` with custom caption
- Uses Telegram Bot API for photo uploads
- Includes logging for debugging
- Reads configuration from `config.ini`