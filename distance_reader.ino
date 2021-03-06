/*
  Ping))) Sensor

  This sketch reads a PING))) ultrasonic rangefinder and returns the distance
  to the closest object in range. To do this, it sends a pulse to the sensor to
  initiate a reading, then listens for a pulse to return. The length of the
  returning pulse is proportional to the distance of the object from the sensor.

  The circuit:
  - +V connection of the PING))) attached to +5V
  - GND connection of the PING))) attached to ground
  - SIG connection of the PING))) attached to digital pin 7

  created 3 Nov 2008
  by David A. Mellis
  modified 30 Aug 2011
  by Tom Igoe

  This example code is in the public domain.

  http://www.arduino.cc/en/Tutorial/Ping
*/

// this constant won't change. It's the pin number of the sensor's output:
const int pingPin = 7;
const int led = 2; // pin number of the LED

void setup() {
  // initialize serial communication:
  Serial.begin(9600);

  // initialize LED
  pinMode(led, OUTPUT);
  digitalWrite(led, LOW);
}

void loop() {
  // establish variables for duration of the ping, and the distance result in meters:
  float duration, meters;

  // The PING))) is triggered by a HIGH pulse of 2 or more microseconds.
  // Give a short LOW pulse beforehand to ensure a clean HIGH pulse:
  pinMode(pingPin, OUTPUT);
  digitalWrite(pingPin, LOW);
  delayMicroseconds(2);
  digitalWrite(pingPin, HIGH);
  delayMicroseconds(5);
  digitalWrite(pingPin, LOW);

  // The same pin is used to read the signal from the PING))): a HIGH pulse
  // whose duration is the time (in microseconds) from the sending of the ping
  // to the reception of its echo off of an object.
  pinMode(pingPin, INPUT);
  duration = pulseIn(pingPin, HIGH);

  // Convert the time into a distance
  meters = microsecondsToMeters(duration);
  
  Serial.print(meters, 3);
  Serial.println();

  delay(100);

  if (meters <= 2) digitalWrite(led, HIGH); // turn on LED if object is within 2 meters
  else digitalWrite(led, LOW); // turn off LED if no object is within 2 meters
}

float microsecondsToMeters(float microseconds) {
  // The speed of sound is 340 m/s or 29 microseconds per centimeter.
  // The ping travels out and back, so to find the distance of the object we
  // take half of the distance travelled.
  return microseconds / 29 / 2 / 100;
}
