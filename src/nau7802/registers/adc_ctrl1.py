from typing import Self
from dataclasses import dataclass

from ..register._byte import ByteRegister


@dataclass
class REG_ADC_CTRL1(ByteRegister):
    ADDRESS = 0x15

    res: int = 0
    reg_chps: int = 0
    adc_vcm: int = 0
    dly_chp: int = 0

    def __post_init__(self) -> None:
        if not 0 <= self.res <= 3:
            raise ValueError("res out of range")
        if not 0 <= self.reg_chps <= 3:
            raise ValueError("reg_chps out of range")
        if not 0 <= self.adc_vcm <= 3:
            raise ValueError("adc_vcm out of range")
        if not 0 <= self.dly_chp <= 3:
            raise ValueError("dly_chp out of range")

    def to_byte(self) -> int:
        value = 0
        value |= (self.res & 0b11) << 6
        value |= (self.reg_chps & 0b11) << 4
        value |= (self.adc_vcm & 0b11) << 2
        value |= self.dly_chp & 0b11
        return value

    @classmethod
    def from_byte(cls, byte: int) -> Self:
        res = (byte >> 6) & 0b11
        reg_chps = (byte >> 4) & 0b11
        adc_vcm = (byte >> 2) & 0b11
        dly_chp = byte & 0b11

        return cls(
            res=res,
            reg_chps=reg_chps,
            adc_vcm=adc_vcm,
            dly_chp=dly_chp,
        )
