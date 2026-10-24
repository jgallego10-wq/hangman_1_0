import random
from words import PALABRAS
from figures import ETAPAS

def obtener_palabra():
    """Selecciona una palabra aleatoria de la lista."""
    return random.choice(PALABRAS)

def mostrar_tablero(palabra_secreta, letras_adivinadas, vidas):
    """Muestra el dibujo del monigote, las vidas y las letras descubiertas."""
    print(ETAPAS[vidas])
    print(f"Vidas restantes: {vidas}")
    
    estado_palabra = []
    for letra in palabra_secreta:
        if letra in letras_adivinadas:
            estado_palabra.append(letra)
        else:
            estado_palabra.append("_")
            
    print("Palabra: " + " ".join(estado_palabra))
    print("-" * 35)

def pedir_letra(letras_usadas):
    """Pide y valida que el jugador ingrese solo una letra válida."""
    while True:
        entrada = input("Ingresa una letra: ").strip().upper()
        
        if len(entrada) != 1 or not entrada.isalpha():
            print("⚠️ Debe ingresar solo 1 letra (A-Z).")
            continue
            
        if entrada in letras_usadas:
            print("⚠️ Ya ha utilizado la letra.")
            continue
            
        return entrada

def jugar():
    """Ejecuta una partida completa del ahorcado."""
    palabra_secreta = obtener_palabra()
    vidas = 6
    letras_adivinadas = set()
    letras_usadas = set()
    
    print("\n🎮 ¡Bienvenido a Hangman 1.0! Tienes 6 vidas.")
    
    while vidas > 0:
        mostrar_tablero(palabra_secreta, letras_adivinadas, vidas)
        letra = pedir_letra(letras_usadas)
        letras_usadas.add(letra)
        
        if letra in palabra_secreta:
            letras_adivinadas.add(letra)
            print(f"✅ ¡Correcto! La letra {letra} está en la palabra.")
            
            if all(l in letras_adivinadas for l in palabra_secreta):
                mostrar_tablero(palabra_secreta, letras_adivinadas, vidas)
                print("🎉 ¡FELICITACIONES, GANASTE! Has descubierto la palabra.")
                return
        else:
            vidas -= 1
            print(f"❌ Letra incorrecta. Pierdes 1 vida.")
            
    mostrar_tablero(palabra_secreta, letras_adivinadas, 0)
    print("💀 ¡HAS PERDIDO! Te has quedado sin vidas.")
    print(f"La palabra secreta era: {palabra_secreta}")

def main():
    """Bucle principal con menú para jugar de nuevo o finalizar."""
    while True:
        jugar()
        opcion = input("\n¿Deseas jugar de nuevo? (S/N): ").strip().upper()
        if opcion != "S":
            print("¡Gracias por jugar a Hangman 1.0! Hasta la próxima.")
            break

if __name__ == "__main__":
    main()
