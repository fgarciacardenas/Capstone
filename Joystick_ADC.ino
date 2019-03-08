// Analog Pins connected to the joystick outputs
int Eje_X = 1;
int Eje_Y = 2;

void setup() {

  //Initialize serial communication at 9600 bps
  Serial.begin(9600);
 
  }

void loop() {

  //Assign the analog values received to variables
  int DX = analogRead(Eje_X);
  int DY = analogRead(Eje_Y);

  //Concatenate the variables in a String
  String Lectura = String(DX) + "/" + String(DY);

  //Prints the String to the serial port
  Serial.println(Lectura);
  
}
