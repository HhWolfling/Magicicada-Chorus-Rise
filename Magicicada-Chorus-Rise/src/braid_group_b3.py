import numpy as np
import matplotlib.pyplot as plt

def generate_braid_group_b3():
    print("Computing B_3 Non-Abelian Braid Group Trajectories...")
    
    # Parameter t along the braid length [0, 4pi]
    t = np.linspace(0, 4 * np.pi, 1000)
    
    # 3-Strand Parametric Braids
    # Strand 1: Kinetic Transient (293.66 Hz - Magenta)
    x1 = 0.5 * np.cos(t)
    y1 = 0.5 * np.sin(t)
    z1 = t
    
    # Strand 2: Grounded Core (65.41 Hz - Gold)
    x2 = 0.5 * np.cos(t + 2 * np.pi / 3)
    y2 = 0.5 * np.sin(t + 2 * np.pi / 3)
    z2 = t
    
    # Strand 3: Harmonic Bridge (196.00 Hz - Cyan)
    x3 = 0.5 * np.cos(t + 4 * np.pi / 3)
    y3 = 0.5 * np.sin(t + 4 * np.pi / 3)
    z3 = t

    # Setup 3D Plot
    plt.style.use('dark_background')
    fig = plt.figure(figsize=(10, 8), facecolor='#05050A')
    ax = fig.add_subplot(111, projection='3d')
    ax.set_facecolor('#05050A')

    # Plot 3 Luminous Strands
    ax.plot(x1, y1, z1, color='#FF007F', linewidth=2.5, label='Strand 1: $293.66\\text{ Hz}$ (Kinetic Transient)')
    ax.plot(x2, y2, z2, color='#FFD700', linewidth=3.0, label='Strand 2: $65.41\\text{ Hz}$ (Core Anchor)')
    ax.plot(x3, y3, z3, color='#00FFCC', linewidth=2.5, label='Strand 3: $196.00\\text{ Hz}$ (Harmonic Bridge)')

    # Add crossing node markers
    crossings = np.linspace(0, 4 * np.pi, 9)
    for idx, tc in enumerate(crossings[:-1]):
        ax.scatter([0.5 * np.cos(tc)], [0.5 * np.sin(tc)], [tc], color='#FFFFFF', s=40, zorder=5)

    # Styling
    ax.set_title("NON-ABELIAN BRAID GROUP TOPOGRAPHY ($B_3$)\nParametric Phase Word: $w = \\sigma_1 \\sigma_2^{-1} \\sigma_1 \\sigma_2^{-1}$", 
                 color='#00FFCC', fontsize=11, fontweight='bold', pad=15)

    ax.xaxis.pane.fill = False
    ax.yaxis.pane.fill = False
    ax.zaxis.pane.fill = False
    ax.grid(True, color='#121C2B', linestyle=':', alpha=0.5)
    ax.legend(loc='upper right', facecolor='#0A0A14', edgecolor='#1A2B4C')

    plt.tight_layout()
    plt.savefig("braid_group_b3.png", dpi=300, facecolor=fig.get_facecolor())
    print("Saved B3 Braid plot as 'braid_group_b3.png'")
    plt.show()

# Run
generate_braid_group_b3()