import argparse
import os

from typing import Any
import random
from typing import Union, Optional


def random_float(start: Union[float, int], stop: Union[float, int], seed: Optional[int] = None) -> float:
    """
    Generates a random floating-point number within the specified range.

    Args:
        start (Union[float, int]): The inclusive lower bound of the range.
        stop (Union[float, int]): The exclusive upper bound of the range.
        seed (Optional[int]): An optional seed value for the random number generator.

    Returns:
        float: A random floating-point number within the range [start, stop].

    Raises:
        ValueError: If start >= stop.
    """
    if seed is not None:
        random.seed(seed)
    if start >= stop:
        raise ValueError("start must be less than stop.")
    return random.uniform(start, stop)


class FaultTreeGeneratorArgParser(argparse.ArgumentParser):
    """
    Command-line argument parser for the Fault-Tree Generator.

    This parser is responsible for handling and validating the command-line arguments
    provided by the user for the generation of fault trees.

    Attributes:
        description (str): Description of the program using the parser.
        formatter_class (Any): Formatter class used for generating help documentation.

    Methods:
        add_arguments: Adds the command-line arguments to the parser.
    """

    def __init__(self, description: str = "Fault-Tree Generator",
                 formatter_class: Any = argparse.ArgumentDefaultsHelpFormatter, **kwargs: Any):
        """
        Initializes the FaultTreeGeneratorArgParser with a description and formatter class.

        Args:
            description (str): Description of the program using the parser.
            formatter_class (Any): Formatter class used for generating help documentation.
            **kwargs (Any): Additional keyword arguments passed to the argparse.ArgumentParser constructor.
        """
        super().__init__(description=description, formatter_class=formatter_class, **kwargs)
        self.add_arguments()

    def add_arguments(self) -> None:
        """
        Adds the command-line arguments to the parser.

        The arguments include options for setting the fault tree name, root gate name,
        random seed, number of basic events, average number of gate arguments, weights for gate types,
        commonality factors, probability ranges, number of house events, number of CCF groups,
        output file path, and an option to nest NOT connectives in Boolean formulae.
        """
        self.add_argument("--ft-name",
                          type=str,
                          help="Name for the fault tree.",
                          metavar="NCNAME",
                          default="Autogenerated")
        self.add_argument("--root",
                          type=str,
                          help="Name for the root gate.",
                          default="G1",
                          metavar="NCNAME")
        self.add_argument("--seed",
                          type=int,
                          default=random.randint(0, 2**32 - 1),
                          metavar="int",
                          help="Seed for the pseudo-random number generator (PRNG).")
        self.add_argument("-b", "--num-basic",
                          type=int,
                          help="Number of basic events.",
                          default=random.randint(2, 4),
                          metavar="int")
        self.add_argument("-a", "--num-args",
                          type=float,
                          default=3.0,
                          help="Average number of gate arguments.",
                          metavar="float")
        self.add_argument("--weights-g",
                          type=float,
                          nargs="+",
                          metavar="float",
                          help="Weights for [AND, OR, K/N, NOT, XOR] gates.",
                          default=[1,
                                   1,
                                   0,
                                   0,
                                   0,
                                   ]
                          )
        self.add_argument("--common-b",
                          type=float,
                          default=random_float(0.001, 0.005),
                          metavar="float",
                          help="Average percentage of common basic events per gate.")
        self.add_argument("--common-g",
                          type=float,
                          default=0.0,
                          metavar="float",
                          help="Average percentage of common gates per gate.")
        self.add_argument("--parents-b",
                          type=float,
                          default=2,
                          metavar="float",
                          help="Average number of parents for common basic events.")
        self.add_argument("--parents-g",
                          type=float,
                          default=2,
                          metavar="float",
                          help="Average number of parents for common gates.")
        self.add_argument("-g", "--num-gate",
                          type=int,
                          default=0,
                          metavar="int",
                          help="Number of gates (overrides parents-b/g and common-b/g).")
        self.add_argument("--max-prob",
                          type=float,
                          default=0.1,
                          metavar="float",
                          help="Maximum probability for basic events.")
        self.add_argument("--min-prob",
                          type=float,
                          default=0.01,
                          metavar="float",
                          help="Minimum probability for basic events.")
        self.add_argument("--num-house",
                          type=int,
                          help="Number of house events.",
                          default=0,
                          metavar="int")
        self.add_argument("--num-ccf",
                          type=int,
                          help="Number of CCF (Common Cause Failure) groups.",
                          default=0,
                          metavar="int")
        self.add_argument("-o", "--out",
                          type=str,
                          default="stdout",
                          metavar="path",
                          help="File path to write the fault tree.")
        self.add_argument("--nest",
                          action="store_true",
                          help="Nest NOT connectives in Boolean formulae.")
        self.add_argument("-n", "--max-trees",
                          type=int,
                          help="Maximum number of fault trees to generate.",
                          default=10,
                          metavar="int")
        self.add_argument("-t", "--timeout",
                          type=int,
                          help="Number of seconds to wait for a single fault tree to be generated before timing out",
                          default=1,
                          metavar="int")
        self.add_argument("-N", "--max-workers",
                          type=int,
                          help="Maximum number of worker processes to spin up for generating fault trees",
                          default=os.cpu_count() or 1,
                          metavar="int")