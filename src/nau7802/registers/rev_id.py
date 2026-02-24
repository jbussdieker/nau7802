from typing import Self
from dataclasses import dataclass

from ..register._byte import ByteRegister


@dataclass
class REG_REV_ID(ByteRegister):
    ADDRESS = 0x1F

    rev_id: int = 0
    res: int = 0

    def to_byte(self) -> int:
        value = 0
        value |= (self.res & 0b1111) << 4
        value |= self.rev_id & 0b1111
        return value

    @classmethod
    def from_byte(cls, byte: int) -> Self:
        res = (byte >> 4) & 0b1111
        rev_id = byte & 0b1111

        return cls(
            res=res,
            rev_id=rev_id,
        )
