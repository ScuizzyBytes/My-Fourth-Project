<div align="center">

# ⚡ Custom Arena Allocator

  <p><b>A low-level memory management system built from scratch in Python using <code>ctypes</code></b></p>

  <div>
    <img src="https://img.shields.io/badge/Python-3776AB?style=for-the-badge&logo=python&logoColor=white" alt="Python" />
    <img src="https://img.shields.io/badge/Ctypes-Raw%20Memory-orange?style=for-the-badge" alt="Ctypes" />
    <img src="https://img.shields.io/badge/Architecture-First--Fit-blueviolet?style=for-the-badge" alt="First-Fit Architecture" />
  </div>

</div>

---

<div id="overview">

## 🎯 Project Overview

This project implements a manual **Arena Allocator** in Python. By bypassing standard Python high-level memory allocation, it interacts directly with byte buffers using C-style memory structures (`ctypes.Structure`) and pointer arithmetic.

</div>

<div id="features">

## 🚀 Key Features

- **Continuous Heap Buffer:** Allocates a single, raw contiguous block of memory on initialization.
- **Header Metadata (`BlockHeader`):** Embeds C-aligned metadata (payload size & availability status) directly before each allocated memory slice.
- **First-Fit Allocation Strategy:** Traverses memory sequentially to discover eligible free blocks and dynamic block splitting.
- **Zero External Dependencies:** Built strictly with Python standard library modules (`ctypes`).

</div>

<div id="architecture">

## 🧠 Architecture & Memory Layout

Each block on the heap is split into metadata and payload:

```
+------------------+------------------+------------------+------------------+
| BlockHeader (8B) | Payload (Data)   | BlockHeader (8B) | Payload (Data)   |
+------------------+------------------+------------------+------------------+
| size | is_free   | User Memory      | size | is_free   | User Memory      |
+------------------+------------------+------------------+------------------+
^                                     ^
|--- Header Offset                    |--- Next Block Offset
```

### Struct Breakdown
* **`size`** (`c_uint32` - 4 Bytes): Usable payload space following the header.
* **`is_free`** (`c_bool` - 1 Byte): Availability status indicator.

</div>

<div id="usage">

## 💻 Quickstart Guide

### 1. Run the Example

Execute `main.py` directly using Python 3:

```bash
python main.py
```

### 2. Code Example

```python
import ctypes
from arena_core import Arena

# Initialize a 1024-byte contiguous memory arena
arena = Arena(size=1024)

# Allocate an 800-byte raw payload block
payload_offset = arena.allocate(800)

print(f"Payload allocated at byte offset: {payload_offset}")
```

</div>

---

<div align="center">
  <sub>Built for low-level systems engineering exploration in Python.</sub>
</div>
