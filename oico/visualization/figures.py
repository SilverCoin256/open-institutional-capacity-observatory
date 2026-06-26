from __future__ import annotations

from collections import Counter
from pathlib import Path

from oico.io import ROOT, read_csv, relative, sha256
from oico.models.authorization import intervention_scenarios


FIGURES = ROOT / "figures" / "gallery"


def _text(x: float, y: float, body: str, cls: str = "label", anchor: str = "start") -> str:
    escaped = (
        str(body)
        .replace("&", "&amp;")
        .replace("<", "&lt;")
        .replace(">", "&gt;")
        .replace('"', "&quot;")
    )
    return f'<text x="{x:.1f}" y="{y:.1f}" class="{cls}" text-anchor="{anchor}">{escaped}</text>'


def _svg(width: int, height: int, body: str) -> str:
    style = """
    <style>
      .title { font: 700 20px system-ui, -apple-system, Segoe UI, sans-serif; fill: #1f2933; }
      .subtitle { font: 13px system-ui, -apple-system, Segoe UI, sans-serif; fill: #52606d; }
      .axis { font: 12px system-ui, -apple-system, Segoe UI, sans-serif; fill: #52606d; }
      .label { font: 11px system-ui, -apple-system, Segoe UI, sans-serif; fill: #334e68; }
      .grid { stroke: #d9e2ec; stroke-width: 1; }
      .line { fill: none; stroke: #0f609b; stroke-width: 3; }
      .line2 { fill: none; stroke: #b83280; stroke-width: 3; }
      .bar { fill: #2f855a; }
      .bar2 { fill: #9f580a; }
      .point { fill: #0f609b; stroke: #fff; stroke-width: 2; }
    </style>
    """
    return f'<svg xmlns="http://www.w3.org/2000/svg" width="{width}" height="{height}" viewBox="0 0 {width} {height}">\n{style}\n{body}\n</svg>\n'


def _write(name: str, width: int, height: int, body: str) -> Path:
    FIGURES.mkdir(parents=True, exist_ok=True)
    path = FIGURES / name
    path.write_text(_svg(width, height, body), encoding="utf-8")
    return path


def _scale(value: float, minimum: float, maximum: float, low: float, high: float) -> float:
    if maximum == minimum:
        return (low + high) / 2
    return low + ((value - minimum) / (maximum - minimum)) * (high - low)


