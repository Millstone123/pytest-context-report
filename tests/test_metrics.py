from pytest_context_report import SessionMetrics


def test_totals_and_slowest_phases():
    metrics = SessionMetrics()
    metrics.start()
    metrics.record_collection(3)
    metrics.record_phase("tests/test_metrics.py::test_b", 0.75)
    metrics.record_phase("tests/test_metrics.py::test_a", 1.25)
    metrics.record_outcome("passed")
    metrics.record_outcome("passed")
    metrics.record_outcome("skipped")

    assert metrics.started is True
    assert metrics.totals() == {"collected": 3, "passed": 2, "failed": 0, "skipped": 1}
    assert metrics.slowest(1) == [("tests/test_metrics.py::test_a", 1.25)]


def test_negative_durations_are_clamped():
    metrics = SessionMetrics()
    metrics.record_phase("tests/test_metrics.py::test_fast", -1)

    assert metrics.slowest() == [("tests/test_metrics.py::test_fast", 0.0)]
