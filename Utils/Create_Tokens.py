import json
import sys
import argparse
import os.path


def create_tokens_file(dictionary, filename='tokens.json'):
    with open(filename, 'w') as file:
        json.dump(dictionary, file)

def main():
    env_cookies = json.loads(os.environ['COOKIES'])
    my_tokens = {
        "chrome": env_cookies['chrome'],
        "firefox": env_cookies['firefox'],
        "edge": env_cookies['edge']
    }

    cur_dir = os.path.dirname(os.path.abspath(__file__))
    config = os.path.join(cur_dir, "tokens.json")
    create_tokens_file(my_tokens, config)

if __name__ == "__main__":
    main()