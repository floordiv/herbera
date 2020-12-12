from sys import modules
from herbera.core.tree import display


head_module = modules['__main__']


def breakpoint(from_context=None, output_manager=print, debug=True):
    """
    From context: any object, which supports obj.__dict__
    output manager: any callable, which takes at least one param: text.
    """

    if not debug:
        return

    if from_context is None:
        from_context = head_module

    display(from_context, output_manager=output_manager)
    input('> Press Enter to continue')


if __file__ == '__main__':
    raise UserWarning('debugger started as a stand-alone program')
