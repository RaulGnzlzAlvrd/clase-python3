"""
x = 5
y = 10
"""

# Calcula la relación señal ruido mediante la fórmula 10log_10(señal / ruido)
import math

signal_power = 9
noise_power = 10
ratio = signal_power / noise_power
decibeles = 10 * math.log10(ratio)
print(decibeles)
