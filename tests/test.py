from mypackage import MyModule
def test_sqr ():
    assert MyModule.sqr(8) == 64, "incorrect"
    assert MyModule.sqr(6) == 36, "incorrect"
    assert MyModule.sqr(10) == 100, "incorrect"