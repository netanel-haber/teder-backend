from csv import reader
from pathlib import Path

dir = Path(__file__).parent

with open(dir / "prompts.csv") as raw_prompts:
    data = reader(raw_prompts)
    prompts = list(data)

if __name__ == "__main__":
    from pprint import pprint

    pprint(prompts)
    for prompt in prompts:
        assert len(prompt) == 2
