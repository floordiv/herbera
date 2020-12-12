import herbera


# all the breakpoint calls will be ignored
herbera.debug = False


x = 5
herbera.breakpoint()
x = 10
herbera.breakpoint()
