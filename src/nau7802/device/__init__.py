from ..protocol import BusProtocol
from .. import registers

from . import power, control, adc


class NAU7802:
    def __init__(self, bus: BusProtocol, addr: int = 0x2A) -> None:
        self.bus = bus
        self.addr: int = addr
        self.channel: int | None = None

    def initialize(self) -> None:
        power._reset(self.bus, self.addr)
        power._power_on(self.bus, self.addr)
        power._set_defaults(self.bus, self.addr)
        adc._set_defaults(self.bus, self.addr)

    def standby(self) -> None:
        power._standby(self.bus, self.addr)

    def resume(self) -> None:
        power._resume(self.bus, self.addr)

    def set_gain(self, gain: int) -> None:
        control._set_gain(self.bus, self.addr, gain)

    def set_crs(self, crs: int) -> None:
        control._set_crs(self.bus, self.addr, crs)

    def set_channel(self, channel: int) -> None:
        control._set_channel(self.bus, self.addr, channel)
        self.channel = channel

    @property
    def cycle_ready(self) -> bool:
        return registers.REG_PU_CTRL.read(self.bus, self.addr).cr

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
