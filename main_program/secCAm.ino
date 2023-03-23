#include <Servo.h>
#define OUR_LED 12


char serialData;
Servo s;

void setup() {
  pinMode(OUR_LED, OUTPUT);
  s.attach(9);
  Serial.begin(9600);
  s.write(0);
}

void loop() {
  if(Serial.available() > 0){
    serialData = Serial.read();

    if(serialData == '1'){
      s.write(180);
      digitalWrite(OUR_LED, HIGH);
    }else if(serialData == '0'){
      digitalWrite(OUR_LED, LOW);
      s.write(0);
    }

  }
}
