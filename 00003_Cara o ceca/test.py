  
  def test_decision_con_moneda_cara_pizzas_empanadas_es_pizzas(self):
    self.assertEqual(decision_con_moneda("cara", "pizzas", "empanadas"), "pizzas")

  def test_decision_con_moneda_cara_asado_empanadas_es_asado(self):
    self.assertEqual(decision_con_moneda("cara", "asado", "empanadas"), "asado")

  def test_decision_con_moneda_ceca_pizzas_empanadas_es_empanadas(self):
    self.assertEqual(decision_con_moneda("ceca", "pizzas", "empanadas"), "empanadas")

  def test_decision_con_moneda_ceca_pizzas_pastas_es_pastas(self):
    self.assertEqual(decision_con_moneda("ceca", "pizzas", "pastas"), "pastas")


