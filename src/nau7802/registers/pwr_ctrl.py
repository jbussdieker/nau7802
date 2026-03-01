from typing import Self
from dataclasses import dataclass

from ..register._byte import ByteRegister


@dataclass
class REG_PWR_CTRL(ByteRegister):
    ADDRESS = 0x1C

    pga_cap_en: bool = False
    master_bias_curr: int = 0
    adc_curr: int = 0
    pga_curr: int = 0

    def __post_init__(self) -> None:
        if not 0 <= self.master_bias_curr <= 7:
            raise ValueError("master_bias_curr out of range")
        if not 0 <= self.adc_curr <= 3:
            raise ValueError("adc_curr out of range")
        if not 0 <= self.pga_curr <= 3:
            raise ValueError("pga_curr out of range")

    def to_byte(self) -> int:
        value = 0
        value |= int(self.pga_cap_en) << 7
        value |= (self.master_bias_curr & 0b111) << 4
        value |= (self.adc_curr & 0b11) << 2
        value |= self.pga_curr & 0b11
        return value

    @classmethod
    def from_byte(cls, byte: int) -> Self:
        pga_curr = byte & 0b111
        adc_curr = (byte >> 2) & 0b11
        master_bias_curr = (byte >> 4) & 0b111

        return cls(
            pga_cap_en=bool(byte & (1 << 7)),
            master_bias_curr=master_bias_curr,
            adc_curr=adc_curr,
            pga_curr=pga_curr,
        )
