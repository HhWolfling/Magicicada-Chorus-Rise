#!/usr/bin/env python3
"""
mahavidya_dsp_profiles.py
Deterministic STFT / DSP Commutator Modulation Profiles (Phi = [H, C])
for the 10 Mahavidya Bija Vectors, locked to 65.41 Hz (C2), 196.00 Hz (G3),
293.66 Hz (D4), and 432.00 Hz.

Integrates directly with Magicicada-Chorus-Rise / mixtum_dsp.py.
[WE_WOZ_HERE]99
"""

from dataclasses import asdict, dataclass
import json
import math
import struct
import sys
from typing import Dict, List, Optional
import wave


@dataclass(frozen=True)
class MahavidyaDSPProfile:
    index: int
    name: str
    lineage: str
    bija: str
    prime_mass: int
    mod29_residue: int
    carrier_h_hz: float      # Kinetic Spark (H) primary frequency
    carrier_c_hz: float      # Structural Ground (C) anchor frequency
    pilot_sync_hz: float     # 64 Hz or 432 Hz reference lock
    mod_p: int               # Prime phase multiplier p (H channel)
    mod_q: int               # Prime phase multiplier q (C channel)
    gamma: float             # Spectral commutator compression exponent
    fm_index: float          # Cross-phase FM modulation depth
    dsp_role: str            # Acoustic function in Mixtum engine


# ---------------------------------------------------------------------------
# 10 MAHAVIDYA DETERMINISTIC DSP PROFILES
# Derived from Matrika-50 Prime Masses & Mod-29 Residues
# ---------------------------------------------------------------------------
MAHAVIDYA_DSP_PROFILES: List[MahavidyaDSPProfile] = [
    MahavidyaDSPProfile(
        index=1,
        name="Kali",
        lineage="Kalikula",
        bija="Krim",
        prime_mass=156,
        mod29_residue=4,
        carrier_h_hz=293.66,
        carrier_c_hz=65.41,
        pilot_sync_hz=64.00,
        mod_p=13,
        mod_q=17,
        gamma=0.85,
        fm_index=0.65,
        dsp_role="Sub-octave time-reversal transient slicer (C2 bedrock)",
    ),
    MahavidyaDSPProfile(
        index=2,
        name="Tara",
        lineage="Kalikula",
        bija="Hum",
        prime_mass=129,
        mod29_residue=5,
        carrier_h_hz=432.00,
        carrier_c_hz=65.41,
        pilot_sync_hz=432.00,
        mod_p=17,
        mod_q=13,
        gamma=0.92,
        fm_index=0.45,
        dsp_role="432 Hz breath-harmonic carrier & upper overtone bridge",
    ),
    MahavidyaDSPProfile(
        index=3,
        name="Tripura Sundari",
        lineage="Shrikula",
        bija="Srim",
        prime_mass=156,
        mod29_residue=4,
        carrier_h_hz=293.66,
        carrier_c_hz=196.00,
        pilot_sync_hz=432.00,
        mod_p=8,
        mod_q=9,
        gamma=1.00,
        fm_index=0.38,
        dsp_role="(8,9) Sri Chakra golden-ratio phase-lock & Bindu focus",
    ),
    MahavidyaDSPProfile(
        index=4,
        name="Bhuvaneshvari",
        lineage="Shrikula",
        bija="Hrim",
        prime_mass=168,
        mod29_residue=8,
        carrier_h_hz=196.00,
        carrier_c_hz=65.41,
        pilot_sync_hz=64.00,
        mod_p=13,
        mod_q=8,
        gamma=0.95,
        fm_index=0.30,
        dsp_role="Wide-aperture Akasha stereo spatializer (G3/C2 fifth)",
    ),
    MahavidyaDSPProfile(
        index=5,
        name="Bhairavi",
        lineage="Kalikula",
        bija="Hsraim",
        prime_mass=265,
        mod29_residue=17,
        carrier_h_hz=293.66,
        carrier_c_hz=65.41,
        pilot_sync_hz=64.00,
        mod_p=17,
        mod_q=19,
        gamma=0.78,
        fm_index=0.85,
        dsp_role="High-heat Tapas sideband saturation (max prime mass 265)",
    ),
    MahavidyaDSPProfile(
        index=6,
        name="Chhinnamasta",
        lineage="Kalikula",
        bija="Hum",
        prime_mass=129,
        mod29_residue=5,
        carrier_h_hz=293.66,
        carrier_c_hz=196.00,
        pilot_sync_hz=64.00,
        mod_p=13,
        mod_q=29,
        gamma=0.80,
        fm_index=0.72,
        dsp_role="Zero-crossing polarity inverter & Sushumna notch gate",
    ),
    MahavidyaDSPProfile(
        index=7,
        name="Dhumavati",
        lineage="Kalikula",
        bija="Dhum",
        prime_mass=73,
        mod29_residue=13,
        carrier_h_hz=196.00,
        carrier_c_hz=65.41,
        pilot_sync_hz=64.00,
        mod_p=13,
        mod_q=14,
        gamma=1.10,
        fm_index=0.22,
        dsp_role="Axis-14 adjacent spectral ash filter (Mod-29 residue 13)",
    ),
    MahavidyaDSPProfile(
        index=8,
        name="Bagalamukhi",
        lineage="Kalikula",
        bija="Hlim",
        prime_mass=172,
        mod29_residue=19,
        carrier_h_hz=196.00,
        carrier_c_hz=65.41,
        pilot_sync_hz=432.00,
        mod_p=19,
        mod_q=13,
        gamma=1.05,
        fm_index=0.15,
        dsp_role="Stambhana phase-freeze & low-drift standing wave lock",
    ),
    MahavidyaDSPProfile(
        index=9,
        name="Matangi",
        lineage="Shrikula",
        bija="Aim",
        prime_mass=84,
        mod29_residue=11,
        carrier_h_hz=432.00,
        carrier_c_hz=293.66,
        pilot_sync_hz=432.00,
        mod_p=11,
        mod_q=13,
        gamma=0.90,
        fm_index=0.52,
        dsp_role="Vak vocal-formant resonant comb & harmonic micro-grid",
    ),
    MahavidyaDSPProfile(
        index=10,
        name="Kamala",
        lineage="Shrikula",
        bija="Srim",
        prime_mass=156,
        mod29_residue=4,
        carrier_h_hz=432.00,
        carrier_c_hz=196.00,
        pilot_sync_hz=432.00,
        mod_p=9,
        mod_q=8,
        gamma=0.98,
        fm_index=0.35,
        dsp_role="Full-spectrum lotus harmonic bloom & C2-G3-D4 triad",
    ),
]


