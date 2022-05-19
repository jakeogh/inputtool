#!/usr/bin/env python3
# -*- coding: utf8 -*-

# pylint: disable=C0111  # docstrings are always outdated and wrong
# pylint: disable=C0114  # Missing module docstring (missing-module-docstring)
# pylint: disable=W0511  # todo is encouraged
# pylint: disable=C0301  # line too long
# pylint: disable=R0902  # too many instance attributes
# pylint: disable=C0302  # too many lines in module
# pylint: disable=C0103  # single letter var names, func name too descriptive
# pylint: disable=R0911  # too many return statements
# pylint: disable=R0912  # too many branches
# pylint: disable=R0915  # too many statements
# pylint: disable=R0913  # too many arguments
# pylint: disable=R1702  # too many nested blocks
# pylint: disable=R0914  # too many local variables
# pylint: disable=R0903  # too few public methods
# pylint: disable=E1101  # no member for base
# pylint: disable=W0201  # attribute defined outside __init__
# pylint: disable=R0916  # Too many boolean expressions in if statement
# pylint: disable=C0305  # Trailing newlines editor should fix automatically, pointless warning


from math import inf
# import os
# import sys
from signal import SIG_DFL
from signal import SIGPIPE
from signal import signal
from typing import Union

import click
from asserttool import ic
from clicktool import click_add_options
from clicktool import click_global_options

signal(SIGPIPE, SIG_DFL)


def yn_question(prompt: str, verbose: Union[bool, int, float]):
    result = input(f"{prompt} [y/n]:")
    if verbose == inf:
        ic(result)
    if result.lower() == "y":
        return True
    return False


def passphrase_prompt(
    note: str,
    *,
    verbose: Union[bool, int, float],
):
    note = note.strip()
    assert len(note) > 0
    prompt = f"Enter {note} passphrase: "
    passphrase = input(prompt)
    passphrase = passphrase.encode("ascii")
    passphrase_v = input(prompt)
    passphrase_v = passphrase_v.encode("ascii")
    assert passphrase == passphrase_v
    assert len(passphrase) > 12
    if verbose:
        ic(passphrase)
    return passphrase


@click.group(no_args_is_help=True)
@click_add_options(click_global_options)
@click.pass_context
def cli(
    ctx,
    verbose: Union[bool, int, float],
    verbose_inf: bool,
):

    pass
