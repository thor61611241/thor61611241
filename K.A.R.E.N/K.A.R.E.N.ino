//ALL LIBRARIES#############################################################################################################################################################//
#include <DS1307RTC.h>
#include <LiquidCrystal.h>
#include <NewPing.h>
#include <Servo.h>
#include <SD.h>
#include <TMRpcm.h>
#include <TimeLib.h>
#include <Wire.h>
#include <SPI.h>
#include <SD.h>
#include <SoftwareSerial.h>
#define chipSelect 53
//ALL VARIABLES#############################################################################################################################################################//
int pr1;
int pl1;
Servo h1;
Servo h2;
Servo rh1;
Servo lh1;
Servo rh2;
Servo lh2;
Servo h22;
int pos = 0;
String voice;
TMRpcm tmrpcm;
int led1 = 22;
int led2 = 24;
int led3 = 26;
int led4 = 28;
int led5 = 30;
int led6 = 32;
int led7 = 34;
int led8 = 36;
int led9 = 38;
int led10 = 40;
int led11 = 42;
int led12 = 44;
int led13 = 31;
int led14 = 33;
int led15 = 35;
int led16 = 37;
int led17 = 39;
int led18 = 41;
int buzzer = A15;
int speaker = 46;
int distance = 100;
int gas_sensor = A14;
int distanceLeft = 0;
int distanceRight = 0;
int motion_sensor = A9;
int flame_sensor = A13;
int light_sensor = A12;
float smokePercentage;
#define TRIGGER_PIN2  9
#define ECHO_PIN2     10
#define TRIGGER_PIN  A10
#define ECHO_PIN     A11
#define MAX_DISTANCE 500
int hand_steralizer = 11;
boolean goesForward = false;
const int left_motor_forward = 29;
const int right_motor_forward = 25;
const int left_motor_backward = 27;
const int right_motor_backward = 23;
LiquidCrystal lcd(17, 15, 14, 9, 10, 16);
NewPing sonar(TRIGGER_PIN, ECHO_PIN, MAX_DISTANCE);
NewPing sonar1(TRIGGER_PIN2, ECHO_PIN2, MAX_DISTANCE);
//ALL FUNCTIONS#############################################################################################################################################################//
int lookRight() {
  h1.write(50);
  delay(500);
  int distance = readPing();
  delay(100);
  h1.write(115);
  return distance;
}
int lookLeft() {
  h1.write(170);
  delay(500);
  int distance = readPing();
  delay(100);
  h1.write(115);
  return distance;
  delay(100);
}
int readPing() {
  delay(70);
  int cm = sonar.ping_cm();
  if (cm == 0) {
    cm = 250;
  }
  return cm;
}
void movestop() {
  digitalWrite(right_motor_forward, LOW);
  digitalWrite(left_motor_forward, LOW);
  digitalWrite(right_motor_backward, LOW);
  digitalWrite(left_motor_backward, LOW);
}
void turnright() {
  digitalWrite(left_motor_forward, HIGH);
}
void turnleft() {
  digitalWrite(right_motor_forward, HIGH);
}
void moveforward() {
  if (!goesForward) {
    while (sonar.ping_cm() > 10){
      goesForward = true;
      digitalWrite(left_motor_forward, HIGH);
      digitalWrite(right_motor_forward, HIGH);
    }
    if (sonar.ping_cm() <= 10){
      movestop();
      delay(900);
      distanceRight = lookRight();
      delay(900);
      distanceLeft = lookLeft(); 
      if (distanceRight >= distanceLeft){
        turnright();
        digitalWrite(left_motor_forward, HIGH);
        digitalWrite(right_motor_forward, HIGH);       
      }
      else{
        turnleft();
        digitalWrite(left_motor_forward, HIGH);
        digitalWrite(right_motor_forward, HIGH);
      }      
    }  
  }
}
void movebackward() {
  goesForward = false;
  while (sonar1.ping_cm() > 10){
    digitalWrite(left_motor_backward, HIGH);
    digitalWrite(right_motor_backward, HIGH);   
  }
  if (sonar1.ping_cm() <= 10){
    digitalWrite(left_motor_backward, LOW);
    digitalWrite(right_motor_backward, LOW);    
  }
}
void shakehands() {
  int pos2 = 90;
  for (pos2 = 0; pos2 <= 180; pos2 += 1) { // goes from 0 degrees to 180 degrees
    // in steps of 1 degree
    rh1.write(pos2);              // tell servo to go to position in variable 'pos'
    delay(15);                       // waits 15 ms for the servo to reach the position
  }
  for (pos2 = 120; pos2 >= 0; pos2 -= 1) { // goes from 180 degrees to 0 degrees
    rh1.write(pos2);              // tell servo to go to position in variable 'pos'
    delay(15);                       // waits 15 ms for the servo to reach the position
  }
}
void handsup() {
  rh2.write(170);
  lh2.write(10);
  rh1.write(60);
  lh1.write(120);
}
void handsdown() {
  rh2.write(30);
  lh2.write(150);
  rh1.write(60);
  lh1.write(120);
}

