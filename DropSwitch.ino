#include <Servo.h>
Servo servo
const byte pix_interrupt = 3;
const byte rec_interrupt = 2;
int output=10;
volatile unsigned long timer_start;
volatile int last_interrupt_time;

void calcSignal()
{
  last_interrupt_time = micros();
  if(digitalRead(pix_interrupt) == HIGH)
  {
    timer_start = micros();  
  }
  else
  {
    if(timer_start != 0)
    {
      pulse_time = ((volatile int)micros() - timer_start);
      timer_start = 0;
    }
  }
}

void calcSignal2()
{
  last_interrupt_time = micros();
  if(digitalRead(rec_interupt) == HIGH)
  {
    timer_start = micros();
  }
  else
  {
    if(timer_start != 0)
    {
      pulse_time2 = ((volatile int)micros() - timer_start);
      timer_start = 0;
    }
  }
}

void setup() 
{
  timer_start = 0;
  attachInterrupt(1, calcSignal, CHANGE);
  attachInterrupt(0, calcSignal2, CHANGE);
  Serial.begin(115200);
  servo.attach(output);
}

void loop() {
pixHawk_nominal = 1500;
reciver_nominal = 1500

//Left Side Drop
if (pix_in < 1500 || rec_in <= 1400){
  servo.write(90);
  }
//Right Side Drop
if (pix_in > 1500 || rec_in >= 1500){
  servo.write(180);
  }
else{
  print("No Decision Made");
  }

}
