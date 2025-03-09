void setup() {
  //Serial.begin(115200);
  Serial.begin(9600);
}

void loop() {
  if (Serial.available() > 0) {
    String received_data = Serial.readStringUntil('\n');
    received_data.trim();


     if (received_data == "ciao"){
          Serial.println("ciao raspb!");
     } else if (received_data == "temperatura") {
          Serial.println("25 gradi");
     } else {
         Serial.println("flag{hai_r07to_il_controllo}");
     }

  }
  // Possibilità di inviare dati dall'ESP32 al PC
  // Serial.println("Dato dall'ESP32");
  delay(100); // Delay per evitare letture eccessive
}
