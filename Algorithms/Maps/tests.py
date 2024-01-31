from LRU import LRU

def test_lru(): 
    lru = LRU(capacity=3)
    assert lru.get("foo") == None
    lru.update("foo", 69)
    assert lru.get("foo") == 69
    
    lru.update("bar", 420)
    assert lru.get("bar") == 420

    lru.update("baz", 1337)
    assert lru.get("baz") == 1337

    lru.update("ball", 69420)
    assert lru.get("ball") == 69420
    assert lru.get("foo") == None
    assert lru.get("bar") == 420
    lru.update("foo", 69)
    assert lru.get("foo") == 69
    assert lru.get("bar") == 420
    assert lru.get("baz") == None

if __name__ == "__main__":
    test_lru()