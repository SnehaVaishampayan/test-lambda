import hello
def test_add():
    assert hello.add(3, 4) == 7
    assert hello.add(3.5, 4) == 7



def test_to_sentence():
    assert hello.to_sentence('apple') == 'Apple.'
    assert hello.to_sentence('Apple trees') == 'Apple trees.'
