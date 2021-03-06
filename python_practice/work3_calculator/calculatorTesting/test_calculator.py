#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2020/8/11 22:42
# @Author  : Yuki


"""
pytest命名规则：
    文件要以test_*.py命名
    类要以Test开头命名，首字母大写
    测试用例方法名要以test_开头

---------------------------------------*-*-*------------------------
用来测试计算器代码的测试代码：

思路：
    1、定义一个计算器测试类
    2、里面有加、减、程、除的测试方法(数字都用传参方式)
    3、测试用例使用参数化方式完成
    4、在调用测试方法之前打印【开始计算】，在调用测试方法之后打印【计算结束】
    5、测试用例中添加断言，验证结果

注意：
    1、本测试类要去调用另一个包下的计算器代码文件方法，才能完成测试，所以要引用Calculator类，实例化对象
    2、本测试类中的四个方法（加减乘除），都需要实例化Calculator类，所以这一部分代码应提取到setup_class方法中
    3、在setup_class方法中实例化Calculator类，以及调用时需要使用self。
    4、参数化需要引用pytest
    5、python的浮点数在进行计算时，使用round(xxx,n)代表对xxx取n位小数

"""

# 引用
from python_practice.work3_calculator.calculatorCode.calculator import Calculator
import pytest
import allure
import yaml

# 从.yml文件中读取测试数据
def get_datas():
    # 打开文件，如果是有中文的文件，需要加encoding=”utf"
    with open("./datas/calc.yml", encoding="utf-8") as f:
        datas = yaml.safe_load(f)
        add_mydatas = datas["add"]["mydatas"]
        add_myids = datas["add"]["myids"]
        addMistake_mydatas = datas["addMistake"]["mydatas"]
        addMistake_myids = datas["addMistake"]["myids"]

        subtract_mydatas = datas["subtract"]["mydatas"]
        asubtract_myids = datas["subtract"]["myids"]
        subtractMistake_mydatas = datas["subtractMistake"]["mydatas"]
        subtractMistake_myids = datas["subtractMistake"]["myids"]

        multiply_mydatas = datas["multiply"]["mydatas"]
        multiply_myids = datas["multiply"]["myids"]
        multiplyMistake_mydatas = datas["multiplyMistake"]["mydatas"]
        multiplyMistake_myids = datas["multiplyMistake"]["myids"]

        divide_mydatas = datas["divide"]["mydatas"]
        divide_myids = datas["divide"]["myids"]
        divideMistake_mydatas = datas["divideMistake"]["mydatas"]
        mdivideMistake_myids = datas["divideMistake"]["myids"]

    return [add_mydatas, add_myids, addMistake_mydatas, addMistake_myids, subtract_mydatas, asubtract_myids, subtractMistake_mydatas, subtractMistake_myids, multiply_mydatas, multiply_myids, multiplyMistake_mydatas, multiplyMistake_myids, divide_mydatas, divide_myids, divideMistake_mydatas, mdivideMistake_myids]

