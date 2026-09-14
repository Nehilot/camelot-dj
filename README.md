# Camelot DJ

Open-source Harmonic Mixing Assistant.

## Project Goals

- Represent the 24 Camelot Wheel positions.
- Convert between musical key notation and Camelot notation.
- Determine harmonically compatible keys.
- Explain why two keys are compatible.
- Support musical key transposition.
- Provide a lightweight standalone application.
- Prepare a clean architecture for future Mixxx integration.
- Keep the musical engine independent from the graphical interface and Mixxx.

## Architecture

The project is divided into three main areas:

### camelot-core

The musical engine.

It is responsible for:

- Musical keys.
- Camelot notation.
- Open Key notation.
- Key conversions.
- Harmonic compatibility.
- Transposition.
- Enharmonic equivalence.
- Validation and musical rules.

The core must remain independent from the GUI and Mixxx integration.

### camelot-dj

The standalone graphical application.

The planned interface will provide:

- Interactive Camelot Wheel.
- Musical and Camelot key display.
- Compatible key suggestions.
- Visual compatibility indicators.
- Notation conversion.
- Transposition information.
- Dark mode.
- Offline operation.

### camelot-mixxx

The future Mixxx integration layer.

The initial integration approach will avoid modifying Mixxx source code and will use available interfaces or scripts where possible.

## First Target — v0.1

The first concrete development target is the Camelot Core.

For example:

```text
Input: 8A

Musical key: A♭ minor
Camelot: 8A

Compatible keys:
- 7A
- 8A
- 9A
- 8B
```

The reverse conversion must also be supported.

Automated tests will cover all 24 Camelot positions and the corresponding nomenclature conversions.

## Development Principle

> First musical precision, then interface, finally integration.

The project should establish a reliable musical foundation before building the graphical interface or Mixxx integration.

## Status

Planning / Initial development.

The architecture and first development target are defined. The Camelot Core implementation is the next major milestone.


## Platform

Initial development target:

- Linux
- Debian-based distributions
- antiX 26

Future target:

- Windows

## License

Camelot DJ is intended to be released under the GNU General Public License v3.0 or later.

See [LICENSE](LICENSE) for details.
