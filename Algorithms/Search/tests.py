from LinearSearch import linear_search

def test_linear_search():
    assert linear_search([1, 2, 3, 4, 5, 6], 6)
    assert not linear_search([1, 2, 3, 4, 5, 6], "E")

if __name__ == "__main__":
    test_linear_search()