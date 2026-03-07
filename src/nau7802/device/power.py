from dataclasses import replace

from typed_registers import RegisterBus

from ..registers import REG_PU_CTRL


def _reset(bus: RegisterBus, addr: int) -> None:
    pu = REG_PU_CTRL.read(bus, addr)
    replace(pu, rr=True).write(bus, addr)


def _power_on(bus: RegisterBus, addr: int) -> None:
    pu = REG_PU_CTRL.read(bus, addr)
    replace(pu, rr=False, pud=True).write(bus, addr)
    pu = REG_PU_CTRL.read(bus, addr)

    for _ in range(100):
        if REG_PU_CTRL.read(bus, addr).pur:
            return

    raise RuntimeError("Power-up failed")


def _set_defaults(bus: RegisterBus, addr: int) -> None:
    pu = REG_PU_CTRL.read(bus, addr)
    replace(pu, avdds=True, cr=True, pua=True).write(bus, addr)


def _standby(bus: RegisterBus, addr: int) -> None:
    pu = REG_PU_CTRL.read(bus, addr)
    replace(pu, pud=False, pua=False).write(bus, addr)


def _resume(bus: RegisterBus, addr: int) -> None:
    pu = REG_PU_CTRL.read(bus, addr)
    replace(pu, pud=True, pua=True).write(bus, addr)
