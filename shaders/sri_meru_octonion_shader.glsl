// sri_meru_octonion_shader.glsl
// 8D Octonionic Fano Field x 3D Sri Meru (Sri Chakra) Stepped Elevation
// Coupled to (p=13, q=17) Prime Brood Torus & Commutator Pulse Phi = [H, C]
// [WE_WOZ_HERE]99

#ifdef GL_ES
precision highp float;
#endif

uniform vec2 u_resolution;
uniform float u_time;
uniform float u_p;      // Default: 13.0 (Magicicada tredecim)
uniform float u_q;      // Default: 17.0 (Magicicada septendecim)
uniform float u_tau;    // Phase-lock coupling tension (0.0 .. 1.0)

const float PI = 3.14159265359;
const float TAU = 6.28318530718;

// 2D rotation helper
mat2 rot2D(float a) {
    float s = sin(a);
    float c = cos(a);
    return mat2(c, -s, s, c);
}

// Signed distance to a 2D equilateral triangle (Shiva upward / Shakti downward)
float sdEquilateralTriangle(vec2 p, float r) {
    const float k = sqrt(3.0);
    p.x = abs(p.x) - r;
    p.y = p.y + r / k;
    if (p.x + k * p.y > 0.0) {
        p = vec2(p.x - k * p.y, -k * p.x - p.y) / 2.0;
    }
    p.x -= clamp(p.x, -2.0 * r, 0.0);
    return -length(p) * sign(p.y);
}

// Signed distance to outer square earth-gate (Bhupura)
float sdBox2D(vec2 p, vec2 b) {
    vec2 d = abs(p) - b;
    return length(max(d, 0.0)) + min(max(d.x, d.y), 0.0);
}

// Evaluate 8D Octonion Field + 3D Sri Meru Stepped Elevation
// Returns vec4(distance_estimate, shiva_energy, shakti_energy, bindu_glow)
vec4 sriMeruOctonionField(vec3 pos) {
    float pFreq = (u_p > 0.0) ? u_p : 13.0;
    float qFreq = (u_q > 0.0) ? u_q : 17.0;
    float coupling = (u_tau > 0.0) ? u_tau : 0.65;

    // Non-commutative commutator cardiac pulse: Phi = [H, C]
    float H = sin(u_time * 1.618 + pFreq * 0.13);
    float C = cos(u_time * 1.000 + qFreq * 0.17);
    float commutatorPhi = H * C - C * H;

    // Tilt Sri Meru slightly so both top-down Sri Chakra and 3D pyramid elevation read cleanly
    vec3 p = pos;
    p.yz *= rot2D(0.42 + 0.12 * sin(u_time * 0.25));
    p.xz *= rot2D(u_time * 0.18 + commutatorPhi * 0.25);

    float radial = length(p.xz);
    float angle = atan(p.z, p.x);

    // -----------------------------------------------------------------------
    // 1. MAP 3D COORDINATES TO 8D OCTONION VECTOR O = x0 + sum(x_i * e_i)
    // -----------------------------------------------------------------------
    // x0 (Real Scalar): Central Bindu / Apex singularity
    float x0 = length(p - vec3(0.0, 0.78, 0.0)) - 0.06;

    // e1..e7 (7 Imaginary Units): 7 Inner Circuits of Sri Meru
    float x1 = sdBox2D(p.xz, vec2(1.35)) * cos(u_time * 0.3);                 // Circuit 1: Bhupura
    float x2 = (radial - 1.12 + 0.04 * cos(16.0 * angle + u_time)) * 0.8;    // Circuit 2: 16-petal lotus
    float x3 = (radial - 0.94 + 0.04 * sin(8.0 * angle - u_time)) * 0.8;     // Circuit 3: 8-petal lotus
    float x4 = sdEquilateralTriangle(p.xz, 0.78);                            // Circuit 4: 14-triangle outer
    float x5 = sdEquilateralTriangle(vec2(p.x, -p.z), 0.62);                 // Circuit 5: 10-triangle outer
    float x6 = sdEquilateralTriangle(p.xz * rot2D(PI / 6.0), 0.46);          // Circuit 6: 10-triangle inner
    float x7 = sdEquilateralTriangle(vec2(p.x, -p.z) * rot2D(-PI / 6.0), 0.30); // Circuit 7: 8-triangle Vagdevatas

    // -----------------------------------------------------------------------
    // 2. NON-ASSOCIATIVE FANO PLANE TRIAD COUPLING
    // Triads: (1,2,3), (1,4,5), (1,7,6), (2,4,6), (2,5,7), (3,4,7), (3,6,5)
    // -----------------------------------------------------------------------
    float fano1 = (x1 * x2 - x3) + (x1 * x4 - x5);
    float fano2 = (x1 * x7 - x6) + (x2 * x4 - x6);
    float fano3 = (x2 * x5 - x7) + (x3 * x4 - x7);
    float fano4 = (x3 * x6 - x5);
    float fanoAssociator = (fano1 + fano2 + fano3 + fano4) * 0.08 * coupling;

    // -----------------------------------------------------------------------
    // 3. INTERLOCKING SHIVA (4 UPWARD) & SHAKTI (5 DOWNWARD) MERU TERRACES
    // -----------------------------------------------------------------------
    // 4 Upward Shiva Layers (Electric Cyan)
    float shivaField = 1e5;
    for (int i = 0; i < 4; i++) {
        float fi = float(i);
        float scale = 0.82 - fi * 0.16;
        float elev = 0.12 + fi * 0.16;
        vec2 q2 = p.xz * rot2D(fi * 0.08 + u_time * 0.05 * (fi + 1.0));
        float triUp = abs(sdEquilateralTriangle(q2, scale)) - 0.012;
        float slab = max(triUp, abs(p.y - elev) - 0.018);
        shivaField = min(shivaField, slab);
    }

    // 5 Downward Shakti Layers (Neon Magenta)
    float shaktiField = 1e5;
    for (int j = 0; j < 5; j++) {
        float fj = float(j);
        float scale = 0.88 - fj * 0.145;
        float elev = 0.06 + fj * 0.155;
        vec2 q2 = vec2(p.x, -p.z) * rot2D(-fj * 0.07 - u_time * 0.06 * (fj + 1.0));
        float triDown = abs(sdEquilateralTriangle(q2, scale)) - 0.012;
        float slab = max(triDown, abs(p.y - elev) - 0.018);
        shaktiField = min(shaktiField, slab);
    }

    // Outer Bhupura Earth-Gate base at y = 0.0
    float bhupuraRing = max(abs(sdBox2D(p.xz, vec2(1.25))) - 0.015, abs(p.y) - 0.015);
    float meruStructure = min(min(shivaField, shaktiField), min(bhupuraRing, x0));

    // Perturb surface gently with 8D Fano associator torsion and (13,17) torus wave
    float torusHarmonic = 0.012 * sin(pFreq * angle + qFreq * radial - u_time * 2.0);
    float d = meruStructure + torusHarmonic + fanoAssociator * 0.05;

    // Channel weights for color synthesis
    float shivaGlow = exp(-18.0 * max(shivaField, 0.0));
    float shaktiGlow = exp(-18.0 * max(shaktiField, 0.0));
    float binduGlow = exp(-28.0 * max(x0, 0.0));

    return vec4(d, shivaGlow, shaktiGlow, binduGlow);
}

