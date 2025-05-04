# spine_visualizer.py
import numpy as np
import matplotlib.pyplot as plt

class SpineVisualizer:
    """
    Demonstrates custom subplot styling using axis spine manipulation, text overlays,
    and curve visualization in a grid layout.
    """

    @staticmethod
    def display_spines():
        x = np.linspace(-10, 10, 400)
        y_funcs = [
            lambda x: np.log(np.abs(x) + 1) * np.sign(x),
            lambda x: np.exp(-x**2 / 10) * np.cos(x),
            lambda x: x**3 - 6*x,
            lambda x: np.abs(x) * np.sin(x / 2)
        ]

        titles = ["Log Sign Curve", "Modulated Cosine", "Cubic Polynomial", "Sinusoidal Absolute"]
        fig, axs = plt.subplots(2, 2, figsize=(12, 8))
        fig.suptitle("Axis Spine Manipulation Showcase", fontsize=16, color='navy')

        for ax, func, label in zip(axs.flat, y_funcs, titles):
            y = func(x)
            ax.plot(x, y, color='darkslategray', linewidth=2)
            ax.set_facecolor('#f8f9fa')
            ax.text(0, 0, label, fontsize=12, ha='center', va='center', style='italic', color='maroon')

            # Spine customization
            ax.spines['top'].set_visible(False)
            ax.spines['right'].set_visible(False)
            ax.spines['left'].set_position(('outward', 10))
            ax.spines['bottom'].set_position(('outward', 10))

            for spine in ax.spines.values():
                spine.set_linewidth(1.5)
                spine.set_color('darkred')

            ax.set_xticks([])
            ax.set_yticks([])

        plt.tight_layout(rect=[0, 0.03, 1, 0.95])
        plt.show()


if __name__ == "__main__":
    SpineVisualizer.display_spines()
