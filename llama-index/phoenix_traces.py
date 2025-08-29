# --------------------------------------------------------------
# Getting the llama traces with Phoenix
# depends on: pip install -U llama-index-callbacks-arize-phoenix
# and setting up the whole account for Phoneix Arize
# --------------------------------------------------------------
import llama_index
import os

PHOENIX_API_KEY = "actual-KEY"
os.environ["OTEL_EXPORTER_OTLP_HEADERS"] = f"api_key={actual-KEY}"
llama_index.core.set_global_handler(
        "arize_phoenix",
        endpoints="https://llamatrace.com/v1/traces"
        )
