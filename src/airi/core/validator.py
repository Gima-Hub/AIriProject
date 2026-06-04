import datetime
import uuid
from .schema import (
    STATUS_VALID, STATUS_INVALID, STATUS_UNKNOWN, STATUS_CONFLICTING, STATUS_STALE,
    RuntimeStateRecord, ValidationResultRecord, EventRecord,
    DriftObservationRecord, SnapshotRecord
)

class RuntimeValidator:
    """
    Provides minimal structure and semantic validation for Runtime Records.
    Pure evaluator: no mutation, no file I/O.
    """

    def __init__(self):
        self.allowed_statuses = {
            STATUS_VALID, STATUS_UNKNOWN, STATUS_CONFLICTING, STATUS_STALE, STATUS_INVALID
        }

    def _create_result(self, target_id: str, status: str, errors: list) -> ValidationResultRecord:
        return ValidationResultRecord(
            id=str(uuid.uuid4()),
            target_id=target_id,
            status=status,
            timestamp=datetime.datetime.now().isoformat(),
            errors=errors
        )

    def validate_runtime_state(self, record: RuntimeStateRecord) -> ValidationResultRecord:
        errors = []
        if not record.id:
            errors.append("Missing record id")
        if record.status not in self.allowed_statuses:
            errors.append(f"Invalid status: {record.status}")
        
        status = STATUS_VALID if not errors else STATUS_INVALID
        return self._create_result(record.id, status, errors)

    def validate_validation_result(self, record: ValidationResultRecord) -> ValidationResultRecord:
        errors = []
        if not record.id:
            errors.append("Missing record id")
        if not record.target_id:
            errors.append("Missing target_id")
        if record.status not in self.allowed_statuses:
            errors.append(f"Invalid status: {record.status}")
            
        status = STATUS_VALID if not errors else STATUS_INVALID
        return self._create_result(record.id, status, errors)

    def validate_event(self, record: EventRecord) -> ValidationResultRecord:
        errors = []
        if not record.id:
            errors.append("Missing record id")
        if not record.event_type:
            errors.append("Missing event_type")
        if record.status not in self.allowed_statuses:
            errors.append(f"Invalid status: {record.status}")
            
        status = STATUS_VALID if not errors else STATUS_INVALID
        return self._create_result(record.id, status, errors)

    def validate_drift_observation(self, record: DriftObservationRecord) -> ValidationResultRecord:
        errors = []
        if not record.id:
            errors.append("Missing record id")
        if record.status not in self.allowed_statuses:
            errors.append(f"Invalid status: {record.status}")
            
        status = STATUS_VALID if not errors else STATUS_INVALID
        return self._create_result(record.id, status, errors)

    def validate_snapshot(self, record: SnapshotRecord) -> ValidationResultRecord:
        errors = []
        if not record.id:
            errors.append("Missing record id")
        if record.status not in self.allowed_statuses:
            errors.append(f"Invalid status: {record.status}")
            
        status = STATUS_VALID if not errors else STATUS_INVALID
        return self._create_result(record.id, status, errors)
