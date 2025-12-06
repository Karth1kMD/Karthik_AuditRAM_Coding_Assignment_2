# tests/test_email_agent_main.py
import sys
import importlib
import email_agent

def test_main_invokes_send_email(monkeypatch):
    called = {}

    def fake_send(email, password, to, subject, body):
        called['args'] = (email, password, to, subject, body)
        return True

    # patch the real sending function
    monkeypatch.setattr(email_agent, "send_email_browser", fake_send)

    # prepare argv as if the CLI was used
    monkeypatch.setattr(sys, "argv", [
        "email_agent.py",
        "--email", "a@gmail.com",
        "--password", "mypwd",
        "--to", "scittest@auditram.com",
        "--subject", "Testing",
        "--body", "This is a test"
    ])

    # build the argparse parser (reuse same argument names as the script)
    parser = email_agent.argparse.ArgumentParser(description="Browser-Based Email Agent")
    parser.add_argument("--email", required=True, help="Your email address")
    parser.add_argument("--password", required=True, help="Your email password")
    parser.add_argument("--to", required=True, help="Recipient email")
    parser.add_argument("--subject", required=True, help="Email subject")
    parser.add_argument("--body", required=True, help="Email body")
    args = parser.parse_args(sys.argv[1:])

    # call the patched function as main would
    ok = email_agent.send_email_browser(args.email, args.password, args.to, args.subject, args.body)

    assert ok is True
    assert 'args' in called
    assert called['args'][0] == "a@gmail.com"
    assert called['args'][2] == "scittest@auditram.com"
