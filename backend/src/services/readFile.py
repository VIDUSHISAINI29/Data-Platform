import os
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent

DATA_DIR = ROOT / "data" / "raw" 

def list_files():
    """Lists all supported data files in the folder."""
    supported_extensions = (".csv", ".json", ".xlsx", ".parquet")
    files = [f for f in os.listdir(DATA_DIR) if f.endswith(supported_extensions)]
    return {"files": files}