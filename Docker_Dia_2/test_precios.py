import precios

def test_con_descuento():
    assert precio_final(100, 20) == 80

def test_sin_descuento():
    assert precio_final(50) == 50

def test_iva():
    assert precio_con_iva(100, 21) == 121