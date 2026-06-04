import json
from ..utils import path_resolver
from .runtime_state import RuntimeState
from .validator import RuntimeValidator

def run_validation_audit():
    """
    Minimal Validation Audit MVP.
    Reads existing runtime_state.json and evaluates it using RuntimeValidator.
    Strictly read-only. No mutation.
    """
    state = RuntimeState()
    # We point to the production file by default in RuntimeState
    
    # Map existing JSON fields into RuntimeStateRecord via Alias Layer
    record = state.to_record(source="validation_audit")
    
    validator = RuntimeValidator()
    return validator.validate_runtime_state(record)
