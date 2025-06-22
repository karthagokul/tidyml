# tidyml

TidyML is a lightweight, human-friendly markup language designed for clean configuration and structured data.

## Usage

```python
from tidyml import parse

text = """
app {
    name = "TidyML"
    version = 1.0
}
"""

data = parse(text)
print(data)
```

## Project Structure

- `tidyml/` – core parser module
- `tests/` – unit tests
- `examples/` – sample `.tml` files


## How to build
### Set up environment
python3 -m venv venv && source venv/bin/activate
pip install .

### Run an example
python run_example.py

### Run tests
pytest tests/

### Build for distribution
python -m build