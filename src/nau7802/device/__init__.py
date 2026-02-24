from typing import Any

from .. import registers
from . import power, setting


class NAU7802:
    def __init__(self, bus: Any, addr: int = 0x2A) -> None:
        self.bus = bus
        self.addr: int = addr
        self.channel: int | None = None

    def power_on(self) -> None:
        power._power_on(self.bus, self.addr)

    def standby(self) -> None:
        power._standby(self.bus, self.addr)

    def resume(self) -> None:
        power._resume(self.bus, self.addr)

    def set_gain(self, gain: int) -> None:
        setting._set_gain(self.bus, self.addr, gain)

    def set_crs(self, crs: int) -> None:
        setting._set_crs(self.bus, self.addr, crs)

    def set_channel(self, channel: int) -> None:
        if self.channel != channel:
            setting._set_channel(self.bus, self.addr, channel)
            self.channel = channel

    @property
    def adco(self) -> int:
        return registers.REG_ADCO.read(self.bus, self.addr).value

    @property
    def gcal1(self) -> int:
        return registers.REG_GCAL1.read(self.bus, self.addr).value

    @property
    def ocal1(self) -> int:
        return registers.REG_OCAL1.read(self.bus, self.addr).value

    @property
    def gcal2(self) -> int:
        return registers.REG_GCAL2.read(self.bus, self.addr).value

    @property
    def ocal2(self) -> int:
        return registers.REG_OCAL2.read(self.bus, self.addr).value

    @property
    def pu_ctrl(self) -> registers.REG_PU_CTRL:
        return registers.REG_PU_CTRL.read(self.bus, self.addr)

    @property
    def ctrl1(self) -> registers.REG_CTRL1:
        return registers.REG_CTRL1.read(self.bus, self.addr)

    @property
    def ctrl2(self) -> registers.REG_CTRL2:
        return registers.REG_CTRL2.read(self.bus, self.addr)

    @property
    def i2c_control(self) -> registers.REG_I2C_CONTROL:
        return registers.REG_I2C_CONTROL.read(self.bus, self.addr)

    @property
    def adc_ctrl1(self) -> registers.REG_ADC_CTRL1:
        return registers.REG_ADC_CTRL1.read(self.bus, self.addr)

    @property
    def adc_ctrl3(self) -> registers.REG_ADC_CTRL3:
        return registers.REG_ADC_CTRL3.read(self.bus, self.addr)

    @property
    def pwr_ctrl(self) -> registers.REG_PWR_CTRL:
        return registers.REG_PWR_CTRL.read(self.bus, self.addr)

    @property
    def rev_id(self) -> registers.REG_REV_ID:
        return registers.REG_REV_ID.read(self.bus, self.addr)
