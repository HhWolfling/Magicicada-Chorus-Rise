# 🌀 Magicicada Chorus Rise: Non-Linear Phase-Lock & Topological DSP Engine

[![Live WebGL — Prime Torus](https://img.shields.io/badge/Live_WebGL-Prime_Torus_Manifold-00FFCC?style=for-the-badge&logo=three.js)](https://hhwolfling.github.io/Magicicada-Chorus-Rise)
[![Live WebGL — 8D Octonion](https://img.shields.io/badge/Live_WebGL-8D_Octonion_Fano-FFD700?style=for-the-badge&logo=three.js)](https://hhwolfling.github.io/Magicicada-Chorus-Rise/octonionic_shader_webgl.html)
[![Live WebGL — Sri Meru Octonion](https://img.shields.io/badge/Live_WebGL-Sri_Meru_Octonion-FF007F?style=for-the-badge&logo=webgl)](https://hhwolfling.github.io/Magicicada-Chorus-Rise/sri_meru_octonion_webgl.html)

> **A non-linear acoustic synthesis and physical state engine mapping non-Abelian braid groups ($B_3$), prime torus knots ($(13, 17)$ on $\mathbb{T}^2$), viscoelastic vorticity dynamics, hypercomplex octonion rotations ($\mathbb{O}$), and biological relaxation oscillators.**

---

## 🌐 Live Interactive WebGL Visualizers

Experience the high-dimensional phase spaces directly in your browser:

* **1. Prime Brood Torus Manifold ($(13, 17)$ on $\mathbb{T}^2$):** [https://hhwolfling.github.io/Magicicada-Chorus-Rise](https://hhwolfling.github.io/Magicicada-Chorus-Rise)[cite: 5]
* **2. 8D Octonionic Fano Plane Engine ($\mathbb{O}$):** [https://hhwolfling.github.io/Magicicada-Chorus-Rise/octonionic_shader_webgl.html](https://hhwolfling.github.io/Magicicada-Chorus-Rise/octonionic_shader_webgl.html)[cite: 6]
* **3. 8D Octonion × 3D Sri Meru Volumetric Manifold (with `13:17` Web Audio):** [https://hhwolfling.github.io/Magicicada-Chorus-Rise/sri_meru_octonion_webgl.html](https://hhwolfling.github.io/Magicicada-Chorus-Rise/sri_meru_octonion_webgl.html)[cite: 2]

---

## 📐 Mathematical & Physical Framework

The engine models acoustic and physical signal interactions across four core pillars:

### 1. The Commutator Operator ($\Phi$)
Energy transfer between kinetic transient drive vectors ($H$) and structural anchor vectors ($C$) is governed by non-commutative operator dynamics:

$$\Phi = [H, C] = H \cdot C - C \cdot H \neq 0$$

*Plaintext version*: Phi equals the commutator bracket of H and C, which is H times C minus C times H, and is non-zero.

When $H$ and $C$ are implemented as non-commuting 3D vector cross-products[cite: 2] or complex conjugate STFT spectra[cite: 3, 4], continuous energy dissipation collapses into discrete, periodic cardiac relaxation pulses (systole/diastole).

### 2. Prime Brood Coprimality & Torus Winding ($\mathbb{T}^2$)
The system locks phase trajectories onto a 2D modular torus surface using the $13$-year (*Magicicada tredecim*) and $17$-year (*Magicicada septendecim*) prime brood ratio:

$$\gcd(13, 17) = 1, \quad N_{\text{sync}} = 13 \times 17 = 221 \text{ years}$$

*Plaintext version*: The greatest common divisor of 13 and 17 equals 1, and the synchronization interval N_sync equals 13 times 17, which is 221 years.

Because $p=13$ and $q=17$ are prime integers, the phase winding traces a closed $(13, 17)$ prime torus knot on $\mathbb{T}^2$ with zero self-intersection and zero Ohmic drag[cite: 5]:

$$\Omega = 0$$

*Plaintext version*: The Ohmic drag Omega equals zero.

### 3. Hypercomplex Octonion Rotations ($\mathbb{O}$)
Signal coordinates rotate across an 8-dimensional normed division algebra governed by the real scalar axis ($x_0$) and the 7 imaginary units of the Fano Plane ($e_1 \dots e_7$)[cite: 1, 2, 5]:

$$\mathbf{O}(t) = x_0(t) + \sum_{i=1}^{7} x_i(t) e_i$$

*Plaintext version*: O(t) is an octonion signal equal to real component x_0(t) plus the sum from i=1 to 7 of x_i(t) times imaginary basis unit e_i.

Because octonionic multiplication is non-associative ($(e_i \cdot e_j) \cdot e_k \neq e_i \cdot (e_j \cdot e_k)$), phase chirps remain uncollapsible in high-dimensional projections[cite: 5].

### 4. Topological Knot Invariants ($B_3$)
The 3-strand braid generator word $w = \sigma_1 \sigma_2^{-1} \sigma_1 \sigma_2^{-1}$ maps to the immutable Trefoil Knot ($3_1$), yielding time-reversibility under the Alexander Polynomial[cite: 5]:

$$\Delta(t) = t - 1 + t^{-1}, \quad V(t) = t^{-1} + t^{-3} - t^{-4}$$

*Plaintext version*: Alexander polynomial Delta(t) equals t minus 1 plus 1/t, and Jones polynomial V(t) equals 1/t plus 1/t^3 minus 1/t^4.

---

## 📁 Repository Structure & Module Manifest

| Path / Asset | Description |
| :--- | :--- |
| `prime_torus_webgl.html` | Interactive WebGL Three.js browser engine with real-time $p, q, \tau$ slider controls[cite: 5]. |
| `octonionic_shader_webgl.html` | Interactive Three.js + GLSL raymarching visualizer computing the 8D octonion norm shell and 7 Fano triad couplings with $p, q$, field density, and phase velocity ($\tau$) controls[cite: 6]. |
| `sri_meru_octonion_webgl.html` | Volumetric raymarching WebGL visualizer projecting an 8D octonion field onto a 3D stepped Sri Meru lattice with orbit camera, Top-Down Chakra toggle, and live `13:17` Web Audio drone[cite: 2]. |
| `shaders/sri_meru_octonion_shader.glsl` | Standalone GLSL fragment shader source for the 8D octonion × 3D Sri Meru volumetric field[cite: 1]. |
| `src/mixtum_dsp.py` | Non-linear DSP synthesizer processing STFT matrices into `mixtum_output.wav`[cite: 5]. |
| `src/mahavidya_dsp_profiles.py` | Deterministic 10-voice STFT commutator audio synthesizer ($\Phi = [Z_H, Z_C]$) locked to `64 Hz`, `65.41 Hz` (C2), `196 Hz` (G3), `293.66 Hz` (D4), and `432 Hz` with pure-Python fallback[cite: 3, 4]. |
| `src/mahavidya_dsp_presets.json` | Machine-readable parameter matrix for all 10 deterministic STFT commutator profiles (*Kali* through *Kamala*)[cite: 3]. |
| `src/octonion_manifold_rotation.py` | 8D Fano plane non-associative signal trajectory map[cite: 5]. |
| `src/knot_invariants.py` | SymPy verification of Jones $V(t)$ and Alexander $\Delta(t)$ topological invariants[cite: 5]. |
| `src/prime_kamea_tetractys.py` | $4 \times 4$ Prime Brood Kamea magic square and Pythagorean Tetractys grid[cite: 5]. |
| `src/viscoelastic_vorticity_engine.py` | 2D fluid shear vorticity matrix $\omega = \nabla \times \mathbf{u}$ generating von Kármán eddies[cite: 5]. |
| `src/braid_group_b3.py` | 3D non-Abelian braid topography visualization for frequencies $65.41\text{ Hz}, 196\text{ Hz}, 293.66\text{ Hz}$[cite: 5]. |
| `src/chladni_3d_volumetric_clean.py` | 3D volumetric standing wave nodal isosurface acoustic chamber[cite: 5]. |
| `assets/*.wav` | Pre-rendered 16-bit PCM audio outputs generated by the Mixtum and 10-voice STFT commutator engines[cite: 4, 5]. |
| `AXIS_MUNDI_MERU.md` | Historical and structural-morphological reference mapping stepped *Meru* architecture and Sanskrit phonetic combinatorics onto octonion and DSP coordinates. |

---

## ⚡ Quickstart

```bash
# 1. Clone repository
git clone [https://github.com/HhWolfling/Magicicada-Chorus-Rise.git](https://github.com/HhWolfling/Magicicada-Chorus-Rise.git)
cd Magicicada-Chorus-Rise

# 2. Install core dependencies
pip install -r requirements.txt

# 3. Synthesize the base Mixtum audio relaxation pulse
python src/mixtum_dsp.py

# 4. Print the 10-voice STFT DSP profile matrix
python src/mahavidya_dsp_profiles.py

# 5. Synthesize a 16-bit PCM WAV file for a specific DSP profile (by index 1-10 or name)
python src/mahavidya_dsp_profiles.py "Tripura Sundari"
python src/mahavidya_dsp_profiles.py 1
