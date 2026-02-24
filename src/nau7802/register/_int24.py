from typing import Type, Self
from abc import abstractmethod

from ._base import Register, R


from dataclasses import dataclass


@dataclass
class Int24Register(Register):
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
