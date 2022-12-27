#!/usr/bin/env python3
# -*- coding: utf8 -*-

# pylint: disable=missing-docstring               # [C0111] docstrings are always outdated and wrong
# pylint: disable=missing-module-docstring        # [C0114]
# pylint: disable=fixme                           # [W0511] todo is encouraged
# pylint: disable=line-too-long                   # [C0301]
# pylint: disable=too-many-instance-attributes    # [R0902]
# pylint: disable=too-many-lines                  # [C0302] too many lines in module
# pylint: disable=invalid-name                    # [C0103] single letter var names, name too descriptive
# pylint: disable=too-many-return-statements      # [R0911]
# pylint: disable=too-many-branches               # [R0912]
# pylint: disable=too-many-statements             # [R0915]
# pylint: disable=too-many-arguments              # [R0913]
# pylint: disable=too-many-nested-blocks          # [R1702]
# pylint: disable=too-many-locals                 # [R0914]
# pylint: disable=too-few-public-methods          # [R0903]
# pylint: disable=no-member                       # [E1101] no member for base
# pylint: disable=attribute-defined-outside-init  # [W0201]
# pylint: disable=too-many-boolean-expressions    # [R0916] in if statement
from __future__ import annotations

from math import inf
from signal import SIG_DFL
from signal import SIGPIPE
from signal import signal

import click
from asserttool import ic
from click_auto_help import AHGroup
from clicktool import click_add_options
from clicktool import click_global_options

signal(SIGPIPE, SIG_DFL)


def yn_question(
    prompt: str,
    verbose: bool | int | float = False,
):
    result = input(f"{prompt} [y/n]: ")
    if verbose == inf:
        ic(result)
    if result.lower() == "y":
        return True
    return False


def passphrase_prompt(
    note: str,
    *,
    verbose: bool | int | float = False,
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


@click.group(no_args_is_help=True, cls=AHGroup)
@click_add_options(click_global_options)
@click.pass_context
def cli(
    ctx,
    verbose_inf: bool,
    verbose: bool | int | float = False,
):

    pass
