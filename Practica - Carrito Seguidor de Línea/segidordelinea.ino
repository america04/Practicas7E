// Pines de sensores
const int sensorIzq = 2;
const int sensorDer = 3;

// Pines de control del L298N (PWM para velocidad)
const int ENA = 5;   // Enable motor izquierdo (PWM)
const int IN1 = 6;   // Control motor izquierdo
const int IN2 = 7;   // Control motor izquierdo
const int IN3 = 8;   // Control motor derecho
const int IN4 = 9;   // Control motor derecho
const int ENB = 10;  // Enable motor derecho (PWM)

// Velocidades (0-255)
const int velocidadMaxima = 110;  // Velocidad máxima
const int velocidadGiro = 130;    // Velocidad para giros

void setup() {
  // Configurar pines de sensores
  pinMode(sensorIzq, INPUT);
  pinMode(sensorDer, INPUT);
  
  // Configurar pines del L298N
  pinMode(ENA, OUTPUT);
  pinMode(IN1, OUTPUT);
  pinMode(IN2, OUTPUT);
  pinMode(IN3, OUTPUT);
  pinMode(IN4, OUTPUT);
  pinMode(ENB, OUTPUT);
  
  Serial.begin(9600);
}

void loop() {
  int izq = digitalRead(sensorIzq);
  int der = digitalRead(sensorDer);

  Serial.print("Sensores -> ");
  Serial.print("Der: ");
  Serial.print(der);
  Serial.print(" Izq: ");
  Serial.print(izq);
  Serial.print(" | ");

  // Control de motores basado en los sensores
  if (izq == 0 && der == 0) {
    // Ambos en blanco -> AVANZAR
    avanzarRecto();
    Serial.println("Avanzando");
  } 
  else if (izq == 1 && der == 0) {
    // Negro izquierdo -> GIRAR DERECHA
    girarDerecha();
    Serial.println("Girando derecha");
  } 
  else if (izq == 0 && der == 1) {
    // Negro derecho -> GIRAR IZQUIERDA
    girarIzquierda();
    Serial.println("Girando izquierda");
  } 
  else if (izq == 1 && der == 1) {
    // Ambos detectan negro -> DETENER
    detenerMotores();
    Serial.println("Detenido");
  }

  delay(100); // Delay reducido para mejor respuesta
}

// Función para avanzar recto
void avanzarRecto() {
  // Motor izquierdo adelante
  digitalWrite(IN1, HIGH);
  digitalWrite(IN2, LOW);
  analogWrite(ENA, velocidadMaxima);
  
  // Motor derecho adelante
  digitalWrite(IN3, HIGH);
  digitalWrite(IN4, LOW);
  analogWrite(ENB, velocidadMaxima);
}

// Función para girar a la izquierda
void girarIzquierda() {
  // Motor izquierdo más lento o parado
  digitalWrite(IN1, LOW);
  digitalWrite(IN2, LOW);
  analogWrite(ENA, 0);
  
  // Motor derecho adelante
  digitalWrite(IN3, HIGH);
  digitalWrite(IN4, LOW);
  analogWrite(ENB, velocidadGiro);
}

// Función para girar a la derecha
void girarDerecha() {
  // Motor izquierdo adelante
  digitalWrite(IN1, HIGH);
  digitalWrite(IN2, LOW);
  analogWrite(ENA, velocidadGiro);
  
  // Motor derecho más lento o parado
  digitalWrite(IN3, LOW);
  digitalWrite(IN4, LOW);
  analogWrite(ENB, 0);
}

// Función para detener los motores
void detenerMotores() {
  analogWrite(ENA, 0);
  analogWrite(ENB, 0);
  digitalWrite(IN1, LOW);
  digitalWrite(IN2, LOW);
  digitalWrite(IN3, LOW);
  digitalWrite(IN4, LOW);
}