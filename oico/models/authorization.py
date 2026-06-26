from __future__ import annotations

import math


def erlang_c(arrival_rate: float, service_rate: float, servers: int) -> float:
    if not isinstance(servers, int) or servers <= 0:
        raise ValueError("servers must be a positive integer")
    if not all(math.isfinite(value) for value in (arrival_rate, service_rate)):
        raise ValueError("arrival_rate and service_rate must be finite")
    if arrival_rate < 0 or service_rate <= 0:
        raise ValueError("arrival_rate must be non-negative and service_rate must be positive")
    rho = arrival_rate / (servers * service_rate)
    if rho >= 1:
        return 1.0
    a = arrival_rate / service_rate
    denom = sum((a**n) / math.factorial(n) for n in range(servers))
    tail = (a**servers) / (math.factorial(servers) * (1 - rho))
    return tail / (denom + tail)


def ceremonial_fraction(rho_s: float, k: float, sharpness: float = 12.0) -> float:
    if not all(math.isfinite(value) for value in (rho_s, k, sharpness)):
        raise ValueError("authorization parameters must be finite")
    if rho_s < 0:
        raise ValueError("rho_s must be non-negative")
    if k < 0:
        raise ValueError("k must be non-negative")
    if sharpness <= 0:
        raise ValueError("sharpness must be positive")
    threshold = k / (1 + k) if k != 0 else 0.0
    scaled = sharpness * (rho_s - threshold)
    if scaled >= 0:
        return 1.0 / (1.0 + math.exp(-scaled))
    exp_scaled = math.exp(scaled)
    return exp_scaled / (1.0 + exp_scaled)


def authorization_quality(rho_s: float, k: float = 1.0, q_substantive: float = 1.0, q_ceremonial: float = 0.25) -> float:
    if not all(math.isfinite(value) for value in (q_substantive, q_ceremonial)):
        raise ValueError("quality parameters must be finite")
    if not 0 <= q_substantive <= 1 or not 0 <= q_ceremonial <= 1:
        raise ValueError("quality parameters must be in [0, 1]")
    frac = ceremonial_fraction(rho_s, k)
    return q_substantive * (1 - frac) + q_ceremonial * frac


def intervention_scenarios(base_rho: float = 0.7, k: float = 1.0) -> list[dict[str, float | str]]:
    scenarios = [
        ("baseline", base_rho, k, 0.25),
        ("double_capacity", base_rho / 2, k, 0.25),
        ("halve_throughput", base_rho * 2, k, 0.25),
        ("raise_tolerance", base_rho, k * 2, 0.25),
        ("quality_floor", base_rho, k, 0.50),
    ]
    return [
        {
            "scenario": name,
            "rho_s": rho,
            "k": scenario_k,
            "q_ceremonial": q_c,
            "quality": authorization_quality(rho, scenario_k, q_ceremonial=q_c),
        }
        for name, rho, scenario_k, q_c in scenarios
    ]


MODEL_DOCUMENTATION = {
    "definition": "Authorization saturation models a transition from substantive to ceremonial review as utilization crosses a tolerance threshold.",
    "mathematical_intuition": "The threshold rho*=k/(1+k) controls the point where ceremonial review becomes likely; quality is a mixture of substantive and ceremonial modes.",
    "assumptions": ["Review tasks are comparable enough to aggregate.", "A single tolerance parameter is a useful abstraction.", "Ceremonial review is faster but lower quality."],
    "limitations": ["Not calibrated to any institution by default.", "Does not model strategic behavior or legal mandates.", "Quality values are illustrative unless empirically measured."],
    "failure_modes": ["Users may mistake simulated intervention effects for policy estimates.", "Extreme rho values can hide heterogeneity across reviewers."],
    "expected_misuse": "Claiming a real agency will improve by a specific amount without calibration.",
}
