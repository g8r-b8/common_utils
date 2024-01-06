import dotenv
import os
from pathlib import Path

def load_my_dotenv(module, poetry):
    if poetry:
        path = os.path.abspath(module.__file__)
        dotenv_path = str(Path(path).parent.parent.parent.absolute()) + '/resc/.env'
        dotenv.load_dotenv(dotenv_path)
