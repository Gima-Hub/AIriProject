from dataclasses import dataclass, field
from typing import Dict, Any, List, Optional

# Status Values
STATUS_VALID = "valid"
STATUS_UNKNOWN = "unknown"
STATUS_CONFLICTING = "conflicting"
STATUS_STALE = "stale"
STATUS_INVALID = "invalid"

@dataclass
class RuntimeStateRecord:
    id: str
    type: str = "runtime_state"
    status: str = STATUS_UNKNOWN
    source: str = "state_manager"
    timestamp: str = ""
    focus: str = ""
    safe_mode: bool = False
    locks: Dict[str, Any] = field(default_factory=dict)
    uncertainty: Dict[str, Any] = field(default_factory=dict)

@dataclass
class ValidationResultRecord:
    id: str
    target_id: str
    type: str = "validation_result"
    status: str = STATUS_UNKNOWN
    source: str = "validation_support"
    timestamp: str = ""
    errors: List[str] = field(default_factory=list)
    uncertainty: Dict[str, Any] = field(default_factory=dict)

@dataclass
class EventRecord:
    id: str
    event_type: str
    type: str = "event"
    status: str = STATUS_UNKNOWN
    source: str = "event_recorder"
    timestamp: str = ""
    payload: Dict[str, Any] = field(default_factory=dict)
    uncertainty: Dict[str, Any] = field(default_factory=dict)

@dataclass
class DriftObservationRecord:
    id: str
    type: str = "drift_observation"
    status: str = STATUS_UNKNOWN
    source: str = "drift_observer"
    timestamp: str = ""
    expected_state_id: str = ""
    observed_state_id: str = ""
    drift_details: Dict[str, Any] = field(default_factory=dict)
    uncertainty: Dict[str, Any] = field(default_factory=dict)

@dataclass
class SnapshotRecord:
    id: str
    type: str = "snapshot"
    status: str = STATUS_UNKNOWN
    source: str = "snapshot_support"
    timestamp: str = ""
    state_summary: Dict[str, Any] = field(default_factory=dict)
    included_record_ids: List[str] = field(default_factory=list)
    uncertainty: Dict[str, Any] = field(default_factory=dict)
