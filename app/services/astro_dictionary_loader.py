from functools import lru_cache
import json
from pathlib import Path

DATA_DIR = Path(__file__).parent.parent / "data" / "astro_dictionary"

@lru_cache
def load_dictionary(name: str) -> dict:
    with open(DATA_DIR / f"{name}.json", "r", encoding="utf-8") as f:
        return json.load(f)
