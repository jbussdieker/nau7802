from typing import Self
from dataclasses import dataclass

from ..register._byte import ByteRegister


@dataclass
class REG_CTRL1(ByteRegister):
    ADDRESS = 0x01

    drdyp: bool = False
    drdy_sel: bool = False
    vldo: int = 0  # 0..7
    pga: int = 1  # 0..7

    def __post_init__(self) -> None:
        if not 0 <= self.vldo <= 7:
            raise ValueError("vldo out of range")
        if not 0 <= self.pga <= 7:
            raise ValueError("pga out of range")

    def to_byte(self) -> int:
        value = 0
        value |= self.drdyp << 7
        value |= self.drdy_sel << 6
        value |= (self.vldo & 0b111) << 3
        value |= self.pga & 0b111
        return value

    @classmethod
    def from_byte(cls, byte: int) -> Self:
        pga = byte & 0b111
        vldo = (byte >> 3) & 0b111

        return cls(
            pga=pga,
            vldo=vldo,
            drdy_sel=bool(byte & (1 << 6)),
            drdyp=bool(byte & (1 << 7)),
        )
