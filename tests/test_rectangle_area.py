from ctypes import windll
from sys import exc_info

import  pytest
from app.geometry.rectangle_area import rectangle_area


def test_rectangle_area_correct_length():
    """
    Проверка целых значений длин сторон прямоугольника
    :return:
    """
    #Arrange
    width = "3"
    height = "5"
    expected_result = 15
    #Act
    actual_result = rectangle_area(width, height)
    #Assert
    assert actual_result == pytest.approx(expected_result)

def test_rectangle_area_string_data():
    """
    тестирование вычисления площади со строкой в качестве стороны прямоугольника
    :return:
    """
    #Arrangle
    width = "hello"
    height = "5.2"
    #Act
    with pytest.raises(ValueError) as exc_info:
        rectangle_area(width, height)
    #assert
    assert str(exc_info.value) == "введено не числовое значение стороны"