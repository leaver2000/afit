import argparse
import datetime
from pathlib import Path
from dataclasses import dataclass

parser = argparse.ArgumentParser("Date and Path argument parser")

parser.add_argument("--date", help="isoformated date",required=True)
parser.add_argument("--path", help="path to save or load some stuff",required=True)

@dataclass
class Args:
    date:datetime.date
    path:Path
    def __post_init__(self) -> None:
        self.date = datetime.date.fromisoformat(self.date)
        self.path = Path(self.path)

if __name__ == "__main__":
    args = Args(**vars(parser.parse_args()))
    print(args)