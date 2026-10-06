from util.pattern_loader import pattern_dict
from pathlib import Path


def main():
    # Runs every main method
    files_logs()
    for name, cls in pattern_dict.items():
        cls().run()

def files_logs():
    dir = Path('./logs')
    for file in dir.glob("*.log"):
        if file.is_file():
            print(file.name)

if __name__ == "__main__":
    main()