@allure.feature("计算器模块")
class TestCalculator:
    # 类级setup_class.teardown_class（在类中）,只在类中前后运行一次
    def setup_class(self):
        self.calc = Calculator()
        print("\nsetup_calss在类开始时运行一次")

    def teardown_class(self):
        print("teardown_calss在类结束时运行一次")

    # 方法级setup_method.teardown_method（在类中）(等同于setup、teardown),只在方法始末运行一次
    def setup(self):
        print("\n-开始计算-")

    def teardown(self):
        print("-结束计算-")

    # 加法-测试用例参数化

    """
    通过传参传递测试用例
    """
    # @pytest.mark.parametrize("a,b,expected", [
    #     (1, 1, 2),
    #     (-1, -1, -2),
    #     (0, 0, 0),
    #     (0.1, 0.1, 0.2),
    #     (999, 111, 1110)
    # ], ids=["整数", "负数", "零", "小数", "大数"])

    """
    通过get_datas去文件中读取测试用例
    """
    @pytest.mark.parametrize("a,b,expected", get_datas()[0], ids =get_datas()[1])

    @pytest.mark.add
    @allure.story("计算器-加法-正确用例")
    def test_add(self, a, b, expected):
        # calc = Calculator()
        print("测试加法-正确用例")
        result = self.calc.add(a, b)
        assert result == expected

    """
    @pytest.mark.parametrize("a,b,expected", [
        # 错误的用例
        (-1, 1, 1)
    ])
    """
    @pytest.mark.parametrize("a,b,expected", get_datas()[2], ids =get_datas()[3])
    @pytest.mark.add
    @allure.story("计算器-加法-错误用例")
    def test_addMistake(self, a, b, expected):
        # calc = Calculator()
        print("测试加法-错误用例")
        result = self.calc.add(a, b)
        assert result == expected

    # 减法-测试用例参数化
    """
    @pytest.mark.parametrize("a,b,expected", [
        (1, 1, 0),
        (-1, -1, 0),
        (-1, 0, -1),
        (0.3, 0.1, 0.2),
        (999, 111, 888)
    ])
    """
    @pytest.mark.parametrize("a,b,expected", get_datas()[4], ids =get_datas()[5])
    @pytest.mark.subtract
    @allure.story("计算器-减法-正确用例")
    def test_subtract(self, a, b, expected):
        # calc = Calculator()
        print("测试减法-正确用例")
        result = round(self.calc.subtract(a, b), 1)
        assert result == expected

    """
    @pytest.mark.parametrize("a,b,expected", [
        # 错误的用例
        (-1, 1, 1)
    ])
    """
    @pytest.mark.parametrize("a,b,expected", get_datas()[6], ids =get_datas()[7])
    @pytest.mark.subtract
    @allure.story("计算器-减法-错误用例")
    def test_subtractMistake(self, a, b, expected):
        # calc = Calculator()
        print("测试减法-错误用例")
        result = round(self.calc.subtract(a, b), 1)
        assert result == expected

    # 乘法-测试用例参数化
    """
    @pytest.mark.parametrize("a,b,expected", [
        (1, 1, 1),
        (-1, -1, 1),
        (-1, 0, 0),
        (0.3, 0.1, 0.03),
        (999, 111, 110889)
    ])
    """
    @pytest.mark.parametrize("a,b,expected", get_datas()[8], ids =get_datas()[9])
    @pytest.mark.multiply
    @allure.story("计算器-乘法-正确用例")
    def test_multiply(self, a, b, expected):
        # calc = Calculator()
        print("测试乘法-正确用例")
        result = self.calc.multiply(a, b)
        assert result == expected

    """
    @pytest.mark.parametrize("a,b,expected", [
        # 错误的用例
        (-1, 1, 1)
    ])
    """
    @pytest.mark.parametrize("a,b,expected", get_datas()[10], ids =get_datas()[11])
    @pytest.mark.multiply
    @allure.story("计算器-乘法-错误用例")
    def test_multiplyMistake(self, a, b, expected):
        # calc = Calculator()
        print("测试乘法-错误用例")
        result = self.calc.multiply(a, b)
        assert result == expected

    # 除法-测试用例参数化
    """
    @pytest.mark.parametrize("a,b,expected", [
        (0, 1, 0),
        (-1, -1, 1),
        (0.3, 0.1, 3),
        (999, 111, 9)
    ])
    """
    @pytest.mark.parametrize("a,b,expected", get_datas()[12], ids =get_datas()[13])
    @pytest.mark.divide
    @allure.story("计算器-除法-正确用例")
    def test_divide(self, a, b, expected):
        # calc = Calculator()
        print("测试除法-正确用例")
        result = round(self.calc.divide(a, b), 1)
        assert result == expected
    """
    @pytest.mark.parametrize("a,b,expected", [
        # 错误的用例
        (-1, 0, 1),
        (-1, 1, 1)
    ])
    """
    @pytest.mark.parametrize("a,b,expected", get_datas()[14], ids =get_datas()[15])
    @pytest.mark.divide
    @allure.story("计算器-除法-错误用例")
    def test_divideMistake(self, a, b, expected):
        # calc = Calculator()
        try:
            result = round(self.calc.divide(a, b), 1)
            assert result == expected
        except ZeroDivisionError:
            print("测试除法-异常用例：被除数不能为0")
        else:
            print("测试除法-错误用例")
