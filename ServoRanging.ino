#include <Servo.h>

//int pwm = 5;
int input1 = 5;
Servo servo;
//int pos = 90;

void setup() {
  //servo.attach(pwm);
  //pinMode(pwm, OUTPUT);
  pinMode(input1, INPUT);
  Serial.begin(4800);
  
}

void loop() {
  //servo.write(270);
  Serial.println(pulseIn(input1, HIGH));
  delay(1000);

  //servo.writeMicroseconds(1500);
  //Serial.println(pulseIn(5, HIGH));
  //delay(1000);

  //servo.writeMicroseconds(1200);
  //delay(2000);

  //servo.writeMicroseconds(1700);
  //Serial.println(pulseIn(5, HIGH));
  //delay(1000);

//  analogWrite(pwm, 200);
//  delay(1000);
//
//  analogWrite(pwm, 0);
//  delay(1000);
//
//  analogWrite(pwm, -200);
//  delay(1000);
  
//  for (pos = 90; pos >= 0; pos--){
//    servo.write(pos);
//    delay(15);
//  }
//  for (pos = 0; pos<=90 ; pos++){
//    servo.write(pos);
//    delay(15);
//  }
//  for (pos = 90; pos <= 180; pos++){
//    servo.write(pos);
//    delay(15);
//  }

}


