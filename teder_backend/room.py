from dataclasses import dataclass, asdict
from enum import Enum, auto


class RoomState(Enum):
    # TODO rename later
    FETUS = auto()
    WAITING = auto()
    HINTING = auto()
    GUESSING = auto()
    AFTER_PARTY = auto()


@dataclass
class Room:
    id: int
    state: RoomState = RoomState.FETUS

    def asdict(self):
        return asdict(self)
