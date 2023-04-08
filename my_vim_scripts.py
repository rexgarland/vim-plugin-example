# my_vim_scripts.py

import parsley

# the -> syntax lets us write Python code
grammar = """
tag = '<' name:n attrs:a '>' -> {'name': n, 'attrs': a}

name = <letter+>
attrs = (ws attr)*
attr = <name '="' (~'"' anything)* '"'>
"""

parse = parsley.makeGrammar(grammar, bindings={})


def order_attrs(before):
    tag = parse(before).tag()
    new_attrs = " ".join(sorted(tag["attrs"]))
    after = "<" + tag["name"] + " " + new_attrs + ">"
    return after