void handsside() {
  rh2.write(90);
  rh2.write(90);
}

void handsfront() {
  rh1.write(80);
  lh1.write(100);
  rh2.write(30);
  lh2.write(150);
}

void righthandup() {
  rh1.write(170);
}

void righthanddown() {
  rh1.write(30);
}

void lefthandup() {
  lh1.write(30);
}

void lefthanddown() {
  lh1.write(150);
}

void watchright() {
  h1.write(30);
}

void watchleft() {
  h1.write(150);
}

void watchfront() {
  h1.write(90);
}

void lighton() {
  digitalWrite(led1, HIGH);
  digitalWrite(led3, HIGH);
  digitalWrite(led4, HIGH);
  digitalWrite(led4, HIGH);
  digitalWrite(led5, HIGH);
  digitalWrite(led6, HIGH);
  digitalWrite(led7, HIGH);
  digitalWrite(led8, HIGH);
  digitalWrite(led9, HIGH);
  digitalWrite(led10, HIGH);
  digitalWrite(led11, HIGH);
  digitalWrite(led12, HIGH);
  digitalWrite(led13, HIGH);
  digitalWrite(led14, HIGH);
  digitalWrite(led15, HIGH);
  digitalWrite(led16, HIGH);
  digitalWrite(led17, HIGH);
  digitalWrite(led18, HIGH);
}

void lightoff() {
  digitalWrite(led1, LOW);
  digitalWrite(led3, LOW);
  digitalWrite(led4, LOW);
  digitalWrite(led4, LOW);
  digitalWrite(led5, LOW);
  digitalWrite(led6, LOW);
  digitalWrite(led7, LOW);
  digitalWrite(led8, LOW);
  digitalWrite(led9, LOW);
  digitalWrite(led10, LOW);
  digitalWrite(led11, LOW);
  digitalWrite(led12, LOW);
  digitalWrite(led13, LOW);
  digitalWrite(led14, LOW);
  digitalWrite(led15, LOW);
  digitalWrite(led16, LOW);
  digitalWrite(led17, LOW);
  digitalWrite(led18, LOW);
}

void partymode() {
  digitalWrite(led1, HIGH);
  digitalWrite(led1, LOW);
  delay(1000);
  digitalWrite(led2, HIGH);
  digitalWrite(led2, LOW);
  delay(1000);
  digitalWrite(led3, HIGH);
  digitalWrite(led3, LOW);
  delay(1000);
  digitalWrite(led4, HIGH);
  digitalWrite(led4, LOW);
  delay(1000);
  digitalWrite(led5, HIGH);
  digitalWrite(led5, LOW);
  delay(1000);
  digitalWrite(led6, HIGH);
  digitalWrite(led6, LOW);
  delay(1000);
  digitalWrite(led7, HIGH);
  digitalWrite(led7, LOW);
  delay(1000);
  digitalWrite(led8, HIGH);
  digitalWrite(led8, LOW);
  delay(1000);
  digitalWrite(led9, HIGH);
  digitalWrite(led9, LOW);
  delay(1000);
  digitalWrite(led10, HIGH);
  digitalWrite(led10, LOW);
  delay(1000);
  digitalWrite(led11, HIGH);
  digitalWrite(led11, LOW);
  delay(1000);
  digitalWrite(led12, HIGH);
  digitalWrite(led12, LOW);
  delay(1000);
  digitalWrite(led13, HIGH);
  digitalWrite(led13, LOW);
  delay(1000);
  digitalWrite(led14, HIGH);
  digitalWrite(led14, LOW);
  delay(1000);
  digitalWrite(led15, HIGH);
  digitalWrite(led15, LOW);
  delay(1000);
  digitalWrite(led16, HIGH);
  digitalWrite(led16, LOW);
  delay(1000);
  digitalWrite(led17, HIGH);
  digitalWrite(led17, LOW);
  delay(1000);
  digitalWrite(led18, HIGH);
  digitalWrite(led18, LOW);
  delay(1000);
}

void bodyguardmode() {
  float motionvalue = digitalRead(motion_sensor);
  if ( motionvalue == HIGH) {
    digitalWrite(buzzer, HIGH);
  }
  else {
    digitalWrite(buzzer, LOW);
  }
}

void handgell() {
  digitalWrite(hand_steralizer, HIGH);
  delay(2000);
  digitalWrite(hand_steralizer, LOW);
}

