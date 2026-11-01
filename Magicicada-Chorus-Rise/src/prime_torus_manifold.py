import numpy as np
import matplotlib.pyplot as plt

def generate_prime_torus_knot(p=13, q=17, R=2.0, r=0.8):
    print(f"Computing Prime Torus Knot ({p},{q}) on T^2 Manifold...")
    
    # 1. Torus Surface Mesh
    u = np.linspace(0, 2 * np.pi, 60)
    v = np.linspace(0, 2 * np.pi, 60)
    U, V = np.meshgrid(u, v)
    
    X_torus = (R + r * np.cos(V)) * np.cos(U)
    Y_torus = (R + r * np.cos(V)) * np.sin(U)
    Z_torus = r * np.sin(V)

    # 2. Prime Torus Knot Trajectory (p=13, q=17)
    theta = np.linspace(0, 2 * np.pi, 2000)
    x_knot = (R + r * np.cos(q * theta)) * np.cos(p * theta)
    y_knot = (R + r * np.cos(q * theta)) * np.sin(p * theta)
    z_knot = r * np.sin(q * theta)

    # Setup 3D Plot
    plt.style.use('dark_background')
    fig = plt.figure(figsize=(10, 8), facecolor='#05050A')
    ax = fig.add_subplot(111, projection='3d')
    ax.set_facecolor('#05050A')

    # Draw Wireframe Torus Manifold
    ax.plot_wireframe(X_torus, Y_torus, Z_torus, color='#121C2B', alpha=0.3, linewidth=0.5)

    # Draw (13,17) Prime Torus Knot Trajectory
    ax.plot(x_knot, y_knot, z_knot, color='#00FFCC', linewidth=2.0, 
            label=f'Prime Torus Knot ({p},{q}) Trajectory')
    
    # Highlight Golden Intersection Core
    ax.scatter([x_knot[0]], [y_knot[0]], [z_knot[0]], color='#FFD700', s=80, label='65.41 Hz Phase Origin')

    # Styling
    ax.set_title(f"PRIME RESIDUE MODULAR TORUS MANIFOLD ($\\mathbb{{T}}^2$)\nPhase-Lock Winding Orbit: ({p},{q}) Prime Brood Ratio", 
                 color='#00FFCC', fontsize=11, fontweight='bold', pad=15)

    ax.xaxis.pane.fill = False
    ax.yaxis.pane.fill = False
    ax.zaxis.pane.fill = False
    ax.grid(True, color='#121C2B', linestyle=':', alpha=0.5)
    ax.legend(loc='upper right', facecolor='#0A0A14', edgecolor='#1A2B4C')

    plt.tight_layout()
    plt.savefig("prime_torus_manifold.png", dpi=300, facecolor=fig.get_facecolor())
    print("Saved Torus Knot plot as 'prime_torus_manifold.png'")
    plt.show()

# Run
generate_prime_torus_knot()