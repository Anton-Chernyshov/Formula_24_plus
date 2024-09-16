/*
CREATED BY ANTON CHERNYSHOV
Made this a while back to re-use code for arduino projects since i was tired of re writing the same thing each time.
Hence made a header file to import, and am constantly upgrading/changing this.
*/


namespace assets {

    class RawPin {
    private:
        int pinNumber;
        bool isAnalogPin;
        int ioMode;
        bool hiLo;



    protected:

        RawPin() { ; }

        RawPin(int p, bool isAnalog, int mode) { // mode is OUTPUT, INPUT , INPUT_PULLUP

            pinNumber = p;
            ioMode = mode;
            isAnalogPin = isAnalog;
            pinMode(pinNumber, ioMode);
        }

        double readFrom() {

            if (isAnalogPin) {
                double voltage = analogRead(pinNumber) * (5.0 / 1023.0);
                return voltage;
            }
            else {
                int voltage = digitalRead(pinNumber);
                return (double)voltage;

            }
        }

        void writeTo(int voltage) { // if is analog its a number in range 0 - 255, but digital is a 1 , 0 
            if (ioMode == OUTPUT) {
                if (isAnalogPin) {
                    analogWrite(pinNumber, voltage);
                }
                else {
                    digitalWrite(pinNumber, voltage);
                }
            }
        }

        int getPinNumber() {
            return pinNumber;
        }

        bool isAnalog() {
            return isAnalogPin;
        }

        
    };




    class Pin {
    private:
        int pinNumber;
        bool isAnalogPin;
        int ioMode;
        bool hiLo;



    public:

        Pin() { ; }

        Pin(int p, bool isAnalog, int mode) { // mode is OUTPUT, INPUT , INPUT_PULLUP

            pinNumber = p;
            ioMode = mode;
            isAnalogPin = isAnalog;
            pinMode(pinNumber, ioMode);
        }

        double readFrom() {

            if (isAnalogPin) {
                double voltage = analogRead(pinNumber) * (5 / 1023);
                return voltage;
            }
            else {
                int voltage = digitalRead(pinNumber);
                return (double)voltage;

            }
        }

        void writeTo(int voltage) { // if is analog its a number in range 0 - 255, but digital is a 1 , 0 

            //if (!(ioMode == OUTPUT)){
            if (isAnalogPin) {

                analogWrite(pinNumber, voltage);
            }
            else {
                digitalWrite(pinNumber, voltage);
            }
            //}
        }

        int getPinNumber() {
            return pinNumber;
        }

        bool isAnalog() {
            return isAnalogPin;
        }

    };








    class LED : public RawPin {
    private:

        int pinNumber;
        bool status;

    public:
        //we do construction
        LED(int p) :
            RawPin(p, false, OUTPUT) // led is always on pin P, with always digital and always output Pin
        {
            pinNumber = p;
            status = false;
        }

        void on() {
            status = true;
            writeTo(HIGH);
        }

        void off() {
            status = false;
            writeTo(LOW);
        }

        bool isOn() {
            return status;
        }

        void toggle() {
            if (isOn()) {

                off();
            }
            else {
                on();
            }


        }

        void blink(int time = 500) {
            toggle();
            delay(time);
            toggle();
            delay(time); // Seccond delay to ensure the LED blinks with proper timing if its looping



        }

        void cBlink(int time1, int time2 = -1) { // used for loops
            if (time2 == -1) {
                time2 = time1;
            }
            toggle();
            delay(time1);
            toggle();
            delay(time2);

        }


    };





    // Button Object

    class Button : public RawPin {
    private:
        int pinNumber;
        bool isNormallyOpen;
    public:
        //constructor
        Button(int p, bool isNormallyOpen = true) :
            RawPin(p, false, INPUT_PULLUP)
        {
            pinNumber = p;
            this->isNormallyOpen = isNormallyOpen;

        }


        bool isDepressed() {
            // returns true if the pin is high, and false if low
            bool val = readFrom();

            if (!val == HIGH) { // this will return true if the button is normally open AND is depressed, if it is normally closed, this will return false.
                return isNormallyOpen;
            }
            else {
                return !isNormallyOpen;
            }

        }

        // Runs passed function if condition is true
        void runOnCondition(bool condition, void (*fPtr)()) { // (*fPtr)() is a function pointer

            if (condition) {
                fPtr();
            }

        }




    };


    class Potentiometer : public RawPin {
    private:
        int pin;
        int currentAngle;
        float voltPerTurn;
        float inputVoltage;
    public:

        Potentiometer(int pinNumber, int possibleAngles, float potinputVoltage = 5) :
            RawPin(pinNumber, true, INPUT_PULLUP)
        {
            pin = pinNumber;
            inputVoltage = potinputVoltage;
            voltPerTurn = inputVoltage / possibleAngles;


        }

        float getAngle() {
            float val = readFrom();
            double voltage = (val + 0.5) * (inputVoltage / 1023);
            float output = voltage / voltPerTurn;
            return output;// / voltPerTurn ;
        }


        void runAtAngle(int angle, void(*fPtr)()) {
            if (getAngle() == angle) {
                fPtr();
            }

        }
        void runAtAngleRange(int minAngle, int maxAngle, void (*fPtr)()) {
            if (getAngle() > minAngle && getAngle() < maxAngle) {
                fPtr();
            }
        }

        void runAtAngleRangeElse(int minAngle, int maxAngle, void (*truePtr)(), void (*falsePtr)()) {
            if (getAngle() > minAngle && getAngle() < maxAngle) {
                truePtr();
            }
            else {
                falsePtr();
            }
        }



    }; //dont forget da semicolon


    class UltrasonicDistanceSensor {
    private:

        int trigPinNumber;
        int echoPinNumber;
        int distance; //distance is in cm and can be up to 4000
        Pin echoPin;
        Pin trigPin;

    public:

        UltrasonicDistanceSensor(int triggerPinNumber, int theEchoPinNumber) {
            trigPinNumber = triggerPinNumber;
            echoPinNumber = theEchoPinNumber;
            echoPin = Pin(echoPinNumber, false, INPUT);
            trigPin = Pin(trigPinNumber, false, OUTPUT);

        }



        int getDistance() {

            trigPin.writeTo(LOW);
            delayMicroseconds(2);
            trigPin.writeTo(HIGH);
            delayMicroseconds(10);
            trigPin.writeTo(LOW);
            long duration = pulseIn(echoPinNumber, HIGH);
            distance = (duration * 0.0343) / 2;
            return distance;
        }



    };


    class DCMotor : public RawPin {
    private:
        int pinNumber;

    public:
        DCMotor(int pinNumber) :
            RawPin(pinNumber, false, OUTPUT) {
            this->pinNumber = pinNumber;


        }

        void spin() {

            writeTo(HIGH);

        }
        void stop() {

            writeTo(LOW);


        }

    };

	class Thermistor : public RawPin {

    private:
		int pinNumber;

    public:
        Thermistor(int pinNumber) :
			RawPin(pinNumber, true, INPUT) {
			this->pinNumber = pinNumber;
		}

		double getTemp() {
			double val = readFrom();
			double voltage = val * (5.0 / 1023.0);
			double resistance = (5.0 - voltage) / voltage;
			double temp = 1.0 / (1.0 / 298.15 + 1.0 / 3435.0 * log(resistance / 10000.0)) - 273.15;
			return temp;
		}
}