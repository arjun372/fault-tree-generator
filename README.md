# Fault Tree Generator

Fault Tree Generator is a utility for creating and exporting synthetic fault trees. It is designed to assist engineers and researchers in the field of reliability engineering and safety analysis.

## Table of Contents

- [Installation](#installation)
- [Command Line Arguments](#command-line-arguments)
- [Usage](#usage)
- [Features](#features)
- [Contributing](#contributing)
- [Code of Conduct](#code-of-conduct)
- [License](#license)
- [Acknowledgments](#acknowledgments)

## Installation

To install Fault Tree Generator, you can use pip:

```bash
pip install fault-tree-generator
```

Alternatively, you can clone the repository and install it manually:

```bash
git clone https://github.com/arjun372/fault-tree-generator.git
cd fault-tree-generator
python setup.py install
```

## Usage

The Fault Tree Generator can be customized using various command-line arguments. Below is the usage information:

```console
usage: fault-tree-generator [--ft-name NCNAME] [--root NCNAME] [--seed int] [-b int] [-a float] [--weights-g float [float ...]]
                            [--common-b float] [--common-g float] [--parents-b float] [--parents-g float] [-g int] [--max-prob float]
                            [--min-prob float] [--num-house int] [--num-ccf int] [-o path] [--aralia] [--nest]

Utility for creating synthetic fault trees.

options:
  -h, --help                Show this help message and exit
  --ft-name NCNAME          Name for the fault tree (default: "Autogenerated")
  --root NCNAME             Name for the root gate (default: "root")
  --seed int                Seed for the PRNG (default: 123)
  -b, --num-basic int       Number of basic events (default: 100)
  -a, --num-args float      Average number of gate arguments (default: 3.0)
  --weights-g float [...]   Weights for [AND, OR, K/N, NOT, XOR] gates (default: [1, 1, 0, 0, 0])
  --common-b float          Average percentage of common basic events per gate (default: 0.1)
  --common-g float          Average percentage of common gates per gate (default: 0.1)
  --parents-b float         Average number of parents for common basic events (default: 2)
  --parents-g float         Average number of parents for common gates (default: 2)
  -g, --num-gate int        Number of gates (overrides parents-b/g and common-b/g if set) (default: 0)
  --max-prob float          Maximum probability for basic events (default: 0.1)
  --min-prob float          Minimum probability for basic events (default: 0.01)
  --num-house int           Number of house events (default: 0)
  --num-ccf int             Number of CCF groups (default: 0)
  -o, --out path            File to write the fault tree (default: standard output)
  --aralia                  Apply the Aralia format to the output (default: False)
  --nest                    Nest NOT connectives in Boolean formulae (default: False)
```

To generate a fault tree with default settings, simply run:

```bash
fault-tree-generator
```

For a more customized fault tree, you can use the command-line arguments to specify various options. Here are a few examples:

To specify a name for the fault tree and the root gate, and to write the output to a file:

```bash
fault-tree-generator --ft-name "ExampleTree" --root "MainGate" --out "example_tree.xml"
```

To set a custom seed for the pseudo-random number generator and adjust the number of basic events:

```bash
fault-tree-generator --seed 456 --num-basic 150
```

To use custom weights for the gate types and specify the maximum and minimum probabilities for basic events:

```bash
fault-tree-generator --weights-g 2 1 0.5 0 0 --max-prob 0.05 --min-prob 0.001
```

## Features

- Generation of synthetic fault trees based on user-defined parameters.
- Exporting fault trees to various formats for further analysis.
- A user-friendly command-line interface.

## Contributing

We welcome contributions to the Fault Tree Generator project! Please read our [CONTRIBUTING.md](CONTRIBUTING.md) file for guidelines on how to make contributions.

## Code of Conduct

Our project adheres to a Code of Conduct that we expect all contributors to follow. Please read the [CODE_OF_CONDUCT.md](CODE_OF_CONDUCT.md) file for details.

## License

Fault Tree Generator is released under the MIT License. See the [LICENSE](LICENSE) file for more information.

## Acknowledgments

Acknowledge any individuals or organizations that have contributed to the project.

- John Doe for initial concept and design.
- XYZ Research Lab for testing and feedback.