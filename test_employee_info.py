import employee_info as INFO

def test_get_employee_by_age_range():

    assert INFO.get_employees_by_age_range(10,20) == []

    assert len(INFO.get_employees_by_age_range(30, 40)) == 2


def test_calculate_average_salary():

    result = INFO.calculate_average_salary()
    expected_result = 361000 / 6 

    assert result == expected_result

def testget_employees_by_dept():
    
    assert len(INFO.get_employees_by_dept("Sales")) == 2
    assert len(INFO.get_employees_by_dept("Engineering")) == 2
    assert len(INFO.get_employees_by_dept("Marketing")) == 2
