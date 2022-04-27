
  def test_medalla_segun_puesto_1(self):
    self.assertEqual(medalla_segun_puesto(1), "oro")

  def test_medalla_segun_puesto_2(self):
    self.assertEqual(medalla_segun_puesto(2), "plata")

  def test_medalla_segun_puesto_3(self):
    self.assertEqual(medalla_segun_puesto(3), "bronce")

  def test_medalla_segun_puesto_4(self):
    self.assertEqual(medalla_segun_puesto(4), "nada")

  def test_medalla_segun_puesto_5(self):
    self.assertEqual(medalla_segun_puesto(5), "nada")

  def test_medalla_segun_puesto_0(self):
    self.assertEqual(medalla_segun_puesto(0), "nada")


