void setup() {
  Serial.begin(9600); 
  delay(2000);        
}

void loop() {
  String message = "Hello from FREENOVE!";
  Serial.println(message); 
  delay(1000);            
}
