from typing import Self
from dataclasses import dataclass

from ..register._byte import ByteRegister


@dataclass
class REG_CTRL2(ByteRegister):
    ADDRESS = 0x02

    chs: bool = False
    crs: int = 0
    cal_err: bool = False
    cals: bool = False
    calmod: int = 0

    def to_byte(self) -> int:
        value = 0
        value |= self.chs << 7
        value |= (self.crs & 0b111) << 4
        value |= self.cal_err << 3
        value |= self.cals << 2
        value |= self.calmod & 0b11
        return value

    @classmethod
    def from_byte(cls, byte: int) -> Self:
        crs = (byte >> 4) & 0b111
        calmod = byte & 0b11

        return cls(
            chs=bool(byte & (1 << 7)),
            crs=crs,
            cal_err=bool(byte & (1 << 3)),
            cals=bool(byte & (1 << 2)),
            calmod=calmod,
        )
