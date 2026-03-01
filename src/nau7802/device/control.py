from ..registers import REG_CTRL1, REG_CTRL2
from ..protocol import BusProtocol


def _set_pga(bus: BusProtocol, addr: int, pga: int) -> None:
    ctrl1 = REG_CTRL1.read(bus, addr)
    if ctrl1.pga != pga:
        ctrl1.pga = pga
        ctrl1.write(bus, addr)


def _set_vldo(bus: BusProtocol, addr: int, vldo: int) -> None:
    ctrl1 = REG_CTRL1.read(bus, addr)
    if ctrl1.vldo != vldo:
        ctrl1.vldo = vldo
        ctrl1.write(bus, addr)


def _set_crs(bus: BusProtocol, addr: int, crs: int) -> None:
    ctrl2 = REG_CTRL2.read(bus, addr)
    if ctrl2.crs != crs:
        ctrl2.crs = crs
        ctrl2.write(bus, addr)


def _set_chs(bus: BusProtocol, addr: int, channel: bool) -> None:
    ctrl2 = REG_CTRL2.read(bus, addr)
    if ctrl2.chs != channel:
        ctrl2.chs = channel
        ctrl2.write(bus, addr)


def _set_cals(bus: BusProtocol, addr: int, cals: bool) -> None:
    ctrl2 = REG_CTRL2.read(bus, addr)
    if ctrl2.cals != cals:
        ctrl2.cals = cals
        ctrl2.write(bus, addr)


def _set_calmod(bus: BusProtocol, addr: int, calmod: int) -> None:
    ctrl2 = REG_CTRL2.read(bus, addr)
    if ctrl2.calmod != calmod:
        ctrl2.calmod = calmod
        ctrl2.write(bus, addr)
