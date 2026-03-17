# Local AI Telegram Bot

A beginner-friendly local AI chatbot powered by Ollama and Telegram. Run any LLM model on your CPU without needing a GPU.

## Features
- Run any Ollama model locally (Phi3, Mistral, OpenHermes, etc.)
- Chat with your AI via Telegram
- Send messages from terminal
- Fully customizable AI behavior and model selection
- Works on low-resource PCs (tested on i5-6500T with 12GB RAM)
- No cloud dependencies - everything runs locally

## Requirements
- Python 3.8+
- Ollama installed
- 8GB+ RAM (12GB recommended)
- Any modern CPU (GPU not required)

## Installation

### 1. Install Ollama
Download from https://ollama.ai or your distro's package manager:
```bash
# For Arch Linux
sudo pacman -S ollama
sudo systemctl start ollama
```

### 2. Clone this repository
```bash
git clone https://github.com/nandan-g28/local-ai-telegram-bot.git
cd local-ai-telegram-bot
```

### 3. Create a virtual environment
```bash
python -m venv bot_env
source bot_env/bin/activate
```

### 4. Install dependencies
```bash
pip install ollama python-telegram-bot
```

### 5. Get your Telegram Bot Token
1. Open Telegram and search for `@BotFather`
2. Send `/newbot` and follow the steps
3. Copy your token (looks like: `123456789:ABCdefGHIjklmnoPQRstuvwxyz`)

### 6. Configure the bot

Edit `telegram_bot.py` and update:
```python
TOKEN = "YOUR_BOT_TOKEN_HERE"
```

## Choosing Your AI Model

### Available Models

Run this to see available models:
```bash
ollama list
```

Popular options:

| Model | Size | Speed | Quality | Censored? |
|-------|------|-------|---------|-----------|
| phi3 | 2.3GB | Fast | Good | Yes |
| mistral | 4.1GB | Medium | Very Good | Somewhat |
| openhermes | 4GB | Medium | Excellent | No |
| gemma2:2b | 1.3GB | Very Fast | OK | Yes |
| neural-chat | 4.7GB | Medium | Good | No |

### How to Change the Model

1. Pull your desired model:
```bash
ollama pull mistral
# or
ollama pull openhermes
# or any other model from https://ollama.ai/library
```

2. Edit `telegram_bot.py` and find this line:
```python
model='openhermes',
```

3. Replace `'openhermes'` with your model name:
```python
model='mistral',  # or 'phi3', 'neural-chat', etc.
```

4. Save and restart the bot

## Usage

### Start the bot
```bash
source bot_env/bin/activate
python telegram_bot.py
```

### Chat on Telegram
1. Open Telegram
2. Search for your bot name
3. Send any message and chat!

### Customize AI Behavior

Edit the `system_prompt` in `telegram_bot.py`:
```python
{'role': 'system', 'content': 'Your custom instruction here'}
```

Examples:
```python
# For short answers:
{'role': 'system', 'content': 'Keep answers SHORT, under 2-3 sentences.'}

# For detailed answers:
{'role': 'system', 'content': 'Provide detailed, thorough explanations with examples.'}

# For a specific role:
{'role': 'system', 'content': 'You are a Python programming expert. Help users with code.'}
```

## Troubleshooting

### Bot won't start
- Check if Ollama is running: `sudo systemctl status ollama`
- Verify your token is correct
- Check Python version: `python --version` (should be 3.8+)

### Slow responses
- This is normal! CPU inference takes time
- Smaller models (2-3B) are faster but less smart
- Larger models (7B+) are smarter but slower

### Out of memory
- Use a smaller model
- Close other applications
- Check RAM usage: `free -h`

### Port already in use
```bash
killall ollama
sudo systemctl restart ollama
```

## Tips for Best Results

1. **Choose the right model for your hardware:**
   - 12GB RAM: phi3, mistral, openhermes (all good)
   - 8GB RAM: phi3, gemma2:2b (smaller models)
   - Low-end CPU: Use quantized models

2. **Experiment with system prompts** to get different behaviors

3. **Keep Ollama running** in the background for best performance

## Contributing

Feel free to improve this project! Fork, modify, and submit a pull request.

## License

MIT License - Use freely!

## Resources

- Ollama: https://ollama.ai
- Available Models: https://ollama.ai/library
- Telegram Bot API: https://core.telegram.org/bots
- Python-Telegram-Bot: https://python-telegram-bot.readthedocs.io

## Author

Created for learning and experimentation with local LLMs.
