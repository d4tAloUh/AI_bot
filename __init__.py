from pathlib import Path
from dotenv import load_dotenv

if __name__ == '__main__':
    env_path = Path('.') / 'environment' / '.env'
    load_dotenv(dotenv_path=env_path, verbose=True)
    print("Loaded env file")
    from bot import run_parser
    from bot import run_telegram_bot
    # run_parser()
    run_telegram_bot()