void dance() {
  digitalWrite(left_motor_forward, HIGH);
  digitalWrite(left_motor_backward, HIGH);
  delay(500);
  digitalWrite(right_motor_forward, HIGH);
  digitalWrite(right_motor_backward, HIGH);
  for (pos = 0; pos <= 180; pos -= 1) {
    // goes from 0 degrees to 180 degrees
    // in steps of 1 degree
    lh1.write(pos);              // tell servo to go to position in variable 'pos'
    delay(15);                       // waits 15 ms for the servo to reach the position
  }
  for (pos = 180; pos >= 0; pos += 1) { // goes from 180 degrees to 0 degrees
    lh1.write(pos);              // tell servo to go to position in variable 'pos'
    delay(15);                       // waits 15 ms for the servo to reach the position
  }
  for (pos = 0; pos <= 180; pos += 1) {
    // goes from 0 degrees to 180 degrees
    // in steps of 1 degree
    rh1.write(pos);              // tell servo to go to position in variable 'pos'
    delay(15);                       // waits 15 ms for the servo to reach the position
  }
  for (pos = 180; pos >= 0; pos -= 1) { // goes from 180 degrees to 0 degrees
    rh1.write(pos);              // tell servo to go to position in variable 'pos'
    delay(15);                       // waits 15 ms for the servo to reach the position
  }
}
void digitalClockDisplay(){
  // digital clock display of the time
  Serial.print(hour());
  printDigits(minute());
  printDigits(second());
  Serial.print(" ");
  Serial.print(day());
  Serial.print(" ");
  Serial.print(month());
  Serial.print(" ");
  Serial.print(year()); 
  Serial.println(); 
}

void printDigits(int digits){
  // utility function for digital clock display: prints preceding colon and leading 0
  Serial.print(":");
  if(digits < 10)
    Serial.print('0');
  Serial.print(digits);
}

