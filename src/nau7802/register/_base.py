from typing import TypeVar, Type
from abc import ABC, abstractmethod

from ..protocol import BusProtocol

R = TypeVar("R", bound="Register")


class Register(ABC):
    ADDRESS: int
    WIDTH: int = 1

    @abstractmethod
    def to_bytes(self) -> bytes: ...

    @classmethod
    @abstractmethod
    def from_bytes(cls: Type[R], data: bytes) -> R: ...

    @classmethod
    def from_byte(cls: Type[R], value: int) -> R:
        if cls.WIDTH != 1:
            raise TypeError(f"{cls.__name__} is not 8-bit")
        return cls.from_bytes(bytes([value]))

    @classmethod
    def read(cls: Type[R], bus: BusProtocol, addr: int) -> R:
        if cls.WIDTH == 1:
            raw = bus.read_byte_data(addr, cls.ADDRESS)
            return cls.from_bytes(bytes([raw]))
        else:
            data = bus.read_i2c_block_data(addr, cls.ADDRESS, cls.WIDTH)
            return cls.from_bytes(bytes(data))

    def to_byte(self) -> int:
        if self.WIDTH != 1:
            raise TypeError(f"{type(self).__name__} is not 8-bit")
        return self.to_bytes()[0]

    def write(self, bus: BusProtocol, addr: int) -> None:
        data = self.to_bytes()

        if self.WIDTH == 1:
            bus.write_byte_data(addr, self.ADDRESS, data[0])
        else:
            bus.write_i2c_block_data(addr, self.ADDRESS, list(data))
