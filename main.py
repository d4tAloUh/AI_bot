from pathlib import Path
from dotenv import load_dotenv
import os

if __name__ == '__main__':
    env_path = Path('.') / 'environment' / '.env'
    load_dotenv(dotenv_path=env_path, verbose=True)
    print("Loaded env file")
    from bot import *

    try:
        if os.getenv("PLATFORM") == 'localhost':
            run_telegram_bot()
        elif os.getenv("PLATFORM") == 'heroku':
            print("Setting webhook")
            set_webhook()
    except:
        run_parser()
