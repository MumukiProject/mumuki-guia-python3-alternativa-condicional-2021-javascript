  
  def test_escribir_cartelito_Dra_Ana_Perez_es_Dra_Ana_Perez(self):
    self.assertEqual(escribir_cartelito("Dra.", "Ana", "Perez"), "Dra. Ana Perez")
  
  def test_escribir_cartelito_Dr_Julio_Gelman_es_Dr_Julio_Gelman(self):
    self.assertEqual(escribir_cartelito("Dr.", "Julio", "Gelman"), "Dr. Julio Gelman")

