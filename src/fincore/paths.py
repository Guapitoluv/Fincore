from pathlib import Path

ROOT = Path(__file__).resolve().parents[2]

DATA = ROOT / "data"
HISTORY = DATA / "history"
GROUP = DATA / "group"

GLOBAL_HISTORY_RECORDS = HISTORY / "global_history_records.json"
HISTORY_RECORDS = HISTORY / "history_records.json"
HISTORY_LOG = HISTORY / "history_log.txt"
HISTORY_CHECKPOINT = HISTORY / "history_checkpoint.txt"

LAST_GROUP = GROUP / "last_group.txt"

MAIN_JSON = DATA / "main.json"

DICTIONARY = DATA / "dictionary" / "dictionary.json"