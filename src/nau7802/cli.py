import time
from dataclasses import dataclass

try:
    import click
except ImportError:
    raise RuntimeError("Install with: pip install nau7802[cli]")

import smbus2

from . import NAU7802


@dataclass
class CLIContext:
    device: NAU7802


pass_context = click.make_pass_decorator(CLIContext)


@click.group(context_settings={"help_option_names": ["-h", "--help"]})
@click.option("--bus", default=1, show_default=True, type=int)
@click.pass_context
def main(ctx: click.Context, bus: int) -> None:
    """NAU7802 CLI tool."""
    ctx.obj = CLIContext(
        device=NAU7802(smbus2.SMBus(bus)),
    )


@main.command()
@pass_context
@click.option("--gain", "-g", default=7, show_default=True)
@click.option("--crs", "-c", default=3, show_default=True)
def init(ctx: CLIContext, gain: int, crs: int) -> None:
    ctx.device.initialize()
    ctx.device.set_gain(gain)
    ctx.device.set_crs(crs)


@main.command()
@pass_context
def standby(ctx: CLIContext) -> None:
    ctx.device.standby()


@main.command()
@pass_context
def resume(ctx: CLIContext) -> None:
    ctx.device.resume()


@main.command()
@pass_context
@click.argument("channel", type=int)
def set_channel(ctx: CLIContext, channel: int) -> None:
    ctx.device.set_channel(channel)


@main.command()
@pass_context
@click.argument("ocal1", type=int)
def set_ocal1(ctx: CLIContext, ocal1: int) -> None:
    ctx.device.ocal1 = ocal1


@main.command()
@pass_context
@click.argument("ocal2", type=int)
def set_ocal2(ctx: CLIContext, ocal2: int) -> None:
    ctx.device.ocal2 = ocal2


@main.command()
@pass_context
@click.argument("calmod", type=int, default=0)
def calibrate(ctx: CLIContext, calmod: int) -> None:
    ctx.device.set_calmod(calmod)
    ctx.device.set_cals(True)

    timeout = time.time() + 1

    while ctx.device.cals:
        print("calibrating")
        time.sleep(0.05)
        if time.time() > timeout:
            print("timed out")

    if ctx.device.cal_err:
        print("error")
    else:
        print("success")


@main.command()
@pass_context
def read(ctx: CLIContext) -> None:
    print(ctx.device.adco.value)


@main.command()
@pass_context
def dump(ctx: CLIContext) -> None:
    print("NAU7802")
    print("  PU_CTRL     ", ctx.device.pu_ctrl)
    print("  CTRL1       ", ctx.device.ctrl1)
    print("  CTRL2       ", ctx.device.ctrl2)
    print("  OCAL1       ", ctx.device.ocal1.value)
    print("  GCAL1       ", hex(ctx.device.gcal1.value))
    print("  OCAL2       ", ctx.device.ocal2.value)
    print("  GCAL2       ", hex(ctx.device.gcal2.value))
    print("  I2C_CONTROL ", ctx.device.i2c_control)
    print("  ADCO        ", ctx.device.adco.value)
    print("  ADC_CTRL1   ", ctx.device.adc_ctrl1)
    print("  ADC_CTRL3   ", ctx.device.adc_ctrl3)
    print("  PWR_CTRL    ", ctx.device.pwr_ctrl)
    print("  REV_ID      ", ctx.device.rev_id)
