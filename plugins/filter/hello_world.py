"""A hello-world filter plugin in foo.bar."""

from __future__ import absolute_import, division, print_function

__metaclass__ = type

DOCUMENTATION = r"""
  name: hello-world
  author: Luca Berton <luca@ansiblepilot.com>
  version_added: "1.0.0"  # same as collection version
  short_description: hello world
  description:
      - This filter returns the hello from a name input.
  positional: _input
  options:
    _input:
      description: Name to show.
      type: raw
      required: true
"""

def _hello_world(name):
    """Returns Hello message."""
    return "Hello, " + name


class FilterModule:
    """filter plugin."""

    def filters(self):
        """filter plugin."""
        return {"hello_world": _hello_world}
