def method_template(self, x):
    return f"{self.__class__.__name__}: {x ** 2}"

# 클래스 동적으로 생성
DynamicClass = type(
    'DynamicClass',
    (object,),
    {'compute': method_template}
)

obj = DynamicClass()
print(obj.compute(5))
