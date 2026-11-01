import numpy as np
import matplotlib.pyplot as plt

def generate_3d_chladni_clean(n=2, m=3, l=4, res=100):
    print("Computing clean 3D Volumetric Chladni Chamber...")
    x = np.linspace(-1, 1, res)
    y = np.linspace(-1, 1, res)
    z = np.linspace(-1, 1, res)
    X, Y, Z = np.meshgrid(x, y, z)

    # 3D Standing Wave Field Equation
    W = (np.sin(n * np.pi * X) * np.sin(m * np.pi * Y) * np.sin(l * np.pi * Z) +
         np.sin(m * np.pi * X) * np.sin(l * np.pi * Y) * np.sin(n * np.pi * Z) +
         np.sin(l * np.pi * X) * np.sin(n * np.pi * Y) * np.sin(m * np.pi * Z))

    # Isolate ONLY strict nodal regions (where standing wave cancels to ~0)
    nodal_mask = np.abs(W) < 0.08  # Transparent interior nodal shell

    # Styling
    plt.style.use('dark_background')
    fig = plt.figure(figsize=(10, 8), facecolor='#05050A')
    ax = fig.add_subplot(111, projection='3d')
    ax.set_facecolor('#05050A')

    # Plot nodal points as glowing particle shells
    xs = X[nodal_mask]
    ys = Y[nodal_mask]
    zs = Z[nodal_mask]
    c_vals = np.sqrt(xs**2 + ys**2 + zs**2) # Radial color gradient

    ax.scatter(xs, ys, zs, c=c_vals, cmap='plasma', s=0.8, alpha=0.4)

    ax.set_title("3D VOLUMETRIC CHLADNI ACOUSTIC CHAMBER (CLEAN ISOSURFACE)\nNodal Standing Wave Geometry Mode (2,3,4)", 
                 color='#00FFCC', fontsize=11, fontweight='bold', pad=15)

    # Transparent plot background panes
    ax.xaxis.pane.fill = False
    ax.yaxis.pane.fill = False
    ax.zaxis.pane.fill = False
    ax.grid(True, color='#121C2B', linestyle=':', alpha=0.5)

    plt.tight_layout()
    plt.savefig("chladni_3d_volumetric_clean.png", dpi=300, facecolor=fig.get_facecolor())
    print("Saved clean 3D plot as 'chladni_3d_volumetric_clean.png'")
    plt.show()

generate_3d_chladni_clean()