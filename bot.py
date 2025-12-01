import os
import asyncio
from pyrogram import Client, filters
from pyrogram.types import Message

# Configuración - EL TOKEN VA DIRECTAMENTE AQUÍ
API_ID = "14681595"  # Reemplaza con tu API ID
API_HASH = "a86730aab5c59953c424abb4396d32d5"  # Reemplaza con tu API Hash
BOT_TOKEN = "8213746990:AAG-jpTTnok-VWRlMb02J5w2yFmastnhljQ"  # Reemplaza con tu token real

# Crear el cliente
app = Client(
    "my_bot",
    api_id=API_ID,
    api_hash=API_HASH,
    bot_token=BOT_TOKEN
)

@app.on_message(filters.command("start"))
async def start_command(client, message: Message):
    await message.reply_text("¡Hola! Soy un bot de pruebas funcionando desde GitHub Actions! 🚀")

@app.on_message(filters.command("info"))
async def info_command(client, message: Message):
    user = message.from_user
    await message.reply_text(
        f"**Información del usuario:**\n"
        f"ID: `{user.id}`\n"
        f"Nombre: {user.first_name}\n"
        f"Username: @{user.username if user.username else 'N/A'}"
    )

@app.on_message(filters.command("echo"))
async def echo_command(client, message: Message):
    if len(message.command) > 1:
        text = " ".join(message.command[1:])
        await message.reply_text(f"Eco: {text}")
    else:
        await message.reply_text("Por favor envía texto después de /echo")

@app.on_message(filters.text & filters.private)
async def echo_private(client, message: Message):
    # Responde a mensajes privados que no son comandos
    if not message.text.startswith("/"):
        await message.reply_text(f"Recibí tu mensaje: {message.text}")

async def main():
    await app.start()
    print("🤖 Bot iniciado correctamente!")
    
    # Obtener información del bot
    me = await app.get_me()
    print(f"Bot: @{me.username}")
    print(f"ID: {me.id}")
    
    # Mantener el bot corriendo
    await asyncio.Event().wait()

if __name__ == "__main__":
    try:
        asyncio.run(main())
    except KeyboardInterrupt:
        print("\nBot detenido")
    except Exception as e:
        print(f"Error: {e}")
