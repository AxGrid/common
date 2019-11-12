import axgridcommons.lenses as lenses


def test_get():
    data = {"a": {"b": {"c": 5}}}
    assert lenses.get(data, "a.b.c") == 5
    assert lenses.get(data, "a.b.e", 2) == 2
    assert lenses.get(data, "a.b.e.f.g", [1, 2, 3, 4, 5]) == 3


def test_set():
    data = {"a": {"b": {"c": 5}}}
    __data = lenses.set(data, "a.b.c", 8)
    assert __data == data
    assert lenses.get(data, "a.b.c") == 8
    __data = lenses.set(data, "a.b.e.f.g", 12)
    assert lenses.get(data, "a.b.e.f.g") == 12
