from .qai import queue_acceleration_index

__all__ = ["queue_acceleration_index", "sedi_from_indicators", "score_document"]


def __getattr__(name: str):
    if name == "sedi_from_indicators":
        from .sedi import sedi_from_indicators

        return sedi_from_indicators
    if name == "score_document":
        from .asi import score_document

        return score_document
    raise AttributeError(f"module {__name__!r} has no attribute {name!r}")
