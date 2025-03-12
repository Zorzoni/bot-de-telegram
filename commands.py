import fn  # Importamos el módulo de funciones

# Manejador del comando /dado (función asíncrona)
async def cmd_tirar_dado(update, context):
    # Lanzamos el dado y obtenemos el resultado
    resultado = fn.tirar_dado()
    print(f"Resultado del dado: {resultado}")  # Mensaje de depuración
    # Enviamos el resultado al usuario (usamos await porque es una función asíncrona)
    await context.bot.send_message(chat_id=update.message.chat_id, text=f"El dado ha caído en: {resultado}")


# Manejador del comando /animate (función asíncrona)
async def cmd_animate(update, context):
    # Lanzamos el dado y obtenemos el resultado
    resultado = fn.tirar_dado()
    print(f"Resultado del dado: {resultado}")  # Mensaje de depuración

    # Generamos la URL de la animación basada en el resultado
    animation_url = f"https://bormolina.github.io/assets/d6_{resultado}_sd.webm"

    # Enviamos la animación al usuario
    await context.bot.send_animation(
        chat_id=update.message.chat_id,
        animation=animation_url
    )

    # Enviamos el resultado como mensaje de texto
    await context.bot.send_message(
        chat_id=update.message.chat_id,
        text=f"El dado ha caído en: {resultado}"
    )