from typing import Self
from dataclasses import dataclass

from ..register._byte import ByteRegister


@dataclass
class REG_ADC_CTRL3(ByteRegister):
    ADDRESS = 0x1B

    rd_otp_sel: bool = False
    ldomode: bool = False
    pga_buff: bool = False
    pga_bp: bool = False
    pgainv: bool = False
    res2: bool = False
    res1: bool = False
    pgachpdis: bool = False

    def to_byte(self) -> int:
        value = 0
        value |= self.rd_otp_sel << 7
        value |= self.ldomode << 6
        value |= self.pga_buff << 5
        value |= self.pga_bp << 4
        value |= self.pgainv << 3
        value |= self.res2 << 2
        value |= self.res1 << 1
        value |= self.pgachpdis << 0
        return value

    @classmethod
    def from_byte(cls, byte: int) -> Self:
        return cls(
            rd_otp_sel=bool(byte & (1 << 7)),
            ldomode=bool(byte & (1 << 6)),
            pga_buff=bool(byte & (1 << 5)),
            pga_bp=bool(byte & (1 << 4)),
            pgainv=bool(byte & (1 << 3)),
            res2=bool(byte & (1 << 2)),
            res1=bool(byte & (1 << 1)),
            pgachpdis=bool(byte & (1 << 0)),
        )
