def iterate(initial, function):
    yield initial
    while True:
        initial = function(initial)
        yield initial