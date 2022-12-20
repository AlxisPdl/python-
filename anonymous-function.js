// fonction anonyme

let my_function = function(a, b) {
    let result = a + b;
    return result;
};

let foo = my_function;

result = my_function(123, 42);
console.log(result);

my_number1 = 123
my_number2 = 42
result = foo(my_number1, my_number2)
console.log(result)

def calculer(calcul1: callable, calcul2: callable, a:float, b: float, c:float) -> float: 
    result = calcul1(a, b)
    result = calcul2(result, c)

    return = result

result = calculer(addition, addition, 123, 42, 14)
print(result)
