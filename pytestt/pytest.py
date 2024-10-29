def pytry():
    '''
    cette fonction essaie de diviser 1 par 0 
    ce qui va causer une erreur de division par zéro.
    '''
    return(1/0)

def test_pytry():
    '''
    cette fonction permet de tester pytest
    '''
    assert(1/0)

def test_divide():
    '''
    cette fonction permet de tester pytest avec plus d'algo
    '''
    for i in range (-5,100):
        assert(5/i)

def test_ranging():
    '''
    cette fonction permet de tester pytest
    '''
    for i in range (-5,100):
        assert(i==5 or i==10)



#Pierre was here
#Pierre was here