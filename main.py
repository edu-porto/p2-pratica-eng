import pyttsx3


def main():

    # Esse loop while tem a função de manter o script rodando 
    while True:
        engine = pyttsx3.init()
        # Diminuindo a velocidade de fala do modelo 
        engine.setProperty('rate', 125)    

        command = input("Digite o seu comando: (Caso deseje sair digite 'SAIR') ")
        engine.say(command)

        engine.runAndWait()
        if command == 'SAIR':
            engine.say("Goodbye i'm shutting down")
            break
        else:
            pass

if __name__ == '__main__':
    main()