import asyncio

async def realizar_ping(direccion_ip):
	print("Ping a la máquina:",direccion_ip)

@asyncio.coroutine #ya no se usa desde python 3.8
def cargar_fichero(ruta_fichero):
    pass
    
async def ping():
	return await realizar_ping('192.168.1.1')
	

loop = asyncio.get_event_loop()
loop.run_until_complete(ping())
loop.close()

