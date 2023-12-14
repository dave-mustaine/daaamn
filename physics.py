import matplotlib.pyplot as plt

S = 1  # const in this problem
G = 9.81  # acceleration of gravity on the surface
position = 10  # start position, const
velocity = 0  # start velocity, const
air_drag = 0.4  # C const
air_density = 0.5  # ro const

mass = 1  # object of research

time_step = 0.001

values = [[], []]
forces = [[], []]
velocities = [[], []]

step = 0
time = 0

while True:
    equivalent_force = - mass * G - ((air_density * air_drag * S * velocity * abs(velocity)) / 2)
    a = equivalent_force / mass
    position += velocity * time_step + ((a * time_step ** 2) / 2)
    velocity += a * time_step

    values[0].append(time)
    values[1].append(position)

    forces[0].append(time)
    forces[1].append(equivalent_force)

    velocities[0].append(time)
    velocities[1].append(velocity)

    step += 1
    time += time_step

    if position < -100:
        break

print(time)

fig, ax = plt.subplots(1, 3)
# fig.tight_layout()

plt.figure(figsize=(10, 6))

plt.subplot(1, 3, 1)
plt.plot(values[0], values[1], color='red')
plt.title('Coordinate')

plt.subplot(1, 3, 2)
plt.plot(forces[0], forces[1], color='green')
plt.title('Forces')

plt.subplot(1, 3, 3)
plt.plot(velocities[0], velocities[1], color='blue')
plt.title('Velocity')

plt.show()
