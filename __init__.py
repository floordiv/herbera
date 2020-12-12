from herbera.core.breakpoint import breakpoint as bp


debug = True
breakpoint = lambda *args: bp(*args, debug=debug)