def get_profile(selector: str) -> Optional[MahavidyaDSPProfile]:
    """Finds a Mahavidya profile by 1-based index or case-insensitive name."""
    key = selector.strip().lower()
    for prof in MAHAVIDYA_DSP_PROFILES:
        if key == str(prof.index) or key in prof.name.lower():
            return prof
    return None


def export_presets_json(filepath: str = "mahavidya_dsp_presets.json") -> None:
    """Writes all 10 Mahavidya DSP profiles to a clean JSON file."""
    payload = {
        "engine": "Magicicada-Chorus-Rise // Mixtum STFT Commutator",
        "equation": "Phi = [Z_H, Z_C] = Z_H * conj(Z_C) - Z_C * conj(Z_H)",
        "anchor_frequencies_hz": [64.0, 65.41, 196.0, 293.66, 432.0],
        "profiles": [asdict(p) for p in MAHAVIDYA_DSP_PROFILES],
    }
    with open(filepath, "w", encoding="utf-8") as f:
        json.dump(payload, f, indent=2)
    print(f"[+] Exported 10 Mahavidya DSP presets to '{filepath}'")


def synthesize_mahavidya_wav(
    profile: MahavidyaDSPProfile,
    duration: float = 4.0,
    sample_rate: int = 44100,
    output_wav: Optional[str] = None,
) -> str:
    """
    Synthesizes a playable 16-bit PCM WAV track using the profile's
    STFT commutator bracket Phi = [H, C] (via numpy/scipy if installed,
    or a deterministic pure-Python commutator oscillator fallback).
    """
    if output_wav is None:
        safe_name = profile.name.lower().replace(" ", "_")
        output_wav = f"mixtum_{safe_name}.wav"

    try:
        import numpy as np
        import scipy.signal as signal

        t = np.linspace(0.0, duration, int(sample_rate * duration), endpoint=False)

        # Signal H (Kinetic Spark)
        sig_h = (
            0.60 * np.sin(2.0 * np.pi * profile.carrier_h_hz * t
                          + profile.fm_index * np.cos(2.0 * np.pi * profile.mod_p * t))
            + 0.35 * np.sin(2.0 * np.pi * profile.pilot_sync_hz * t)
        )

        # Signal C (Structural Ground)
        sig_c = (
            0.80 * np.sin(2.0 * np.pi * profile.carrier_c_hz * t)
            + 0.30 * np.sin(2.0 * np.pi * (profile.carrier_c_hz * 0.5) * t
                          + np.sin(2.0 * np.pi * profile.mod_q * t))
        )

        # STFT Commutator Coupling: Phi = [Z_H, Z_C]
        nperseg = 1024
        _, _, z_h = signal.stft(sig_h, fs=sample_rate, nperseg=nperseg)
        _, _, z_c = signal.stft(sig_c, fs=sample_rate, nperseg=nperseg)

        z_phi = (z_h * np.conj(z_c)) - (z_c * np.conj(z_h))
        phase_lock = np.exp(
            1j * (np.angle(z_h) * profile.mod_p - np.angle(z_c) * profile.mod_q)
        )
        z_mixtum = (np.abs(z_phi) ** profile.gamma) * phase_lock

        _, audio = signal.istft(z_mixtum, fs=sample_rate, nperseg=nperseg)
        peak = float(np.max(np.abs(audio))) or 1.0
        audio = audio / peak

        with wave.open(output_wav, "wb") as wf:
            wf.setnchannels(1)
            wf.setsampwidth(2)
            wf.setframerate(sample_rate)
            pcm = (audio * 32767.0).astype(np.int16)
            wf.writeframes(pcm.tobytes())

        print(f"[+] Synthesized STFT Commutator WAV: '{output_wav}' (scipy/numpy engine)")
        return output_wav

    except ImportError:
        # Pure-Python fallback for environments without numpy/scipy
        num_samples = int(sample_rate * duration)
        with wave.open(output_wav, "wb") as wf:
            wf.setnchannels(1)
            wf.setsampwidth(2)
            wf.setframerate(sample_rate)
            frames = bytearray()
            for n in range(num_samples):
                t = n / float(sample_rate)
                h = math.sin(
                    2.0 * math.pi * profile.carrier_h_hz * t
                    + profile.fm_index * math.cos(2.0 * math.pi * profile.mod_p * t)
                )
                c = math.sin(2.0 * math.pi * profile.carrier_c_hz * t)
                # Time-domain non-commutative phase cross-term
                phi = (h * math.cos(2.0 * math.pi * profile.mod_q * t)) - (
                    c * math.cos(2.0 * math.pi * profile.mod_p * t)
                )
                sample_val = max(-1.0, min(1.0, 0.85 * phi))
                frames.extend(struct.pack("<h", int(sample_val * 32767.0)))
            wf.writeframes(bytes(frames))

        print(f"[+] Synthesized Pure-Python Commutator WAV: '{output_wav}'")
        return output_wav


