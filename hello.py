import os
from pathlib import Path

# same result
print(os.path.abspath(__file__))    # os module provides a more low-level approach.
print(Path(__file__).resolve())     #pathlib module provides a more modern and convenient way to work with file paths