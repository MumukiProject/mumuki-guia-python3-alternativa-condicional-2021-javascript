
function saludarA(quien, horario) {
  if (horario < 12){
    return "Buenos días " + quien;
  } else if (horario < 19) {
    return "Buenas tardes " + quien;
  } else {
    return "Buenas noches " + quien;
  }
}

function saludarARecargado(quien, horario) {
  if (horario < 19){
    return "Buenas tardes " + quien;
  } else if (horario < 12) {
    return "Buenos días " + quien;
  } else {
    return "Buenas noches " + quien;
  }
    