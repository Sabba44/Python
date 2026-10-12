import calculador_precio

def test_precios():
    assert calculador_precio.calculador_precio_final(100, 0.2) == 80
    assert calculador_precio.calculador_precio_final(50, 0) == 50