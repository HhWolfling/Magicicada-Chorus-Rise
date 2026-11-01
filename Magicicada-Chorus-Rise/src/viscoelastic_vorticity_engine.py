import numpy as np
import matplotlib.pyplot as plt

def simulate_viscoelastic_vorticity(grid_size=400):
    print("Computing Viscoelastic Vorticity Shear Engine...")
    
    # Setup 2D spatial grid [-2, 2] x [-2, 2]
    x = np.linspace(-2, 2, grid_size)
    y = np.linspace(-2, 2, grid_size)
    X, Y = np.meshgrid(x, y)

    # Velocity field modeling jet collision (v1 kinetic spark vs v2 grounded mass)
    # Jet stream (Track 1) pushing from left to right along Y=0
    u_x = np.exp(-4 * Y**2) * np.cos(3 * X) + 0.5 * np.sin(13 * Y)
    u_y = np.exp(-4 * X**2) * np.sin(3 * Y) + 0.5 * np.cos(17 * X)

    # Compute Vorticity Field w = du_y/dx - du_x/dy using 2D finite difference
    dx = x[1] - x[0]
    dy = y[1] - y[0]

    du_y_dx = np.gradient(u_y, dx, axis=1)
    du_x_dy = np.gradient(u_x, dy, axis=0)

    vorticity = du_y_dx - du_x_dy

    # Setup Figure
    plt.style.use('dark_background')
    fig, ax = plt.subplots(figsize=(10, 8), facecolor='#05050A')
    ax.set_facecolor('#05050A')

    # Plot Vorticity Heatmap (Von Kármán Shear Eddies)
    im = ax.imshow(vorticity, cmap='magma', extent=[-2, 2, -2, 2], origin='lower', alpha=0.9)
    
    # Overlay Streamline Vectors
    stride = 16
    ax.streamplot(X[::stride, ::stride], Y[::stride, ::stride], 
                  u_x[::stride, ::stride], u_y[::stride, ::stride], 
                  color='#00FFCC', density=0.8, linewidth=0.8, arrowsize=0.8)

    # Highlight Core Shear Node (65.41 Hz Anchor)
    ax.scatter([0], [0], color='#FFD700', s=150, zorder=5, label='65.41 Hz Shear Origin')

    # Annotations & Styling
    ax.set_title("VISCOELASTIC VORTICITY ENGINE: NON-LINEAR FLUID MIXING\nSpatial Shear Vorticity $\\omega = \\nabla \\times \\mathbf{u}$ & Von Kármán Vortex Street", 
                 color='#00FFCC', fontsize=11, fontweight='bold', pad=15)
    ax.set_xlabel("Channel X-Axis [Kinetic Jet Axis]", color='#8A9BA8')
    ax.set_ylabel("Channel Y-Axis [Viscous Substrate Axis]", color='#8A9BA8')

    fig.colorbar(im, ax=ax, label="Vorticity Index $\\omega = \\partial u_y/\\partial x - \\partial u_x/\\partial y$")
    ax.legend(loc='upper right', facecolor='#0A0A14', edgecolor='#1A2B4C')

    plt.tight_layout()
    plt.savefig("viscoelastic_vorticity_engine.png", dpi=300, facecolor=fig.get_facecolor())
    print("Saved Vorticity plot as 'viscoelastic_vorticity_engine.png'")
    plt.show()

# Run
simulate_viscoelastic_vorticity()