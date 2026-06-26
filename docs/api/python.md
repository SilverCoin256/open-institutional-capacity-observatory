# Python API

The v1 package is dependency-light and organized around inspectable modules.

## Metrics

```python
from oico.metrics.qai import queue_acceleration_index

qai = queue_acceleration_index(
    pending_t=1108300,
    pending_previous=975977,
    completions_t=195145,
)
```

```python
from oico.metrics.asi import score_document
```

```python
from oico.metrics.sedi import sedi_from_indicators, rolling_sedi
```

## Models

```python
from oico.models.authorization import authorization_quality, intervention_scenarios
from oico.models.procedural_capacity import procedural_failure_risk
```

## Data Build

```python
from oico.datasets import build_all

report = build_all()
```

## Benchmarks

```python
from oico.benchmarks import run_all_benchmarks

results = run_all_benchmarks()
```
