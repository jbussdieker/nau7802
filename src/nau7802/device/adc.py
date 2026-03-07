from dataclasses import replace

from typed_registers import RegisterBus

from ..registers import REG_ADC_CTRL1


def _set_defaults(bus: RegisterBus, addr: int) -> None:
    adc = REG_ADC_CTRL1.read(bus, addr)
    if adc.reg_chps != 3:
        replace(adc, reg_chps=3).write(bus, addr)
