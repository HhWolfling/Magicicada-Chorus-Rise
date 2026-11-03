import numpy as np
import matplotlib.pyplot as plt

def simulate_octonion_fano_manifold():
    print("Computing 8D Octonion Fano Plane Signal Rotation...")

    # 1. Generate 7 Imaginary Basis Coordinates on Fano Plane (Unit Circle + Center)
    angles = np.linspace(0, 2 * np.pi, 7, endpoint=False)
    # 6 vertices along boundary + 1 center point (e7)
    x_basis = np.append(np.cos(angles), [0])
    y_basis = np.append(np.sin(angles), [0])
    labels = ['$e_1$', '$e_2$', '$e_3$', '$e_4$', '$e_5$', '$e_6$', '$e_7$']

    # 2. Simulate 8D Octonion Vector Rotation Signal over time t
    t = np.linspace(0, 2 * np.pi, 500)
    # 8 components: 1 real (x0) + 7 imaginary (x1..x7)
    components = np.zeros((8, len(t)))
    components[0] = np.cos(t) # Real scalar part x0
    
    # 7 Imaginary components driven by prime ratios
    prime_factors = [13, 17, 65.41, 196, 293.66, 1031, 1229]
    for idx, p in enumerate(prime_factors):
        components[idx + 1] = np.sin(p * t / 100) * np.exp(-0.05 * t)

    # Project 8D octonion norm into 2D Fano spatial density
    x_proj = np.zeros_like(t)
    y_proj = np.zeros_like(t)
    for i in range(7):
        x_proj += components[i + 1] * x_basis[i]
        y_proj += components[i + 1] * y_basis[i]

    # Setup Figure
    plt.style.use('dark_background')
    fig, ax = plt.subplots(figsize=(9, 9), facecolor='#05050A')
    ax.set_facecolor('#05050A')

    # Draw Fano Plane Triangular Structure Lines
    # Outer circle
    circle = plt.Circle((0, 0), 1.0, color='#121C2B', fill=False, linestyle='--', linewidth=1.5)
    ax.add_patch(circle)

    # Fano Triangles
    fano_edges = [(0, 2), (2, 4), (4, 0), (1, 3), (3, 5), (5, 1)]
    for e1, e2 in fano_edges:
        ax.plot([x_basis[e1], x_basis[e2]], [y_basis[e1], y_basis[e2]], 
                color='#1A2B4C', linewidth=1.2, alpha=0.7)

    # Plot 8D Trajectory Orbit
    ax.plot(x_proj, y_proj, color='#00FFCC', linewidth=1.8, alpha=0.9, 
            label='Octonion Signal Trajectory $\mathbf{O}(t) \in \mathbb{O}$')
    ax.fill(x_proj, y_proj, color='#00FFCC', alpha=0.1)

    # Plot Basis Nodes (e1..e7)
    for i in range(7):
        ax.scatter([x_basis[i]], [y_basis[i]], color='#FF007F' if i < 6 else '#FFD700', s=220, zorder=5)
        ax.text(x_basis[i] * 1.15, y_basis[i] * 1.15, labels[i], 
                color='#FFD700', fontsize=12, fontweight='bold', ha='center', va='center')

    # Central Core Node (x0 Real Anchor)
    ax.scatter([0], [0], color='#FFD700', s=300, zorder=6, label='Real Unit $e_0$ (Core Anchor)')

    # Styling
    ax.set_title("HYPERCOMPLEX OCTONION SIGNAL ROTATION ($\mathbb{O}$-MANIFOLD)\nNon-Associative 8D Fano Plane Projection", 
                 color='#00FFCC', fontsize=12, fontweight='bold', pad=20)
    ax.set_xlim(-1.4, 1.4)
    ax.set_ylim(-1.4, 1.4)
    ax.axis('off')
    ax.legend(loc='lower right', facecolor='#0A0A14', edgecolor='#1A2B4C')

    plt.tight_layout()
    plt.savefig("octonion_manifold_rotation.png", dpi=300, facecolor=fig.get_facecolor())
    print("Saved Octonion Fano plot as 'octonion_manifold_rotation.png'")
    plt.show()

# Run
simulate_octonion_fano_manifold()