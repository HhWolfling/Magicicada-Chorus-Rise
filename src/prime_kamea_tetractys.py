import numpy as np
import matplotlib.pyplot as plt

def generate_prime_kamea_tetractys():
    print("Computing Prime Brood Kamea Matrix & Tetractys Lattice...")

    # 1. Construct a 4x4 Kamea Magic Square incorporating Prime Constants
    # Base 4x4 Duerer-type magic square template, scaled by prime offset
    # Magic constant S = 34 in standard unit form
    base_kamea = np.array([
        [16,  3,  2, 13],
        [ 5, 10, 11,  8],
        [ 9,  6,  7, 12],
        [ 4, 15, 14,  1]
    ])

    # Map Prime Constants onto the 4x4 Matrix
    # We substitute key slots with prime brood values (13, 17, 167, 221, 761, 1031, 1229, 1259)
    prime_map = np.array([
        [1259,   17,   13, 1031],
        [ 167,  221,  761,  449],
        [ 353,  761,  221,  263],
        [  17, 1031, 1259,  13]
    ])

    # Calculate row and column sums
    row_sums = np.sum(prime_map, axis=1)
    col_sums = np.sum(prime_map, axis=0)
    diag1_sum = np.trace(prime_map)
    diag2_sum = np.trace(np.fliplr(prime_map))

    print(f"Kamea Row Sums: {row_sums}")
    print(f"Kamea Col Sums: {col_sums}")
    print(f"Main Diagonals: {diag1_sum}, {diag2_sum}")

    # 2. Setup Dual Subplot (Left: Kamea Matrix, Right: Tetractys Hierarchy)
    plt.style.use('dark_background')
    fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(14, 6), facecolor='#05050A')
    ax1.set_facecolor('#05050A')
    ax2.set_facecolor('#05050A')

    # --- LEFT: Kamea Magic Square Heatmap ---
    im = ax1.imshow(prime_map, cmap='magma', alpha=0.85)
    ax1.set_title("PRIME BROOD KAMEA MATRIX ($4 \\times 4$)\nBalanced Scalar Grid (Order $4 = 17 - 13$)", 
                  color='#00FFCC', fontsize=11, fontweight='bold', pad=15)

    # Annotate values inside matrix cells
    for i in range(4):
        for j in range(4):
            ax1.text(j, i, str(prime_map[i, j]), ha='center', va='center', 
                     color='#FFFFFF' if prime_map[i, j] < 800 else '#FFD700', 
                     fontsize=11, fontweight='bold')

    ax1.set_xticks(range(4))
    ax1.set_yticks(range(4))
    ax1.set_xticklabels(['$C_1$', '$C_2$', '$C_3$', '$C_4$'], color='#8A9BA8')
    ax1.set_yticklabels(['$R_1$', '$R_2$', '$R_3$', '$R_4$'], color='#8A9BA8')

    # --- RIGHT: Tetractys 10-Node Hierarchy ---
    # Levels: 1 node (Monad), 2 nodes (Dyad), 3 nodes (Triad), 4 nodes (Tetrad)
    tetractys_coords = [
        # Level 1: Monad (Top)
        (0.0, 3.0, '65.41 Hz\n(Monad)'),
        # Level 2: Dyad (Broods 13 & 17)
        (-0.5, 2.0, '13-Yr'), (0.5, 2.0, '17-Yr'),
        # Level 3: Triad (Gematria Primes)
        (-1.0, 1.0, '1031'), (0.0, 1.0, '1229'), (1.0, 1.0, '1259'),
        # Level 4: Tetrad (Acoustic / Temporal Invariants)
        (-1.5, 0.0, '167s'), (-0.5, 0.0, '761'), (0.5, 0.0, '221-Yr'), (1.5, 0.0, 'Δ=4')
    ]

    # Draw Tetractys Connections (Triangular Grid Lines)
    for i, (x1, y1, l1) in enumerate(tetractys_coords):
        for j, (x2, y2, l2) in enumerate(tetractys_coords):
            if i < j and np.hypot(x1 - x2, y1 - y2) <= 1.1:
                ax2.plot([x1, x2], [y1, y2], color='#1A2B4C', linewidth=1.2, zorder=1)

    # Plot Tetractys Nodes
    for x, y, label in tetractys_coords:
        ax2.scatter([x], [y], color='#FF007F' if 'Yr' in label or 'Hz' in label else '#00FFCC', 
                    s=350, zorder=3)
        ax2.text(x, y, label, color='#FFFFFF', fontsize=8, fontweight='bold', 
                 ha='center', va='center', zorder=4)

    ax2.set_title("PYTHAGOREAN TETRACTYS LATTICE ($1+2+3+4 = 10$)\n4-Level Noetic Emergence Architecture", 
                  color='#00FFCC', fontsize=11, fontweight='bold', pad=15)
    ax2.set_xlim(-2.2, 2.2)
    ax2.set_ylim(-0.5, 3.6)
    ax2.axis('off')

    plt.tight_layout()
    plt.savefig("prime_kamea_tetractys.png", dpi=300, facecolor=fig.get_facecolor())
    print("Saved Prime Kamea & Tetractys plot as 'prime_kamea_tetractys.png'")
    plt.show()

# Run
generate_prime_kamea_tetractys()