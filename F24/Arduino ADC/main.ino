const int thermistorPins[] = { 
A0, // AMBIENT
A1, // MOTOR
A2, // BATTERY
A3 // NOT USED

}; // Array of thermistor pins

const int numThermistors = sizeof(thermistorPins) / sizeof(thermistorPins[0]); // Number of thermistors
float R1 = 10000; // Resistance of the fixed resistor in ohms
float c1 = 1.009249522e-03, c2 = 2.378405444e-04, c3 = 2.019202697e-07;

void setup() {
	Serial.begin(9600);
}

void loop() {
	for (int i = 0; i < numThermistors; i++) {
		temperatures[i] = getTemperature(thermistorPins[i]);
		Serial.print("Temperature ");
		Serial.print(i + 1);  // Print thermistor number
		Serial.print(": ");
		Serial.print(temperatures[i]);
		Serial.println(" *C");
	}
	delay(50);
}



function getTemperature(int pin) {
	// Steinhart-Hart equation 
	int Vo = analogRead(pin);
	float R2 = R1 * (1023.0 / (float)Vo - 1.0);
	float logR2 = log(R2);
	float T = (1.0 / (c1 + c2 * logR2 + c3 * logR2 * logR2 * logR2));
	T = T - 273.15; // Convert Kelvin to Celsius
	return T;
}