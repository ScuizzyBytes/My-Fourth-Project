import ctypes  # noqa: F401

from arena_core import Arena

arena = Arena()

ptr = arena.allocate(800)

print(ptr)