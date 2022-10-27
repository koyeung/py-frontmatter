from .conftest import run_console_script


def test_get(sample, capsys):
    exit_code = run_console_script("frontmatter", "get", str(sample))
    assert exit_code == 0

    captured = capsys.readouterr()
    assert (
        captured.out
        == """\
{"title": "Hacker's note", "tags": ["a", "b"]}
"""
    )


def test_get__shell_quote(sample, capsys):
    exit_code = run_console_script("frontmatter", "get", "--sq", str(sample))
    assert exit_code == 0

    captured = capsys.readouterr()
    assert (
        captured.out
        == """\
'{"title": "Hacker'"'"'s note", "tags": ["a", "b"]}'
"""
    )
