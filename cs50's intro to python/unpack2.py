def f(*args, **kwargs):
    print("Positional: ", args)
    print("Named: ", kwargs)


f(100, 25, 5)
f(galleons=100, sickles=50, knuts=25)
