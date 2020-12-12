from inspect import getmembers, isbuiltin


def display(obj, indent=0, output_manager=print, exclude=('__globals__', 'breakpoint', 'herbera')):
    items = getmembers(obj, lambda member: not isbuiltin(member))
    indentation = '\t' * indent

    for var, val in items:
        if var in exclude:
            continue

        if hasattr(val, '__dict__') and not (var.startswith('__') and var.endswith('__')):
            output_manager(f'{indentation}{var}:')
            display(val, indent=indent + 1, output_manager=output_manager, exclude=exclude)
        else:
            output_manager(f'{indentation}{var}: {repr(val)}')


def display_tree(tree, indent=0, output_manager=print):
    indentation = '\t' * indent

    for var, val in tree.items():
        if isinstance(val, dict):
            output_manager(f'{indentation}{var}:')
            display_tree(val, indent=indent + 1, output_manager=output_manager)
        else:
            output_manager(f'{indentation}{var}: {repr(val)}')


def build(obj, exclude=('__globals__', 'breakpoint', 'herbera')):
    tree = {}
    items = getmembers(obj, lambda member: not isbuiltin(member))

    for var, val in items:
        if var in exclude:
            continue

        if hasattr(val, '__dict__') and not (var.startswith('__') and var.endswith('__')):
            val = build(val, exclude=exclude)

        tree[var] = val

    return tree
