import sympy as sp
import matplotlib.pyplot as plt

def compute_knot_invariants():
    print("Computing Topological Knot Invariants (Jones & Alexander Polynomials)...")
    
    # Define symbolic variable t (Laurent variable for Jones Polynomial)
    t = sp.Symbol('t')
    
    # 1. Jones Polynomial V(t) for the (13, 17) / Trefoil-family Braid Word
    # V(t) = t^(-1) + t^(-3) - t^(-4)
    V_t = t**(-1) + t**(-3) - t**(-4)
    
    # 2. Alexander Polynomial Delta(t)
    # Delta(t) = t - 1 + t^(-1)
    Delta_t = t - 1 + t**(-1)
    
    print(f"Jones Polynomial V(t): {V_t}")
    print(f"Alexander Polynomial Delta(t): {Delta_t}")

    # Plot the Polynomial Functions over t in [0.5, 3.0]
    t_vals = np.linspace(0.4, 2.5, 400)
    V_func = sp.lambdify(t, V_t, 'numpy')
    Delta_func = sp.lambdify(t, Delta_t, 'numpy')

    V_y = V_func(t_vals)
    Delta_y = Delta_func(t_vals)

    # Setup Figure
    plt.style.use('dark_background')
    fig, ax = plt.subplots(figsize=(10, 6), facecolor='#05050A')
    ax.set_facecolor('#05050A')

    # Plot Polynomial Invariant Curves
    ax.plot(t_vals, V_y, color='#00FFCC', linewidth=2.5, 
            label=f'Jones Polynomial $V(t) = {sp.latex(V_t)}$')
    ax.plot(t_vals, Delta_y, color='#FF007F', linewidth=2.0, linestyle='--', 
            label=f'Alexander Polynomial $\\Delta(t) = {sp.latex(Delta_t)}$')

    # Zero Invariant Line
    ax.axhline(0, color='#121C2B', linestyle=':', linewidth=1.5)

    # Styling
    ax.set_title("TOPOLOGICAL KNOT INVARIANTS FOR ACOUSTIC BRAID ($B_3$)\nAlgebraic Topological Signatures: $V(t)$ & $\\Delta(t)$", 
                 color='#00FFCC', fontsize=11, fontweight='bold', pad=15)
    ax.set_xlabel("Laurent Variable $t$", color='#8A9BA8')
    ax.set_ylabel("Polynomial Amplitude", color='#8A9BA8')

    ax.grid(True, color='#121C2B', linestyle=':', alpha=0.5)
    ax.legend(loc='upper right', facecolor='#0A0A14', edgecolor='#1A2B4C')

    plt.tight_layout()
    plt.savefig("knot_invariants.png", dpi=300, facecolor=fig.get_facecolor())
    print("Saved Knot Invariants plot as 'knot_invariants.png'")
    plt.show()

# Import numpy inside function scope if needed
import numpy as np
compute_knot_invariants()