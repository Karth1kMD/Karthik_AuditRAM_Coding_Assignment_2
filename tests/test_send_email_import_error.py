# tests/test_send_email_import_error.py
import sys
import importlib
import email_agent

def test_send_email_returns_false_when_selenium_missing(monkeypatch):
    # Ensure selenium not present in sys.modules and imports will fail
    monkeypatch.setitem(sys.modules, "selenium", None)
    for name in list(sys.modules.keys()):
        if name.startswith("selenium."):
            monkeypatch.delitem(sys.modules, name, raising=False)

    ok = email_agent.send_email_browser("a", "p", "t", "s", "b")
    assert ok is False
