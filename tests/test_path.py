from axgridcommons.path import Path


def test_fs_path():
    p = Path(ct_root="/ctx/", fs_root="/tmp/fs/ctx/")
    assert p.item(fs_target="../../tk/a.txt").fs == "/tmp/tk/a.txt"
    assert p.item(fs_target="./tk/a.txt").fs == "/tmp/fs/ctx/tk/a.txt"
    assert p.item(fs_target="/tk/a.txt").fs == "/tk/a.txt"

    assert p.item(ct_target="../tk/a.txt").fs == "/tmp/fs/tk/a.txt"
    assert p.item(ct_target="./tk/a.txt").fs == "/tmp/fs/ctx/tk/a.txt"
    assert p.item(ct_target="/tk/a.txt").fs == "/tmp/fs/tk/a.txt"


def test_ct_path():
    p = Path(ct_root="/ctx/", fs_root="/tmp/fs/ctx/")
    assert p.item(ct_target="../tk/a.txt").ct == "/tk/a.txt"
    assert p.item(ct_target="./tk/a.txt").ct == "/ctx/tk/a.txt"
    assert p.item(ct_target="/tk/a.txt").ct == "/tk/a.txt"

    assert p.item(fs_target="../tk/a.txt").ct == "/tk/a.txt"
    assert p.item(fs_target="./tk/a.txt").ct == "/ctx/tk/a.txt"
    assert p.item(fs_target="../a.txt").ct == "/a.txt"
    assert p.item(fs_target="/tmp/fs/a.txt").ct == "/a.txt"


def test_rel_fs_path():
    p = Path(ct_root="/ctx/", fs_root="/tmp/fs/ctx/")
    assert p.item(fs_target="../../tk/a.txt").fs_rel == "../../tk/a.txt"
    assert p.item(fs_target="/tk/a.txt").fs_rel == "../../../tk/a.txt"
    assert p.item(fs_target="/tmp/fs/a.txt").fs_rel == "../a.txt"

    assert p.item(ct_target="/tk/a.txt").fs_rel == "../tk/a.txt"
    assert p.item(ct_target="../tk/a.txt").fs_rel == "../tk/a.txt"
    assert p.item(ct_target="/ctx/kt/a.txt").fs_rel == "kt/a.txt"


def test_rel_ct_path():
    p = Path(ct_root="/ctx/", fs_root="/tmp/fs/ctx/")
    assert p.item(fs_target="../tk/a.txt").ct_rel == "../tk/a.txt"
    assert p.item(fs_target="/tmp/fs/ctx/a.txt").ct_rel == "a.txt"
    assert p.item(fs_target="/tmp/fs/ctx/kt/a.txt").ct_rel == "kt/a.txt"

    assert p.item(ct_target="./a.txt").fs_rel == "a.txt"
    assert p.item(ct_target="../a.txt").fs_rel == "../a.txt"
    assert p.item(ct_target="/ctx/kt/a.txt").fs_rel == "kt/a.txt"


def test_path_methods():
    p = Path(ct_root="/ctx/", fs_root="/tmp/fs/ctx/")
    assert p.fs_rel(ct_target="/ctx/kt/a.txt") == p.item(ct_target="/ctx/kt/a.txt").fs_rel
    assert p.fs(ct_target="/ctx/kt/a.txt") == p.item(ct_target="/ctx/kt/a.txt").fs
    assert p.ct_rel(ct_target="/ctx/kt/a.txt") == p.item(ct_target="/ctx/kt/a.txt").ct_rel
    assert p.ct(ct_target="/ctx/kt/a.txt") == p.item(ct_target="/ctx/kt/a.txt").ct


def test_sub_path():
    p = Path(ct_root="/ctx/", fs_root="/tmp/fs/ctx/")
    p = p.get(ct_root="./tmp/")
    assert p.item(fs_target="/tmp/fs/ctx/tmp/a.txt").ct_rel == "a.txt"
    assert p.item(ct_target="a.txt").fs == "/tmp/fs/ctx/tmp/a.txt"

