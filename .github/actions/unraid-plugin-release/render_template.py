#!/usr/bin/env python3
"""Render a Jinja2 template for the unraid-plugin-release composite action.

Replaces the templating step that used dkaser/jinja2-action. Its contract is
kept: the top-level keys of the JSON data file become template variables, `env`
is the process environment, undefined names render empty unless --strict is
given, and the output ends with exactly one newline after the render.

Behaviour follows dkaser/jinja2-action at commit 44d5cd5 (Derek Kaser, a fork of
cuchi/jinja2-action). No code is copied from it.
"""

import argparse
import json
import os

from jinja2 import StrictUndefined, Template


def render(template_path, output_path, data_path=None, strict=False):
    variables = {'env': os.environ}
    if data_path:
        with open(data_path, 'r') as file:
            variables.update(json.load(file))

    with open(template_path, 'r') as file:
        template_kwargs = {'undefined': StrictUndefined} if strict else {}
        template = Template(file.read(), **template_kwargs)

    with open(output_path, 'w') as file:
        file.write(template.render(**variables) + '\n')


if __name__ == '__main__':
    parser = argparse.ArgumentParser(description='Render a Jinja2 template to a file.')
    parser.add_argument('template')
    parser.add_argument('output')
    parser.add_argument('--data', help='JSON file whose top-level keys become template variables')
    parser.add_argument('--strict', action='store_true', help='fail on undefined variables')
    args = parser.parse_args()
    render(args.template, args.output, args.data, args.strict)
