# -*- coding: utf-8 -*-
class VRAMCircuitBreaker(Exception):
    pass

class VRAMMeltdownGuard:
    """Monitors memory ceiling and hardware trips ESTOP at 50.0 GB threshold."""
    def __init__(self, ceiling_gb: float = 50.0):
        self.ceiling_gb = ceiling_gb
        self.current_allocated_gb = 0.0

    def record_allocation(self, size_gb: float) -> bool:
        if self.current_allocated_gb + size_gb >= self.ceiling_gb:
            raise VRAMCircuitBreaker(
                f"[EMERGENCY ESTOP] Memory allocation requested {size_gb:.2f}GB exceeds 50.0GB ceiling! (Current: {self.current_allocated_gb:.2f}GB)"
            )
        self.current_allocated_gb += size_gb
        return True

    def reset(self):
        self.current_allocated_gb = 0.0
