// ---------------------------------------------------------------------------
// code to project: smart_stick(ver=1.0).
// ---------------------------------------------------------------------------
int buzzer = 13; //connect buzzer at pin 13
unsigned i;
void buzz() {
  for (i = 0; i < 80; i++) {
    digitalWrite(buzzer, HIGH);
    delay(1);//wait for 1ms
    digitalWrite(buzzer, LOW);
    delay(1);//wait for 1ms
  }
  //output another frequency
  for (i = 0; i < 100; i++) {
    digitalWrite(buzzer, HIGH);
    delay(2);//wait for 2ms
    digitalWrite(buzzer, LOW);
    delay(2);//wait for 2ms
  }
}
#include <NewPing.h>

#define TRIGGER_PIN  12  // Arduino pin tied to trigger pin on the ultrasonic sensor.
#define ECHO_PIN     11  // Arduino pin tied to echo pin on the ultrasonic sensor.
#define MAX_DISTANCE 200 // Maximum distance we want to ping for (in centimeters). Maximum sensor distance is rated at 400-500cm.

NewPing sonar(TRIGGER_PIN, ECHO_PIN, MAX_DISTANCE); // NewPing setup of pins and maximum distance.

void setup() {
  Serial.begin(9600); // Open serial monitor at 115200 baud to see ping results.
  pinMode(13,OUTPUT);
  buzz();
}

void loop() {
  delay(50);                     // Wait 50ms between pings (about 20 pings/sec). 29ms should be the shortest delay between pings.
  Serial.print("Ping: ");
  Serial.print(sonar.ping_cm()); // Send ping, get distance in cm and print result (0 = outside set distance range)
  Serial.println("cm");
  if (sonar.ping_cm() <= 10) {
    digitalWrite(buzzer, HIGH);
  }
  else {
    digitalWrite(buzzer, LOW);
  }
}
