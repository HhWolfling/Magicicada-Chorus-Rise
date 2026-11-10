# 🌀 Magicicada Chorus Rise: Non-Linear Phase-Lock & Topological DSP Engine

[![License: CC BY 4.0](https://img.shields.io/badge/License-CC_BY_4.0-lightgrey.svg)](https://creativecommons.org/licenses/by/4.0/)
[![Live WebGL Canvas](https://img.shields.io/badge/Live_WebGL-Prime_Torus_Manifold-00FFCC?style=for-the-badge&logo=three.js)](https://hhwolfling.github.io/Magicicada-Chorus-Rise/prime_torus_webgl.html)
[![GitHub Pages](https://img.shields.io/badge/Deployment-GitHub_Pages-FF007F?style=for-the-badge&logo=github)](https://hhwolfling.github.io/Magicicada-Chorus-Rise/)

> **A non-linear acoustic synthesis and physical state engine mapping non-Abelian braid groups ($B_3$), prime torus knots ($(13, 17)$ on $\mathbb{T}^2$), viscoelastic vorticity dynamics, hypercomplex octonion rotations ($\mathbb{O}$), and biological relaxation oscillators.**

---

## 🌐 Live Interactive WebGL Visualizer

Experience the high-dimensional phase space directly in your browser:
* **Interactive Torus Engine**: [https://hhwolfling.github.io/Magicicada-Chorus-Rise/prime_torus_webgl.html](https://hhwolfling.github.io/Magicicada-Chorus-Rise/prime_torus_webgl.html)
* **Project Portal**: [https://hhwolfling.github.io/Magicicada-Chorus-Rise/](https://hhwolfling.github.io/Magicicada-Chorus-Rise/)

---

## 📐 Mathematical & Physical Framework

The engine models acoustic and physical signal interactions across four core pillars:

### 1. The Commutator Operator ($\Phi$)
Energy transfer between kinetic transient drive vectors ($H$) and structural anchor vectors ($C$) is governed by non-commutative operator dynamics:

$$\Phi = [H, C] = H \cdot C - C \cdot H$$

*Plaintext version*: Phi equals the commutator bracket of H and C, which is H times C minus C times H.

When $H$ and $C$ do not commute, continuous energy dissipate collapses into discrete, periodic cardiac relaxation pulses (systole/diastole).

### 2. Prime Brood Coprimality & Torus Winding ($\mathbb{T}^2$)
The system locks phase trajectories onto a 2D modular torus surface using the $13$-year (*Magicicada tredecim*) and $17$-year (*Magicicada septendecim*) prime brood ratio:

$$\gcd(13, 17) = 1, \quad N_{\text{sync}} = 13 \times 17 = 221 \text{ years}$$

*Plaintext version*: The greatest common divisor of 13 and 17 equals 1, and the synchronization interval N_sync equals 13 times 17, which is 221 years.

Because $p=13$ and $q=17$ are prime integers, the phase winding traces a closed $(13, 17)$ prime torus knot on $\mathbb{T}^2$ with zero self-intersection and zero Ohmic drag:

$$\Omega = 0$$

*Plaintext version*: The Ohmic drag Omega equals zero.

### 3. Hypercomplex Octonion Rotations ($\mathbb{O}$)
Signal coordinates rotate across 8-dimensional normed division algebra governed by the 7 imaginary units of the Fano Plane ($e_1 \dots e_7$):

$$\mathbf{O}(t) = x_0(t) + \sum_{i=1}^{7} x_i(t) e_i$$

*Plaintext version*: O(t) is an octonion signal equal to real component x_0(t) plus the sum from i=1 to 7 of x_i(t) times imaginary basis unit e_i.

Because octonionic multiplication is non-associative ($(e_i \cdot e_j) \cdot e_k \neq e_i \cdot (e_j \cdot e_k)$), phase chirps remain uncollapsible in high-dimensional projections.

### 4. Topological Knot Invariants ($B_3$)
The 3-strand braid generator word $w = \sigma_1 \sigma_2^{-1} \sigma_1 \sigma_2^{-1}$ maps to the immutable Trefoil Knot ($3_1$), yielding time-reversibility under the Alexander Polynomial:

$$\Delta(t) = t - 1 + t^{-1}, \quad V(t) = t^{-1} + t^{-3} - t^{-4}$$

*Plaintext version*: Alexander polynomial Delta(t) equals t minus 1 plus 1/t, and Jones polynomial V(t) equals 1/t plus 1/t^3 minus 1/t^4.

---

## 📁 Repository Module Manifest

| Script / Asset | Description |
| :--- | :--- |
| `prime_torus_webgl.html` | Interactive WebGL Three.js browser engine with real-time $p, q, \tau$ slider controls. |
| `src/mixtum_dsp.py` | Non-linear DSP synthesizer processing STFT matrices into `mixtum_output.wav`. |
| `src/octonion_manifold_rotation.py` | 8D Fano plane non-associative signal trajectory map. |
| `src/knot_invariants.py` | SymPy verification of Jones $V(t)$ and Alexander $\Delta(t)$ topological invariants. |
| `src/prime_kamea_tetractys.py` | $4 \times 4$ Prime Brood Kamea magic square and Pythagorean Tetractys grid. |
| `src/viscoelastic_vorticity_engine.py` | 2D fluid shear vorticity matrix $\omega = \nabla \times \mathbf{u}$ generating von Kármán eddies. |
| `src/braid_group_b3.py` | 3D non-Abelian braid topography visualization for frequencies $65.41\text{ Hz}, 196\text{ Hz}, 293.66\text{ Hz}$. |
| `src/chladni_3d_volumetric_clean.py` | 3D volumetric standing wave nodal isosurface acoustic chamber. |

---

## ⚡ Quickstart

```bash
# 1. Clone repository
git clone [https://github.com/HhWolfling/Magicicada-Chorus-Rise.git](https://github.com/HhWolfling/Magicicada-Chorus-Rise.git)
cd Magicicada-Chorus-Rise

# 2. Install core dependencies
pip install -r requirements.txt

# 3. Synthesize the Mixtum audio relaxation pulse
python src/mixtum_dsp.py
