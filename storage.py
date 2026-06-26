import json
import os


def load_json(file_path, default=None):
    """
    Load JSON file.
    If file doesn't exist, create it using default.
    """

    if default is None:
        default = {}

    if not os.path.exists(file_path):
        save_json(file_path, default)
        return default

    try:
        with open(file_path, "r", encoding="utf-8") as f:
            return json.load(f)
    except Exception:
        save_json(file_path, default)
        return default


def save_json(file_path, data):
    """
    Save data to JSON file.
    """

    with open(file_path, "w", encoding="utf-8") as f:
        json.dump(
            data,
            f,
            ensure_ascii=False,
            indent=4
        )


def file_exists(file_path):
    return os.path.exists(file_path)


def delete_file(file_path):
    if os.path.exists(file_path):
        os.remove(file_path)
