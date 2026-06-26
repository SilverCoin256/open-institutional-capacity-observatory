from __future__ import annotations

from oico.io import ROOT, read_csv


def main() -> None:
    institutions = read_csv(ROOT / "datasets" / "processed" / "institutions.csv")
    queue = read_csv(ROOT / "datasets" / "processed" / "queue_observations.csv")
    print(f"{len(institutions)} institutions")
    print(f"{len(queue)} queue observations")


if __name__ == "__main__":
    main()
