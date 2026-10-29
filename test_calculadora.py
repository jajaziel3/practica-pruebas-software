import pytest 
from calculadora import sumar, restar, multiplicar, dividir 
 
def test_sumar_positivos(): 
    assert sumar(2, 3) == 5 
 
def test_sumar_negativos(): 
    assert sumar(-2, -3) == -5 
 
def test_restar_positivos(): 
    assert restar(5, 3) == 2 
 
def test_restar_resultado_negativo(): 
    assert restar(3, 5) == -2 
 
def test_multiplicar_negativos(): 
    assert multiplicar(-2, 3) == -6 
    assert multiplicar(-2, -3) == 6 
 
def test_dividir_exactamente(): 
    assert dividir(10, 2) == 5 
 
def test_dividir_decimal(): 
    assert dividir(7, 2) == 3.5 
 
def test_dividir_cero_entre_numero(): 
    assert dividir(0, 5) == 0 
 
def test_dividir_entre_cero(): 
    with pytest.raises(ValueError): 
        dividir(10, 0) 
 
def test_dividir_entrada_no_numerica(): 
    with pytest.raises(TypeError): 
        dividir("diez", 2) 
