int sensorPin = A0;
int sensorValue = 0;

void setup(){
    Serial.begin(9600);
}

void loop(){
    sensorValue = analogRead(sensorPin);
    Serial.print("sensor = ");
    Serial.print(sensorValue);
    delay(2);
}
