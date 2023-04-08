# test_order_attrs.py

from my_vim_scripts import order_attrs


def test_order_attrs():
    before = '<tag b="on" a="right">'
    after = '<tag a="right" b="on">'

    assert order_attrs(before) == after
