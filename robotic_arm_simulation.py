import numpy as np
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation

class RoboticArm:
    def __init__(self, link_lengths):
        self.link_lengths = link_lengths
        self.joint_angles = np.zeros(len(link_lengths))

    def forward_kinematics(self):
        x = np.cumsum([0] + [l * np.cos(np.sum(self.joint_angles[:i + 1])) for i, l in enumerate(self.link_lengths)])
        y = np.cumsum([0] + [l * np.sin(np.sum(self.joint_angles[:i + 1])) for i, l in enumerate(self.link_lengths)])
        return x, y

    def update_joint_angles(self, joint_index, angle):
        self.joint_angles[joint_index] = angle

    def plot(self):
        x, y = self.forward_kinematics()
        plt.plot(x, y, 'o-', linewidth=2, markersize=8)
        plt.xlim(-sum(self.link_lengths), sum(self.link_lengths))
        plt.ylim(-sum(self.link_lengths), sum(self.link_lengths))
        plt.gca().set_aspect('equal', adjustable='box')

def update(frame, arm):
    plt.clf()
    arm.update_joint_angles(1, np.sin(frame / 10))
    arm.plot()

if __name__ == "__main__":
    link_lengths = [2, 2, 1]
    robotic_arm = RoboticArm(link_lengths)

    fig = plt.figure()
    ani = FuncAnimation(fig, update, fargs=(robotic_arm,), frames=100, interval=100)
    plt.show()
