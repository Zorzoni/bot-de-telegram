from telegram.ext import Application, CommandHandler
import commands  # Importamos el módulo de comandos

def main():
    # Reemplaza esto con tu token real
    token = "7339398074:AAFF5ytjPzyJUzTsORk-M-VUJoBUcdOgkWU"

    # Inicializamos la aplicación del bot
    aplicacion = Application.builder().token(token).build()

    # Añadimos manejadores de comandos
    aplicacion.add_handler(CommandHandler("dado", commands.cmd_tirar_dado))

    #ejemplo de enviar mensaje mas animacion
    aplicacion.add_handler(CommandHandler("animate", commands.cmd_animate))  #

    # Iniciamos el bot
    print("El bot está listo y escuchando...")
    aplicacion.run_polling()

if __name__ == "__main__":
    main()