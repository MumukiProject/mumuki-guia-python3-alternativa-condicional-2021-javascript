  
  def test_valor_canto_truco_retruco_es_3(self):
    self.assertEqual(valor_canto_truco("retruco"), 3)
  
  def test_valor_canto_truco_truco_es_2(self):
    self.assertEqual(valor_canto_truco("truco"), 2)
  
  def test_valor_canto_truco_vale_cuatro_es_4(self):
    self.assertEqual(valor_canto_truco("vale cuatro"), 4)
  
