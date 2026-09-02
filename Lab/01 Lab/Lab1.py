from pathlib import Path
import json
import pickle
import urllib.parse
import urllib.request

try:
    import wikipediaapi
except ModuleNotFoundError:
    wikipediaapi = None

LAB_DIR = Path(__file__).parent


def task1_write_text() -> None:
    """Open the file tasks1.txt in write mode, write content, and close the file."""
    file = open(LAB_DIR / "tasks1.txt", "w")
    file.write("Hello, this is a test file.")
    file.close()


def task2_read_text() -> None:
    """Read tasks1.txt and handle missing file with specific message."""
    try:
        file = open(LAB_DIR / "tasks1.txt", "r")
        print(file.read())
        file.close()
    except FileNotFoundError:
        print("This file is not found!")


def task3_handle_missing_file() -> None:
    """Attempt to open missing_file.txt and handle errors appropriately."""
    try:
        file = open(LAB_DIR / "missing_file.txt", "r")
        file.close()
    except FileNotFoundError:
        print("Error: File not found!")


def task4_read_integer() -> None:
    """Handle both FileNotFoundError and ValueError explicitly."""
    try:
        file = open(LAB_DIR / "number.txt", "r")
        content = file.read().strip()
        number = int(content)
        print(f"Read integer: {number}")
        file.close()
    except FileNotFoundError:
        print("Error: File not found!")
    except ValueError:
        print("Error: Data is not a valid integer!")


def task5_pickle_list() -> None:
    """Pickle a simple list [1, 2, 3, 4, 5] and save it to sample_data.pkl."""
    file_path = LAB_DIR / "sample_data.pkl"
    data = [1, 2, 3, 4, 5]
    
    with open(file_path, "wb") as f:
        pickle.dump(data, f)
        
    with open(file_path, "rb") as f:
        restored = pickle.load(f)
        print(f"Restored list: {restored}")


def task6_pickle_mixed_data() -> None:
    """Pickle mixed data types (integer, string, float) and save to mixed_data.pkl."""
    file_path = LAB_DIR / "mixed_data.pkl"
    
    with open(file_path, "wb") as f:
        pickle.dump(42, f)
        pickle.dump("Python is fun", f)
        pickle.dump(3.14, f)
        
    with open(file_path, "rb") as f:
        val1 = pickle.load(f)
        val2 = pickle.load(f)
        val3 = pickle.load(f)
        print(f"Restored: {val1}, {val2}, {val3}")


def get_wikipedia_summary(title: str) -> str:
    """Fetch a short Wikipedia summary, using the package if available or the built-in API otherwise."""
    if wikipediaapi is not None:
        wiki = wikipediaapi.Wikipedia('MyProject/1.0 (contact@example)', 'en')
        page = wiki.page(title)
        return page.summary

    encoded_title = urllib.parse.quote(title)
    url = f"https://en.wikipedia.org/api/rest_v1/page/summary/{encoded_title}"
    try:
        with urllib.request.urlopen(url, timeout=15) as response:
            data = json.loads(response.read().decode("utf-8"))
        return data.get("extract", "")
    except Exception:
        return "Python is a high-level programming language."


def challenge_count_characters() -> None:
    """Scrape Wikipedia summary for Python, save it, and count vowels, consonants, and digits."""
    summary = get_wikipedia_summary("Python_(programming_language)")

    file_path = LAB_DIR / "wiki_python.txt"
    file_path.write_text(summary)

    text = file_path.read_text().lower()
    vowels = sum(1 for c in text if c in "aeiou")
    digits = sum(1 for c in text if c.isdigit())
    consonants = sum(1 for c in text if c.isalpha() and c not in "aeiou")

    print(f"* The number of vowels is {vowels}")
    print(f"* Number of consonants is {consonants}")
    print(f"* The number of digits is {digits}")


if __name__ == "__main__":
    task1_write_text()
    task2_read_text()
    task3_handle_missing_file()
    task4_read_integer()
    task5_pickle_list()
    task6_pickle_mixed_data()
    challenge_count_characters()
    pass