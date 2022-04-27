  
  def test_valor_envido_2_es_2(self):
    self.assertEqual(valor_envido(2), 2)
  
  def test_valor_envido_1_es_1(self):
    self.assertEqual(valor_envido(1), 1)
  
  def test_valor_envido_5_es_5(self):
    self.assertEqual(valor_envido(5), 5)
    
  def test_valor_envido_7_es_7(self):
    self.assertEqual(valor_envido(7), 7)  
  
  def test_valor_envido_12_es_0(self):
    self.assertEqual(valor_envido(12), 0)
  
  def test_valor_envido_11_es_0(self):
    self.assertEqual(valor_envido(11), 0)
  
  def test_valor_envido_10_es_0(self):
    self.assertEqual(valor_envido(10), 0)