def line_chart(path_name: str, title: str, subtitle: str, rows: list[dict[str, str]], x_key: str, y_key: str) -> Path:
    values = [(row[x_key], float(row[y_key])) for row in rows if row.get(y_key) not in ("", None)]
    width, height = 760, 420
    left, right, top, bottom = 72, 36, 72, 70
    chart_w, chart_h = width - left - right, height - top - bottom
    ys = [value for _, value in values] + [0.0]
    y_min, y_max = min(ys), max(ys)
    parts = [_text(24, 32, title, "title"), _text(24, 52, subtitle, "subtitle")]
    for frac in [0, 0.25, 0.5, 0.75, 1]:
        y = top + chart_h * frac
        parts.append(f'<line x1="{left}" y1="{y:.1f}" x2="{left + chart_w}" y2="{y:.1f}" class="grid"/>')
    points = []
    for idx, (_, value) in enumerate(values):
        x = left + (chart_w * idx / max(1, len(values) - 1))
        y = _scale(value, y_min, y_max, top + chart_h, top)
        points.append((x, y, value))
    if points:
        coords = " ".join(f"{x:.1f},{y:.1f}" for x, y, _ in points)
        parts.append(f'<polyline points="{coords}" class="line"/>')
        for x, y, value in points:
            parts.append(f'<circle cx="{x:.1f}" cy="{y:.1f}" r="4.5" class="point"/>')
    zero_y = _scale(0.0, y_min, y_max, top + chart_h, top)
    parts.append(f'<line x1="{left}" y1="{zero_y:.1f}" x2="{left + chart_w}" y2="{zero_y:.1f}" stroke="#9aa5b1" stroke-dasharray="5 4"/>')
    parts.append(_text(24, top + chart_h / 2, y_key.upper(), "axis"))
    for idx, (label, _) in enumerate(values):
        if idx in (0, len(values) - 1) or idx % max(1, len(values) // 6) == 0:
            x = left + (chart_w * idx / max(1, len(values) - 1))
            parts.append(_text(x, height - 34, label, "axis", "middle"))
    return _write(path_name, width, height, "\n".join(parts))


def bar_chart(path_name: str, title: str, subtitle: str, items: list[tuple[str, float]], y_label: str) -> Path:
    width, height = 760, 430
    left, right, top, bottom = 82, 36, 78, 86
    chart_w, chart_h = width - left - right, height - top - bottom
    max_value = max([value for _, value in items] + [1])
    bar_w = chart_w / max(1, len(items)) * 0.7
    parts = [_text(24, 32, title, "title"), _text(24, 52, subtitle, "subtitle")]
    for frac in [0, 0.25, 0.5, 0.75, 1]:
        y = top + chart_h * frac
        parts.append(f'<line x1="{left}" y1="{y:.1f}" x2="{left + chart_w}" y2="{y:.1f}" class="grid"/>')
    for idx, (label, value) in enumerate(items):
        x = left + (idx + 0.15) * (chart_w / len(items))
        h = chart_h * value / max_value
        y = top + chart_h - h
        parts.append(f'<rect x="{x:.1f}" y="{y:.1f}" width="{bar_w:.1f}" height="{h:.1f}" class="bar"/>')
        parts.append(_text(x + bar_w / 2, height - 44, label, "axis", "middle"))
    parts.append(_text(24, top + chart_h / 2, y_label, "axis"))
    return _write(path_name, width, height, "\n".join(parts))


def make_all_figures() -> list[Path]:
    queue = read_csv(ROOT / "datasets" / "processed" / "queue_observations.csv")
    indicators = read_csv(ROOT / "datasets" / "processed" / "institutional_indicators.csv")
    asi = read_csv(ROOT / "datasets" / "processed" / "asi_scores.csv")
    paths = [
        line_chart(
            "qai_eoir.svg",
            "EOIR Queue Acceleration Index",
            "Backlog growth normalized by completions; descriptive signal, not causal proof.",
            [row for row in queue if row["institution_id"] == "eoir"],
            "period",
            "qai",
        ),
        line_chart(
            "qai_uscis.svg",
            "USCIS Queue Acceleration Index",
            "Quarterly snapshot using inherited public workload data.",
            [row for row in queue if row["institution_id"] == "uscis"],
            "period",
            "qai",
        ),
        line_chart(
            "cfpb_sedi.svg",
            "CFPB Rolling SEDI",
            "Complaint-volume pressure and outcome proxies summarized against local history.",
            [row for row in indicators if row["institution_id"] == "cfpb"],
            "period",
            "sedi",
        ),
        line_chart(
            "sec_review_intensity.svg",
            "SEC EDGAR Review Intensity",
            "Comment-letter output divided by 10-K review base.",
            [row for row in indicators if row["institution_id"] == "sec"],
            "period",
            "review_intensity",
        ),
    ]
    distribution = Counter(int(row["total_asi_score"]) for row in asi)
    paths.append(
        bar_chart(
            "asi_score_distribution.svg",
            "ASI Score Distribution",
            "Document-level accountability specificity; not operational accountability.",
            [(str(score), count) for score, count in sorted(distribution.items())],
            "documents",
        )
    )
    scenarios = intervention_scenarios()
    paths.append(
        bar_chart(
            "authorization_quality_scenarios.svg",
            "Authorization Saturation Scenarios",
            "Illustrative model outputs for benchmark and teaching use.",
            [(row["scenario"], float(row["quality"])) for row in scenarios],
            "quality",
        )
    )
    write_figure_manifest(paths)
    return paths


def write_figure_manifest(paths: list[Path]) -> None:
    lines = [
        "# Figure Manifest",
        "",
        "All figures are generated as deterministic SVG files by `oico make-figures`.",
        "They are intended for inspection, teaching, and paper drafts; statistical claims should cite the processed data and metric documentation.",
        "",
        "| figure | sha256 | purpose |",
        "|---|---|---|",
    ]
    purposes = {
        "qai_eoir.svg": "EOIR queue pressure over fiscal years.",
        "qai_uscis.svg": "USCIS queue pressure over fiscal quarters.",
        "cfpb_sedi.svg": "CFPB degradation-index signal over monthly complaint data.",
        "sec_review_intensity.svg": "SEC comment-letter intensity over yearly EDGAR counts.",
        "asi_score_distribution.svg": "Distribution of accountability specificity scores.",
        "authorization_quality_scenarios.svg": "Illustrative authorization-saturation intervention outputs.",
    }
    for path in paths:
        lines.append(f"| `{relative(path)}` | `{sha256(path)}` | {purposes.get(path.name, '')} |")
    FIGURES.joinpath("FIGURE_MANIFEST.md").write_text("\n".join(lines) + "\n", encoding="utf-8")
