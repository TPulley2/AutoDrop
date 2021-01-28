#include <Servo.h>

Servo servo;
int pix = 3;
int rec = 5;
int drop = 6;
int pix_in=0;
int rec_in=0;

void setup() {
  servo.attach(drop);
  pinMode(pix, INPUT);
  pinMode(rec, INPUT);
  Serial.begin(4800);
  servo.write(90);
}

void loop() {
  pix_in = pulseIn(pix, HIGH);
  rec_in = pulseIn(rec, HIGH);
  Serial.println(pix_in);
  Serial.println(rec_in);

  //Left Side Drop
  if (pix_in < 1250 && pix_in > 1000) {
    servo.write(35);
    Serial.println("Pix");
  }
  if (rec_in < 1400 && rec_in > 1000){
    servo.write(35);
  }
  //Right Side Drop
  if (pix_in > 1600 && pix_in < 2000) {
    servo.write(145);    
    Serial.println("Pix");
  }
  if (rec_in > 1650 && rec_in < 2000){
    servo.write(145);
  }
  if (rec_in > 1400 && rec_in < 1600){
    servo.write(90);
  }
  else {
    //servo.write(90);
    delay(15);
  }

}
