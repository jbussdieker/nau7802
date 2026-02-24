from typing import Any

from ..registers import REG_PU_CTRL, REG_ADC_CTRL1


def _power_on(bus: Any, addr: int) -> None:
    pu = REG_PU_CTRL.read(bus, addr)
    pu.rr = True
    pu.write(bus, addr)
    pu = REG_PU_CTRL.read(bus, addr)
    pu.rr = False
    pu.pud = True
    pu.write(bus, addr)
    pu = REG_PU_CTRL.read(bus, addr)
    if not pu.pur:
        raise RuntimeError("Power-up failed")
    pu.avdds = True
    pu.cr = True
    pu.pua = True
    pu.write(bus, addr)
    adc = REG_ADC_CTRL1.read(bus, addr)
    adc.reg_chps = 3
    adc.write(bus, addr)


def _standby(bus: Any, addr: int) -> None:
    pu = REG_PU_CTRL.read(bus, addr)
    pu.pud = False
    pu.pua = False
    pu.write(bus, addr)


def _resume(bus: Any, addr: int) -> None:
    pu = REG_PU_CTRL.read(bus, addr)
    pu.pud = True
    pu.pua = True
    pu.write(bus, addr)
