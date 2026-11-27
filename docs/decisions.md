# Decision log

For each decision: what was chosen, the alternatives, and why. Talk material.

| Date | Decision | Alternatives | Why |
|------|----------|--------------|-----|
| | Immutable frozen dataclasses; methods return new objects | Mutable objects updated in place | |
| | Copy mappings on construction (`MappingProxyType(dict(...))`) | Wrap caller's dict directly | |
| | `players_tiles` representation: _undecided_ | dict + MappingProxyType / tuple indexed by player / frozenset | |
| | Hashable game state: _undecided_ | | |