void setup() {
  tmrpcm.speakerPin = 46;
  Serial.begin(9600);
  lcd.begin(16, 4);
  rh1.attach(6);
  rh2.attach(5);
  lh2.attach(7);
  h2.attach(9);
  h1.attach(4); 
  lh1.attach(8);
  h22.attach(3);
  pinMode(led1, OUTPUT);
  pinMode(led2, OUTPUT);
  pinMode(led3, OUTPUT);
  pinMode(led4, OUTPUT);
  pinMode(led5, OUTPUT);
  pinMode(led6, OUTPUT);
  pinMode(led7, OUTPUT);
  pinMode(led8, OUTPUT);
  pinMode(led9, OUTPUT);
  pinMode(led10, OUTPUT);
  pinMode(led11, OUTPUT);
  pinMode(led12, OUTPUT);
  pinMode(led13, OUTPUT);
  pinMode(led14, OUTPUT);
  pinMode(led15, OUTPUT);
  pinMode(led16, OUTPUT);
  pinMode(led17, OUTPUT);
  pinMode(led18, OUTPUT);
  pinMode(buzzer, OUTPUT);
  pinMode(right_motor_forward, OUTPUT);
  pinMode(left_motor_forward, OUTPUT);
  pinMode(right_motor_backward, OUTPUT);
  pinMode(left_motor_backward, OUTPUT);
  if (!SD.begin(chipSelect)) {
    Serial.println("SD FAIL");
    return;
  }
  Serial.println("SD HAS BEEN FOUND");
  while (!Serial) ; // wait until Arduino Serial Monitor opens
  setSyncProvider(RTC.get);   // the function to get the time from the RTC
  if (timeStatus() != timeSet) {
    Serial.println("Unable TO CONNECT WITH RTC");
  }
  else {
    Serial.println("RTC HAS BEEN FOUND");
  }
  if (sonar.ping_cm() == 0) {
    Serial.println("Unable TO CONNECT WITH ULTRASONIC");
  }
  else {
    Serial.println("ULTRASONIC HAS BEEN FOUND");
  }
  distance = readPing();
  delay(100);
  lcd.setCursor(0, 0);
  lcd.print("ABDALRAHMAN");
  lcd.setCursor(0, 1);
  lcd.print("01029388659");
  lcd.setCursor(2, 0);
  lcd.print("OTHMAN TECH");
  lcd.setCursor(3, 1);
  lcd.print("industries");
  delay(1000);
  lcd.clear();
  lcd.setCursor(0, 0);
  lcd.print("usingarduinotech");
  lcd.setCursor(0, 1);
  lcd.print("using AI");
  lcd.setCursor(2, 0);
  lcd.print("OTHMAN TECH");
  lcd.setCursor(3, 1);
  lcd.print("industries");
  delay(1000);
  lcd.clear();
  lcd.setCursor(0, 0);
  lcd.print("introduce");
  lcd.setCursor(0, 1);
  lcd.print("K.A.R.E.N");
  lcd.setCursor(2, 0);
  lcd.print("AI & ROBOT");
  lcd.setCursor(3, 1);
  lcd.print("OTHMANtech");
  tmrpcm.play("self.wav");
  delay(1000);
  lcd.clear();
}
void loop() {
  while (Serial.available()) {
    delay(10);
    char c = Serial.read();
    voice += c;
  }
  //voice function
  if (voice.length() > 0) {
    Serial.println(voice);
    if ((voice == "say hi") or (voice == "hi") or (voice == "1") or (voice == "hello")){
      tmrpcm.play("hi.wav");
    }
    else if ((voice == "sing") or (voice == "turn on songs") or (voice == "2")) {
      tmrpcm.play("music1.wav");
    }
    else if ((voice == "good bye") or (voice == "see you soon") or (voice == "3")){
      tmrpcm.play("bye.wav");
    }
    else if ((voice == "good morning") or (voice == "morning") or (voice == "4")){
      tmrpcm.play("goodmorning.wav");
    }
    else if ((voice == "good evening") or (voice == "evening") or (voice == "5")) {
      tmrpcm.play("goodevining.wav");
    }
    else if ((voice == "good afternoon") or (voice == "afternoon") or (voice == "6")) {
      tmrpcm.play("goodafternoon.wav");
    }
    else if ((voice == "shake hands") or (voice == "give me your hand") or (voice == "7")) {
      shakehands();
    }
    else if ((voice == "hands up") or (voice == "rise up your hands") or (voice == "8")) {
      handsup();
    }
    else if ((voice == "hands down") or (voice == "put your arms down") or (voice == "9")) {
      handsdown();
    }

    else if ((voice == "hands side") or (voice == "A")){
      handsside();
    }

    else if ((voice == "hands front") or (voice == "B")) {
      handsfront();
    }

    else if ((voice == "right hand up") or (voice == "C")){
      righthandup();
    }

    else if ((voice == "right hand down") or (voice == "D")) {
      righthanddown();
    }

    else if ((voice == "left hand up") or (voice == "K")){
      lefthandup();
    }

    else if ((voice == "left hand down") or (voice == "J")) {
      lefthanddown();
    }

    else if ((voice == "watch right") or (voice == "E")){
      watchright();
    }

    else if ((voice == "watch left") or (voice == "N")){
      watchleft();
    }

    else if ((voice == "watch front") or (voice == "O")){
      watchfront();
    }

    else if ((voice == "move forward") or (voice == "F")) {
      moveforward();
    }

    else if ((voice == "turn left") or (voice == "L")) {
      turnleft();
    }

    else if ((voice == "turn right") or (voice == "R")){
      turnright();
    }

    else if ((voice == "go backward") or (voice == "G")) {
      movebackward();
    }

    else if ((voice == "stop") or (voice == "S")) {
      movestop();
    }

    else if ((voice == "light on") or (voice == "M")) {
      lighton();
    }

    else if ((voice == "light off") or (voice == "m")) {
      lightoff();
    }

    else if ((voice == "party mode") or (voice == "P")){
      partymode();
    }

    else if ((voice == "body guard mode") or (voice == "Q")) {
      bodyguardmode();
    }

    else if ((voice == "hand gell") or (voice == "T")){
      handgell();
    }

    else if ((voice == "dance") or (voice == "U")){
      dance();
    }
    voice = "";
  }
  //LIGHT FUNCTION
  int light = analogRead(light_sensor);
  Serial.print("light = ");
  Serial.print(light);  
  if (light < 10) {
    lighton();
    Serial.println(" -Dark");
  }
  else if (light < 200) {
    Serial.println(" - Dim");
    lightoff();
  }
  else if (light < 800) {
    Serial.println(" - Bright");
    lightoff();
  } else {
    Serial.println(" - Very bright");
  }
  //DISTANCE FUNCTION
  Serial.print("distance front = ");
  Serial.print(sonar.ping_cm()); 
  Serial.println("cm");
  Serial.print("Distance back = ");
  Serial.print(sonar1.ping_cm());
  Serial.println("cm");
  if (sonar.ping_cm() <= 10) {
    digitalWrite(buzzer, HIGH);
  }
  else {
    digitalWrite(buzzer, LOW);
  }
  //GAS FUNCTION
  float gas = analogRead(gas_sensor);
  Serial.print("gas statuse: ");
  Serial.println(gas);
  if (gas == HIGH) {
    digitalWrite(buzzer, HIGH);
  }
  //FIRE FUNCTION
  float fire = analogRead(flame_sensor);
  Serial.print("fire statuse: ");
  Serial.println(fire);
  if (fire == LOW) {
    digitalWrite(buzzer, HIGH);
  }
  //RTC
  if (timeStatus() == timeSet) {
    digitalClockDisplay();
  }  
  Serial.println("#####################################################################");
  delay(1000);
}
