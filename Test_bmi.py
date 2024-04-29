import Lab2.bmi as BMI

def test_bmi_normal_weight() :
    result = []
    height = 1.73
    weight = 57
    result = BMI.calculate_bmi(height,weight)
    assert result == 0
    
def test_bmi_over_weight() :
    result = []
    height = 1.73
    weight = 87
    result = BMI.calculate_bmi(height,weight)
    assert result == 1


def test_bmi_under_weight() :
    result = []
    height = 1.73
    weight = 47
    result = BMI.calculate_bmi(height,weight)
    assert result == -1