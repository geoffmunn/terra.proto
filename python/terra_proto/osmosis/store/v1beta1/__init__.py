# Generated by the protocol buffer compiler.  DO NOT EDIT!
# sources: tree.proto
# plugin: python-betterproto
from dataclasses import dataclass
from typing import List

import betterproto


@dataclass(eq=False, repr=False)
class Node(betterproto.Message):
    children: List["Child"] = betterproto.message_field(1)


@dataclass(eq=False, repr=False)
class Child(betterproto.Message):
    index: bytes = betterproto.bytes_field(1)
    accumulation: str = betterproto.string_field(2)


@dataclass(eq=False, repr=False)
class Leaf(betterproto.Message):
    leaf: "Child" = betterproto.message_field(1)
