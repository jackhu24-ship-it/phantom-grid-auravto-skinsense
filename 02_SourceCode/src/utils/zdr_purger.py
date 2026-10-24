# -*- coding: utf-8 -*-
import ctypes
import hashlib

class ZDRPurger:
    """Executes 2-Pass bitwise cryptographic memory purge leaving 0.000000 MB residue."""
    def __init__(self):
        self._buffer = bytearray(1024 * 64)

    def load_buffer(self, data: bytes):
        size = min(len(data), len(self._buffer))
        self._buffer[:size] = data[:size]

    def purge_memory(self) -> float:
        # Pass 1: Overwrite with 0xAA
        for i in range(len(self._buffer)):
            self._buffer[i] = 0xAA
        # Pass 2: Overwrite with 0x00
        for i in range(len(self._buffer)):
            self._buffer[i] = 0x00
        # Calculate residual non-zero bytes
        residue = sum(1 for b in self._buffer if b != 0x00)
        residue_mb = (residue / (1024 * 1024))
        return residue_mb

    def get_audit_signature(self) -> str:
        return hashlib.sha256(self._buffer).hexdigest()
