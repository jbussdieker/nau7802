from typing import Self
from dataclasses import dataclass

from ..register._byte import ByteRegister


@dataclass
class REG_I2C_CONTROL(ByteRegister):
    ADDRESS = 0x11

    crsd: bool = False
    frd: bool = False
    spe: bool = False
    wpd: bool = False
    si: bool = False
    bopga: bool = False
    ts: bool = False
    bgpcp: bool = False

    def to_byte(self) -> int:
        value = 0
        value |= int(self.crsd) << 7
        value |= int(self.frd) << 6
        value |= int(self.spe) << 5
        value |= int(self.wpd) << 4
        value |= int(self.si) << 3
        value |= int(self.bopga) << 2
        value |= int(self.ts) << 1
        value |= int(self.bgpcp) << 0
        return value

    @classmethod
    def from_byte(cls, byte: int) -> Self:
        return cls(
            crsd=bool(byte & (1 << 7)),
            frd=bool(byte & (1 << 6)),
            spe=bool(byte & (1 << 5)),
            wpd=bool(byte & (1 << 4)),
            si=bool(byte & (1 << 3)),
            bopga=bool(byte & (1 << 2)),
            ts=bool(byte & (1 << 1)),
            bgpcp=bool(byte & (1 << 0)),
        )