def print_profile_matrix() -> None:
    print("=" * 84)
    print("  10 MAHAVIDYA STFT / DSP COMMUTATOR PROFILES (Phi = [Z_H, Z_C])")
    print("  Harmonic Anchors: 64 Hz | 65.41 Hz (C2) | 196.00 Hz (G3) | 293.66 Hz (D4) | 432 Hz")
    print("=" * 84)
    for p in MAHAVIDYA_DSP_PROFILES:
        print(
            f"  [{p.index:>2}] {p.name:<16} ({p.bija:<6}) | "
            f"H:{p.carrier_h_hz:>6.2f}Hz  C:{p.carrier_c_hz:>6.2f}Hz  Pilot:{p.pilot_sync_hz:>6.2f}Hz | "
            f"(p,q)=({p.mod_p:>2},{p.mod_q:>2}) | gamma={p.gamma:.2f}"
        )
        print(f"       Role: {p.dsp_role}")
    print("-" * 84)


if __name__ == "__main__":
    print_profile_matrix()
    export_presets_json()
    if len(sys.argv) > 1:
        target = " ".join(sys.argv[1:])
        selected = get_profile(target)
        if selected:
            print(f"\n[>] Engaging DSP Profile [{selected.index}] {selected.name} ({selected.bija})...")
            synthesize_mahavidya_wav(selected)
        else:
            print(f"[!] Profile '{target}' not found. Pass an index (1-10) or Mahavidya name.")