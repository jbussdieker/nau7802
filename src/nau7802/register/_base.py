from typing import TypeVar, Type, Any
from abc import ABC, abstractmethod

R = TypeVar("R", bound="Register")


class Register(ABC):
    ADDRESS: int
    WIDTH: int = 1

    @abstractmethod
    def to_bytes(self) -> bytes: ...

    @classmethod
    @abstractmethod
    def from_bytes(cls: Type[R], data: bytes) -> R: ...

    def to_byte(self) -> int:
        data = self.to_bytes()
        if len(data) != 1:
            raise TypeError(f"{type(self).__name__} is not 8-bit")
        return data[0]

    @classmethod
    def from_byte(cls: Type[R], value: int) -> R:
        if cls.WIDTH != 1:
            raise TypeError(f"{cls.__name__} is not 8-bit")
        return cls.from_bytes(bytes([value]))

    @classmethod
    def read(cls: Type[R], bus: Any, addr: int) -> R:
        if cls.WIDTH == 1:
            raw = bus.read_byte_data(addr, cls.ADDRESS)
            return cls.from_bytes(bytes([raw]))

        data = bus.read_i2c_block_data(addr, cls.ADDRESS, cls.WIDTH)
        return cls.from_bytes(bytes(data))

    def write(self, bus: Any, addr: int) -> None:
        data = self.to_bytes()

        if self.WIDTH == 1:
            bus.write_byte_data(addr, self.ADDRESS, data[0])
        else:
            bus.write_i2c_block_data(addr, self.ADDRESS, list(data))
