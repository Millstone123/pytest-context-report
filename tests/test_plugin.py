from pytest_context_report.plugin import ContextReportPlugin


def test_plugin_starts_only_when_configured():
    plugin = ContextReportPlugin()
    assert plugin.metrics.started is False

    class Config:
        pass

    plugin.pytest_configure(Config())
    assert plugin.metrics.started is True
