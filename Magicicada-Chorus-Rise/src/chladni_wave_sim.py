import numpy as np
import matplotlib.pyplot as plt

def simulate_chladni_plate(n1, m1, n2, m2, title, filename):
    # Create 2D grid representing square plate [-1, 1] x [-1, 1]
    x = np.linspace(-1, 1, 600)
    y = np.linspace(-1, 1, 600)
    X, Y = np.meshgrid(x, y)

    # 2D Chladni Standing Wave Formula
    # Nodal lines occur where W(X, Y) = 0
    W1 = np.sin(n1 * np.pi * X) * np.sin(m1 * np.pi * Y) - np.sin(m1 * np.pi * X) * np.sin(n1 * np.pi * Y)
    W2 = np.sin(n2 * np.pi * X) * np.sin(m2 * np.pi * Y) - np.sin(m2 * np.pi * X) * np.sin(n2 * np.pi * Y)
    
    # Combined Mixtum Pattern
    W_mixtum = W1 + 0.6 * W2

    # Setup Plot
    plt.style.use('dark_background')
    fig, ax = plt.subplots(figsize=(8, 8), facecolor='#05050A')
    ax.set_facecolor('#05050A')

    # Contour map of absolute displacement (0 displacement = sand accumulates)
    sand_density = np.exp(-15 * np.abs(W_mixtum))

    im = ax.imshow(sand_density, cmap='magma', extent=[-1, 1, -1, 1], origin='lower')

    ax.set_title(title, color='#00FFCC', fontsize=12, fontweight='bold', pad=15)
    ax.axis('off')

    plt.tight_layout()
    plt.savefig(filename, dpi=300, facecolor=fig.get_facecolor())
    print(f"Saved Chladni pattern as '{filename}'")
    plt.show()

# Run 1: Low C2 Core Resonance (65.41 Hz) -> Fundamental Mode (m=2, n=3)
simulate_chladni_plate(2, 3, 3, 2, 
                       "CHLADNI WAVE PATTERN: 65.41 Hz (C2 CORE RESONANCE)\nNodal Sand Distribution Mode (2,3)", 
                       "chladni_65Hz_core.png")

# Run 2: High Harmonic Lock (293.66 Hz) -> Upper Harmonic Mode (m=5, n=6)
simulate_chladni_plate(5, 6, 6, 5, 
                       "CHLADNI WAVE PATTERN: 293.66 Hz (D4 OPEN STRING HARMONIC)\nNodal Sand Distribution Mode (5,6)", 
                       "chladni_293Hz_harmonic.png")