from ..registers import REG_PU_CTRL
from ..protocol import BusProtocol


def _reset(bus: BusProtocol, addr: int) -> None:
    pu = REG_PU_CTRL.read(bus, addr)
    pu.rr = True
    pu.write(bus, addr)


def _power_on(bus: BusProtocol, addr: int) -> None:
    pu = REG_PU_CTRL.read(bus, addr)
    pu.rr = False
    pu.pud = True
    pu.write(bus, addr)
    pu = REG_PU_CTRL.read(bus, addr)

    for _ in range(100):
        if REG_PU_CTRL.read(bus, addr).pur:
            return

    raise RuntimeError("Power-up failed")


def _set_defaults(bus: BusProtocol, addr: int) -> None:
    pu = REG_PU_CTRL.read(bus, addr)
    pu.avdds = True
    pu.cr = True
    pu.pua = True
    pu.write(bus, addr)


def _standby(bus: BusProtocol, addr: int) -> None:
    pu = REG_PU_CTRL.read(bus, addr)
    pu.pud = False
    pu.pua = False
    pu.write(bus, addr)


def _resume(bus: BusProtocol, addr: int) -> None:
    pu = REG_PU_CTRL.read(bus, addr)
    pu.pud = True
    pu.pua = True
    pu.write(bus, addr)
