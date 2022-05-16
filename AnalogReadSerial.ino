
// partie parametres
const int baudrate = 9600;
const int Button1Pin = 0;
const int Button2Pin = 1;



void setup() {
  // parametre la communication série
  Serial.begin(baudrate);

  //
  pinMode( Button1Pin , INPUT_PULLUP);
  pinMode( Button2Pin , INPUT_PULLUP);
}

// the loop routine runs over and over again forever:
void loop() {

  int Button1 = digitalRead(Button1Pin);
  int Button2 = digitalRead(Button2Pin);

  if(Button1 == 1){
    Serial.println("AI0");
  }
  if(Button2 == 1) {
    Serial.println("AI1");
  }
  
  delay(1);
}
