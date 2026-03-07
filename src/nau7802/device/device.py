from typing import Literal

from typed_registers import RegisterBus

from .. import registers
from . import power, control, adc


class NAU7802:
    def __init__(self, bus: RegisterBus, addr: int = 0x2A) -> None:
        self.bus = bus
        self.addr: int = addr

    def initialize(self) -> None:
        power._reset(self.bus, self.addr)
        power._power_on(self.bus, self.addr)
        power._set_defaults(self.bus, self.addr)
        adc._set_defaults(self.bus, self.addr)

    def standby(self) -> None:
        power._standby(self.bus, self.addr)

    def resume(self) -> None:
        power._resume(self.bus, self.addr)

    def set_vldo(self, vldo: int) -> None:
        control._set_vldo(self.bus, self.addr, vldo)

    def set_gain(self, gain: int) -> None:
        control._set_pga(self.bus, self.addr, gain)

    def set_crs(self, crs: int) -> None:
        control._set_crs(self.bus, self.addr, crs)

    def set_channel(self, channel: Literal[1, 2]) -> None:
        if channel == 1:
            chs = False
        elif channel == 2:
            chs = True
        else:
            raise RuntimeError(f"Invalid channel {channel}")

        control._set_chs(self.bus, self.addr, chs)

    def set_cals(self, cals: bool) -> None:
        control._set_cals(self.bus, self.addr, cals)

    def set_calmod(self, calmod: int) -> None:
        control._set_calmod(self.bus, self.addr, calmod)

    @property
    def channel(self) -> int:
        return 2 if self.ctrl2.chs else 1

    @property
    def cycle_ready(self) -> bool:
        return self.pu_ctrl.cr

    @property
    def cals(self) -> bool:
        return self.ctrl2.cals

    @property
    def cal_err(self) -> bool:
        return self.ctrl2.cal_err

    @property
    def adc_ctrl1(self) -> registers.REG_ADC_CTRL1:
        return registers.REG_ADC_CTRL1.read(self.bus, self.addr)

    @property
    def adc_ctrl3(self) -> registers.REG_ADC_CTRL3:
        return registers.REG_ADC_CTRL3.read(self.bus, self.addr)

    @property
    def adco(self) -> registers.REG_ADCO:
        return registers.REG_ADCO.read(self.bus, self.addr)

    @property
    def ctrl1(self) -> registers.REG_CTRL1:
        return registers.REG_CTRL1.read(self.bus, self.addr)

    @property
    def ctrl2(self) -> registers.REG_CTRL2:
        return registers.REG_CTRL2.read(self.bus, self.addr)

    @property
    def gcal1(self) -> registers.REG_GCAL1:
        return registers.REG_GCAL1.read(self.bus, self.addr)

    @gcal1.setter
    def gcal1(self, value: int) -> None:
        registers.REG_GCAL1(value=value).write(self.bus, self.addr)

    @property
    def gcal2(self) -> registers.REG_GCAL2:
        return registers.REG_GCAL2.read(self.bus, self.addr)

    @gcal2.setter
    def gcal2(self, value: int) -> None:
        registers.REG_GCAL2(value=value).write(self.bus, self.addr)

    @property
    def i2c_control(self) -> registers.REG_I2C_CONTROL:
        return registers.REG_I2C_CONTROL.read(self.bus, self.addr)

    @property
    def ocal1(self) -> registers.REG_OCAL1:
        return registers.REG_OCAL1.read(self.bus, self.addr)

    @ocal1.setter
    def ocal1(self, value: int) -> None:
        registers.REG_OCAL1(value=value).write(self.bus, self.addr)

    @property
    def ocal2(self) -> registers.REG_OCAL2:
        return registers.REG_OCAL2.read(self.bus, self.addr)

    @ocal2.setter
    def ocal2(self, value: int) -> None:
        registers.REG_OCAL2(value=value).write(self.bus, self.addr)

    @property
    def pu_ctrl(self) -> registers.REG_PU_CTRL:
        return registers.REG_PU_CTRL.read(self.bus, self.addr)

    @property
    def pwr_ctrl(self) -> registers.REG_PWR_CTRL:
        return registers.REG_PWR_CTRL.read(self.bus, self.addr)

    @property
    def rev_id(self) -> registers.REG_REV_ID:
        return registers.REG_REV_ID.read(self.bus, self.addr)
