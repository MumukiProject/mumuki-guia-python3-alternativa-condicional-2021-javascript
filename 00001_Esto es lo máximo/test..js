describe('', function() {
  it("el maximo entre 4 y 10 es 10", function() {
    assert.equal(maximo(4, 10), 10);
  });
  
  it("el maximo entre 3 y 9 es 9", function() {
    assert.equal(maximo(3, 9), 9);
  });
  
  it("el maximo entre 20 y 11 es 20", function() {
    assert.equal(maximo(20, 11), 20);
  });
  
  it("el maximo entre 25 y 15 es 25", function() {
    assert.equal(maximo(25, 15), 25);
  });
})
