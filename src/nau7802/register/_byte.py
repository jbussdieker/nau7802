from typing import Type
from abc import abstractmethod
from dataclasses import dataclass

from ._base import Register, R


@dataclass
class ByteRegister(Register):
    WIDTH = 1

    @abstractmethod
    def to_byte(self) -> int: ...

    @classmethod
    @abstractmethod
    def from_byte(cls: Type[R], data: int) -> R: ...

    def to_bytes(self) -> bytes:
        return bytes([self.to_byte()])

    @classmethod
    def from_bytes(cls: Type[R], data: bytes) -> R:
        cls._assert_data_width(data)
        return cls.from_byte(data[0])