void main() {
    vec2 uv = (gl_FragCoord.xy - 0.5 * u_resolution.xy) / u_resolution.y;

    // Camera setup looking at the 3D Sri Meru apex
    vec3 ro = vec3(0.0, 1.35, 2.75);
    vec3 target = vec3(0.0, 0.35, 0.0);
    vec3 fwd = normalize(target - ro);
    vec3 right = normalize(cross(fwd, vec3(0.0, 1.0, 0.0)));
    vec3 up = cross(right, fwd);
    vec3 rd = normalize(fwd + uv.x * right + uv.y * up);

    // Volumetric raymarching across the 8D x 3D manifold
    float t = 0.0;
    vec3 accumColor = vec3(0.0);

    // Cyber-Esoteric Palette: Pitch-Black Void, Electric Cyan, Neon Magenta, Radiant Gold
    vec3 colVoid    = vec3(0.0196, 0.0196, 0.0392); // #05050A
    vec3 colCyan    = vec3(0.0, 1.0, 0.8);          // #00FFCC (Shiva Prakasha)
    vec3 colMagenta = vec3(1.0, 0.0, 0.498);        // #FF007F (Shakti Vimarsha)
    vec3 colGold    = vec3(1.0, 0.843, 0.0);        // #FFD700 (Bindu Singularity)

    for (int i = 0; i < 72; i++) {
        vec3 pos = ro + rd * t;
        vec4 field = sriMeruOctonionField(pos);
        float d = field.x;

        // Accumulate volumetric emission from Shiva, Shakti, and Bindu layers
        float stepGlow = 0.028 / (1.0 + 35.0 * abs(d));
        accumColor += colCyan    * field.y * stepGlow * 1.15;
        accumColor += colMagenta * field.z * stepGlow * 1.15;
        accumColor += colGold    * field.w * stepGlow * 1.85;

        t += max(abs(d) * 0.45, 0.018);
        if (t > 6.5) break;
    }

    // Subtle radial vignette around pitch-black background
    float vignette = 1.0 - 0.35 * dot(uv, uv);
    vec3 finalColor = colVoid + accumColor * vignette;

    // Tone-map highlights cleanly without clipping gold/cyan intersections
    finalColor = finalColor / (1.0 + 0.35 * finalColor);

    gl_FragColor = vec4(finalColor, 1.0);
}
