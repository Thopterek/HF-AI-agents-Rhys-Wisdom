# ----------------------------------------------
# Simplest way to load data from the local files
# ----------------------------------------------
from llama_index.core import SimpleDirectoryReader

reader = SimpleDirectoryReader(input_dir="path/to/dir")
doc = reader.load_data()
