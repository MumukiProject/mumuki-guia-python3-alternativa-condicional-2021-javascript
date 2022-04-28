  
  def test_escribe_un_cartelito_largo_cuando_el_nombre_es_carla_toledo(self):
    self.assertEqual(escribir_cartelito_optimo("Ing.", "Carla", "Toledo"), "Ing. Carla Toledo")
  
  def test_escribe_un_cartelito_largo_cuando_el_nombre_es_branco_luis(self):
    self.assertEqual(escribir_cartelito_optimo("Ing.", "Branco", "Luis"), "Ing. Branco Luis")
  
  def test_escribe_un_cartelito_corto_cuando_el_nombre_es_estanislao_schwarzschild(self):
    self.assertEqual(escribir_cartelito_optimo("Dr.", "Estanislao", "Schwarzschild"), "Dr. Schwarzschild")
  
  def test_escribe_un_cartelito_corto_cuando_el_nombre_es_katherine_boumann(self):
    self.assertEqual(escribir_cartelito_optimo("Ing.", "Katherine", "Boumann"), "Ing. Boumann")