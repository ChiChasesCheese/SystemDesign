"""Trellis: skeleton-constrained knowledge cards.

A skeleton (YAML mind map) defines topics, their order, and prerequisite
edges. Cards are Obsidian-native markdown files attached to skeleton nodes
as leaves. The build compiles the vault into an Anki .apkg with stable
GUIDs so re-imports update cards in place.
"""

__version__ = "0.1.0"
