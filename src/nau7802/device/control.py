from ..registers import REG_CTRL1, REG_CTRL2
from ..protocol import BusProtocol


def _set_gain(bus: BusProtocol, addr: int, gain: int) -> None:
    ctrl1 = REG_CTRL1.read(bus, addr)
    ctrl1.pga = gain
    ctrl1.write(bus, addr)


def _set_crs(bus: BusProtocol, addr: int, crs: int) -> None:
    ctrl2 = REG_CTRL2.read(bus, addr)
    ctrl2.crs = crs
    ctrl2.write(bus, addr)


def _set_channel(bus: BusProtocol, addr: int, channel: int) -> None:
    if channel == 1:
        expected = False
    elif channel == 2:
        expected = True
    else:
        raise RuntimeError(f"Invalid channel {channel}")

    ctrl2 = REG_CTRL2.read(bus, addr)
    if ctrl2.chs != expected:
        ctrl2.chs = expected
        ctrl2.write(bus, addr)
