from axgridtools import __version__

from axgridtools.path import Path


def test_version():
    assert __version__ == '0.1.0'


def test_fs_path():
    p = Path(ct_root="/ctx/", fs_root="/tmp/fs/ctx/")
    assert p.get(fs_target="../../tk/a.txt").fs == "/tmp/tk/a.txt"
    assert p.get(fs_target="./tk/a.txt").fs == "/tmp/fs/ctx/tk/a.txt"
    assert p.get(fs_target="/tk/a.txt").fs == "/tk/a.txt"

    assert p.get(ct_target="../tk/a.txt").fs == "/tmp/fs/tk/a.txt"
    assert p.get(ct_target="./tk/a.txt").fs == "/tmp/fs/ctx/tk/a.txt"
    assert p.get(ct_target="/tk/a.txt").fs == "/tmp/fs/tk/a.txt"


def test_ct_path():
    p = Path(ct_root="/ctx/", fs_root="/tmp/fs/ctx/")
    assert p.get(ct_target="../tk/a.txt").ct == "/tk/a.txt"
    assert p.get(ct_target="./tk/a.txt").ct == "/ctx/tk/a.txt"
    assert p.get(ct_target="/tk/a.txt").ct == "/tk/a.txt"

    assert p.get(fs_target="../tk/a.txt").ct == "/tk/a.txt"
    assert p.get(fs_target="./tk/a.txt").ct == "/ctx/tk/a.txt"
    assert p.get(fs_target="../a.txt").ct == "/a.txt"
    assert p.get(fs_target="/tmp/fs/a.txt").ct == "/a.txt"


def test_rel_fs_path():
    p = Path(ct_root="/ctx/", fs_root="/tmp/fs/ctx/")
    assert p.get(fs_target="../../tk/a.txt").fs_rel == "../../tk/a.txt"
    assert p.get(fs_target="/tk/a.txt").fs_rel == "../../../tk/a.txt"
    assert p.get(fs_target="/tmp/fs/a.txt").fs_rel == "../a.txt"

    assert p.get(ct_target="/tk/a.txt").fs_rel == "../tk/a.txt"
    assert p.get(ct_target="../tk/a.txt").fs_rel == "../tk/a.txt"
    assert p.get(ct_target="/ctx/kt/a.txt").fs_rel == "kt/a.txt"


def test_rel_ct_path():
    p = Path(ct_root="/ctx/", fs_root="/tmp/fs/ctx/")
    assert p.get(fs_target="../tk/a.txt").ct_rel == "../tk/a.txt"
    assert p.get(fs_target="/tmp/fs/ctx/a.txt").ct_rel == "a.txt"
    assert p.get(fs_target="/tmp/fs/ctx/kt/a.txt").ct_rel == "kt/a.txt"

    assert p.get(ct_target="./a.txt").fs_rel == "a.txt"
    assert p.get(ct_target="../a.txt").fs_rel == "../a.txt"
    assert p.get(ct_target="/ctx/kt/a.txt").fs_rel == "kt/a.txt"
