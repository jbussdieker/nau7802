from ..registers import REG_ADC_CTRL1
from ..protocol import BusProtocol


def _set_defaults(bus: BusProtocol, addr: int) -> None:
    adc = REG_ADC_CTRL1.read(bus, addr)
    adc.reg_chps = 3
    adc.write(bus, addr)
