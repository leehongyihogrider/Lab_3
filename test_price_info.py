import price_info as PRICE

def test_total_cost_shopping():
    expected_total_cost = 5*1.20 + 5*1.40 + 1*6.50 + 2*2.70 + 10*0.90 + 1*2.95 + 2*4.95
    total_cost = PRICE.total_cost_shopping()
    assert total_cost == expected_total_cost

def test_cost_of_fruits():
    fruit = 'apple'
    quantity = 10
    expected_cost = quantity * 1.20
    cost = PRICE.cost_of_fruits(fruit, quantity)
    assert cost == expected_cost

