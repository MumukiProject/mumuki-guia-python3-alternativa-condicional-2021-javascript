  
  # positivos menores a 100 diferentes de 15
  
  def test_es_numero_de_la_suerte_2_es_verdadero(self):
    self.assertTrue(es_numero_de_la_suerte(2))

  def test_es_numero_de_la_suerte_5_es_verdadero(self):
    self.assertTrue(es_numero_de_la_suerte(5))

  def test_es_numero_de_la_suerte_9_es_verdadero(self):
    self.assertTrue(es_numero_de_la_suerte(9))

  def test_es_numero_de_la_suerte_45_es_verdadero(self):
    self.assertTrue(es_numero_de_la_suerte(45))
    
  def test_es_numero_de_la_suerte_97_es_verdadero(self):
    self.assertTrue(es_numero_de_la_suerte(97))  
    
  # mayores a 100
  
  def test_es_numero_de_la_suerte_101_es_falso(self):
    self.assertFalse(es_numero_de_la_suerte(101))

  def test_es_numero_de_la_suerte_12456_es_falso(self):
    self.assertFalse(es_numero_de_la_suerte(12456))

  def test_es_numero_de_la_suerte_3003_es_falso(self):
    self.assertFalse(es_numero_de_la_suerte(3003))

  # negativos

  def test_es_numero_de_la_suerte_es_falso_si_es_negativo(self):
    self.assertFalse(es_numero_de_la_suerte(-3))

  # el 15

  def test_es_numero_de_la_suerte_15_es_falso(self):
    self.assertFalse(es_numero_de_la_suerte(15))
