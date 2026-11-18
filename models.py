"""Совместимость на этапе B: модели перенесены в domain."""

from src.domain.entities.university import (
    Course as Course,
)
from src.domain.entities.university import (
    DomainError as DomainError,
)
from src.domain.entities.university import (
    Grade as Grade,
)
from src.domain.entities.university import (
    NotFoundError as NotFoundError,
)
from src.domain.entities.university import (
    State as State,
)
from src.domain.entities.university import (
    StorageError as StorageError,
)
from src.domain.entities.university import (
    Student as Student,
)
from src.domain.entities.university import (
    ValidationError as ValidationError,
)
