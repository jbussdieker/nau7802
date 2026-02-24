from typing import Self
from dataclasses import dataclass

from ..register._byte import ByteRegister


@dataclass
class REG_PU_CTRL(ByteRegister):
    ADDRESS = 0x00

    avdds: bool = False
    oscs: bool = False
    cr: bool = False
    cs: bool = False
    pur: bool = False
    pua: bool = False
    pud: bool = False
    rr: bool = False

    def to_byte(self) -> int:
        value = 0
        value |= self.avdds << 7
        value |= self.oscs << 6
        value |= self.cr << 5
        value |= self.cs << 4
        value |= self.pur << 3
        value |= self.pua << 2
        value |= self.pud << 1
        value |= self.rr << 0
        return value

    @classmethod
    def from_byte(cls, byte: int) -> Self:
        return cls(
            avdds=bool(byte & (1 << 7)),
            oscs=bool(byte & (1 << 6)),
            cr=bool(byte & (1 << 5)),
            cs=bool(byte & (1 << 4)),
            pur=bool(byte & (1 << 3)),
            pua=bool(byte & (1 << 2)),
            pud=bool(byte & (1 << 1)),
            rr=bool(byte & (1 << 0)),
        )
