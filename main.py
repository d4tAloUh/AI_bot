from pathlib import Path
from dotenv import load_dotenv
import os

if __name__ == '__main__':
    env_path = Path('.') / 'environment' / '.env'
    load_dotenv(dotenv_path=env_path, verbose=True)
    print("Loaded env file")

    from bot import *
    # try:
    #     run_telegram_bot()
    # except:
    run_parser()
