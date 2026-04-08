import numpy as np
import matplotlib.pyplot as plt

# Simulation parameters
dt = 0.1
time = np.arange(0, 20, dt)

# System (simple 1D system)
setpoint = 10
position = 0
velocity = 0

# PID gains (you tuned these)
Kp = 1.2
Ki = 0.05
Kd = 0.8

# PID variables
integral = 0
prev_error = 0

positions = []
errors = []

for t in time:
    error = setpoint - position
    integral += error * dt
    derivative = (error - prev_error) / dt

    # PID control
    control = Kp * error + Ki * integral + Kd * derivative

    # System update (simple physics)
    acceleration = control
    velocity += acceleration * dt
    position += velocity * dt

    positions.append(position)
    errors.append(error)

    prev_error = error

# Plot results
plt.figure()

plt.subplot(2,1,1)
plt.plot(time, positions, label="Position")
plt.axhline(setpoint, linestyle="--", label="Setpoint")
plt.title("PID Control System Response")
plt.ylabel("Position")
plt.legend()
plt.grid()

plt.subplot(2,1,2)
plt.plot(time, errors, label="Error", color="red")
plt.xlabel("Time")
plt.ylabel("Error")
plt.legend()
plt.grid()

plt.tight_layout()
plt.show()
