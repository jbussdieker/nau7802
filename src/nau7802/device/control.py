from dataclasses import replace

from typed_registers import RegisterBus

from ..registers import REG_CTRL1, REG_CTRL2


def _set_pga(bus: RegisterBus, addr: int, pga: int) -> None:
    ctrl1 = REG_CTRL1.read(bus, addr)
    if ctrl1.pga != pga:
        replace(ctrl1, pga=pga).write(bus, addr)


def _set_vldo(bus: RegisterBus, addr: int, vldo: int) -> None:
    ctrl1 = REG_CTRL1.read(bus, addr)
    if ctrl1.vldo != vldo:
        replace(ctrl1, vldo=vldo).write(bus, addr)


def _set_crs(bus: RegisterBus, addr: int, crs: int) -> None:
    ctrl2 = REG_CTRL2.read(bus, addr)
    if ctrl2.crs != crs:
        replace(ctrl2, crs=crs).write(bus, addr)


def _set_chs(bus: RegisterBus, addr: int, chs: bool) -> None:
    ctrl2 = REG_CTRL2.read(bus, addr)
    if ctrl2.chs != chs:
        replace(ctrl2, chs=chs).write(bus, addr)


def _set_cals(bus: RegisterBus, addr: int, cals: bool) -> None:
    ctrl2 = REG_CTRL2.read(bus, addr)
    if ctrl2.cals != cals:
        replace(ctrl2, cals=cals).write(bus, addr)


def _set_calmod(bus: RegisterBus, addr: int, calmod: int) -> None:
    ctrl2 = REG_CTRL2.read(bus, addr)
    if ctrl2.calmod != calmod:
        replace(ctrl2, calmod=calmod).write(bus, addr)
