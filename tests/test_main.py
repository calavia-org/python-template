from template.cli import main


def test_main(capsys):
    assert main(['--name', 'test']) == 0
    out, err = capsys.readouterr()
    # test is a user which does not have any contributions since 2010.
    # Hopefully this will not change in the future and the test will not break.
    assert out == 'Hello test!\nYou have 5 repos.\n'
    assert err == ''


def test_main_empty_name(capsys):
    assert main(['--name', '']) == 1
    out, err = capsys.readouterr()
    assert out == 'Username cannot be empty\n'
    assert err == ''
