from typing import Self
from dataclasses import dataclass

from ..register._base import Register


@dataclass
class REG_OCAL1(Register):
    ADDRESS = 0x03
    WIDTH = 3

    value: int = 0  # signed 24-bit

    def to_bytes(self) -> bytes:
        v = self.value & 0xFFFFFF
        return bytes(
            [
                (v >> 16) & 0xFF,
                (v >> 8) & 0xFF,
                v & 0xFF,
            ]
        )

    @classmethod
    def from_bytes(cls, data: bytes) -> Self:
        val = (data[0] << 16) | (data[1] << 8) | data[2]

        # sign extend
        if val & 0x800000:
            val -= 1 << 24

        return cls(value=val)
