from django.test import TestCase
from .views import calculator_view


# Write unit tests for calculator_view view.
# Before writing the tests, let's understand the view.
# and also look the urls.py file to understand the URL pattern.
# produce unit test cases now
class TestCalculatorView(TestCase):
    def test_get_request(self):
        response = self.client.get("/")
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, "CalcApp/calculator.html")

    def test_post_request_add(self):
        response = self.client.post("/", {"num1": 10, "num2": 20, "operation": "add"})
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, "CalcApp/calculator.html")
        self.assertEqual(response.context["result"], 30)

    def test_post_request_subtract(self):
        response = self.client.post("/", {"num1": 20, "num2": 10, "operation": "subtract"})
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, "CalcApp/calculator.html")
        self.assertEqual(response.context["result"], 10)

    def test_post_request_multiply(self):
        response = self.client.post("/", {"num1": 10, "num2": 20, "operation": "multiply"})
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, "CalcApp/calculator.html")
        self.assertEqual(response.context["result"], 200)

    # create edge test cases for division. Before that, read the above test cases- which I have modified for url pattern.
    def test_post_request_divide(self):
        response = self.client.post("/", {"num1": 20, "num2": 10, "operation": "divide"})
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, "CalcApp/calculator.html")
        self.assertEqual(response.context["result"], 2)

    # I said write Edge test cases for division. So, what are the edge test cases for division?
    # 1. Divide by zero.
    # 2. Divide a number by itself.
    # 3. Divide a number by 1.
    # 4. Divide a number by -1.
    # 5. Divide a number by a negative number.
    # 6. Divide a number by a positive number.
    # 7. Divide a number by a decimal number.
    # 8. Divide a number by a fraction number.
    # 9. Divide a number by a large number.
    # 10. Divide a number by a small number.

    # Let's write test cases for all the above edge test cases.
    def test_post_request_divide_by_zero(self):
        response = self.client.post("/", {"num1": 20, "num2": 0, "operation": "divide"})
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, "CalcApp/calculator.html")
        self.assertEqual(response.context["result"], "Error: Division by zero")

    # Let's write test cases for all above cases, don't stop after writing for only 1 test case
    def test_post_request_divide_by_itself(self):
        response = self.client.post("/", {"num1": 20, "num2": 20, "operation": "divide"})
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, "CalcApp/calculator.html")
        self.assertEqual(response.context["result"], 1)

    def test_post_request_divide_by_1(self):
        response = self.client.post("/", {"num1": 20, "num2": 1, "operation": "divide"})
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, "CalcApp/calculator.html")
        self.assertEqual(response.context["result"], 20)

    def test_post_request_divide_by_minus_1(self):
        response = self.client.post("/", {"num1": 20, "num2": -1, "operation": "divide"})
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, "CalcApp/calculator.html")
        self.assertEqual(response.context["result"], -20)

    def test_post_request_divide_by_negative_number(self):
        response = self.client.post("/", {"num1": 20, "num2": -10, "operation": "divide"})
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, "CalcApp/calculator.html")
        self.assertEqual(response.context["result"], -2)

    def test_post_request_divide_by_positive_number(self):
        response = self.client.post("/", {"num1": 20, "num2": 10, "operation": "divide"})
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, "CalcApp/calculator.html")
        self.assertEqual(response.context["result"], 2)

    def test_post_request_divide_by_decimal_number(self):
        response = self.client.post("/", {"num1": 20, "num2": 10.5, "operation": "divide"})
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, "CalcApp/calculator.html")
        self.assertEqual(response.context["result"], 1.9047619047619047)

    def test_post_request_divide_by_fraction_number(self):
        response = self.client.post("/", {"num1": 20, "num2": 1/3, "operation": "divide"})
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, "CalcApp/calculator.html")
        self.assertEqual(response.context["result"], 60)

    