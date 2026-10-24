# -*- coding: utf-8 -*-
import math

class DampingController:
    """Enforces 1.35x geometric damping scalar under load overload."""
    def __init__(self, damping_factor: float = 1.35, overload_threshold: float = 0.85):
        self.damping_factor = damping_factor
        self.overload_threshold = overload_threshold
        self.is_damped = False

    def evaluate_load(self, current_load: float) -> float:
        if current_load > self.overload_threshold:
            self.is_damped = True
            return self.damping_factor
        self.is_damped = False
        return 1.0
