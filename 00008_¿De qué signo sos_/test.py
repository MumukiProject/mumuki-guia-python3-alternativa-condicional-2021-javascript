
  def test_signo_10_es_1(self):
    self.assertEqual(signo(10), 1)

  def test_signo_1_es_1(self):
    self.assertEqual(signo(1), 1)

  def test_signo_0_es_0(self):
    self.assertEqual(signo(0), 0)

  def test_signo_menos_65_es_menos_1(self):
    self.assertEqual(signo(-65), -1)

  def test_signo_menos_87_es_menos_1(self):
    self.assertEqual(signo(-87), -1)


