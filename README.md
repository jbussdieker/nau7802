# NAU7802

A **typed, register-accurate Python driver** for the **NAU7802** 24-bit ADC load-cell amplifier.

This library provides a clean, Pythonic interface to the NAU7802 while preserving a **1:1 mapping to the hardware register model**. Every register is represented as a strongly-typed dataclass, enabling safe configuration, introspection, and debugging without hiding how the device actually works.

Designed primarily for Linux SBCs (Raspberry Pi, etc.) using I²C via `smbus2`.

## Features

* ✅ Typed register definitions (dataclasses)
* ✅ Full register-level control
* ✅ Automatic byte packing/unpacking
* ✅ Signed 24-bit and 32-bit register support
* ✅ Minimal abstraction — hardware behavior stays visible
* ✅ CLI utility for quick testing and debugging
* ✅ Python 3.11+

## Philosophy

Many ADC drivers hide device behavior behind opaque APIs.

**nau7802** intentionally does the opposite:

> The hardware register map *is* the API.

Each NAU7802 register is modeled explicitly:

* Bitfields become dataclass fields
* Reads return structured objects
* Writes serialize automatically
* Multi-byte registers behave naturally

This makes debugging with a datasheet straightforward — what you see in Python matches what exists on the chip.

Typed registers prevent invalid bit configurations and make register state inspectable during debugging.

## Installation

```bash
pip install nau7802[cli]
```

Or from source:

```bash
git clone https://github.com/jbussdieker/nau7802
cd nau7802
pip install -e .
```

## Requirements

* Python ≥ 3.11
* Linux I²C support enabled
* `smbus2`

Example (Raspberry Pi):

```bash
sudo raspi-config
# Enable I2C
```

## Quick Start

```python
import smbus2
from nau7802 import NAU7802

bus = smbus2.SMBus(1)
adc = NAU7802(bus, addr=0x2A)

adc.power_on()
adc.set_gain(7)
adc.set_channel(1)

print(adc.ctrl2)
# REG_CTRL2(chs=False, crs=3, ...)

value = adc.adco
print(value)
```

## Command Line Interface

A CLI tool is installed automatically:

```bash
nau7802 --help
```

### Power On

```bash
nau7802 power_on
```

### Initialize Device

```bash
nau7802 init --gain 7 --crs 3
```

### Read ADC Value

```bash
nau7802 read
```

### Dump All Registers

```bash
nau7802 dump
```

Example output:

```
NAU7802
  PU_CTRL      REG_PU_CTRL(...)
  CTRL1        REG_CTRL1(...)
  CTRL2        REG_CTRL2(...)
  ADCO         123456
  REV_ID       REG_REV_ID(...)
```

## Register Model

Registers are first-class objects.

Example:

```python
from nau7802.registers import REG_CTRL1

ctrl1 = REG_CTRL1.read(bus, 0x2A)

ctrl1.pga = 7
ctrl1.write(bus, 0x2A)
```

### Benefits

* No manual bit masking
* Self-documenting configuration
* Datasheet alignment
* Safe serialization

## Supported Register Types

### Byte Registers

Automatically mapped bitfields:

```python
REG_CTRL2(
    chs=False,
    crs=3,
)
```

### Multi-Byte Registers

Signed values handled automatically:

* 24-bit registers (ADCO, OCALx)
* 32-bit registers (GCALx)

Sign extension is applied transparently.

## Device API

### Power Control

```python
adc.power_on()
adc.standby()
adc.resume()
```

### Configuration

```python
adc.set_gain(7)
adc.set_crs(3)
adc.set_channel(1)
```

### Reading Data

```python
value = adc.adco
```

## Architecture Overview

```
nau7802/
├── device/
│   ├── power.py        # power sequencing
│   └── setting.py      # configuration helpers
│
├── register/
│   ├── _base.py        # generic register interface
│   └── _byte.py        # 8-bit register specialization
│
└── registers/
    └── REG_*           # typed register definitions
```

### Layering

1. **Register layer** — serialization + hardware truth
2. **Device layer** — safe operations & sequencing
3. **CLI layer** — human interaction

## Example: Debugging With Registers

```python
print(adc.ctrl2)
```

Instead of raw hex values, you see structured state:

```
REG_CTRL2(chs=False, crs=3, cal_err=False, ...)
```

## Development

Install dev dependencies:

```bash
pip install -e .[dev]
```

Type checking:

```bash
mypy src/
```

## Status

**Development Status:** Pre-Alpha

The API may change as hardware behavior and ergonomics are refined.

## Contributing

Issues and pull requests are welcome:

[https://github.com/jbussdieker/nau7802/issues](https://github.com/jbussdieker/nau7802/issues)

## License

MIT License

## Author

**Joshua B. Bussdieker**
[jbussdieker@gmail.com](mailto:jbussdieker@gmail.com)
