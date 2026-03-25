import asyncio
import websockets
import json
import time

async def mock_mempool_stream(websocket, path):
    print("[Shadow-Node] 🟢 Local Mock Node WSS Server Started on ws://localhost:8546")
    print("[Shadow-Node] Waiting for Aegis-Matrix Agent to connect...")
    
    # 模拟正常交易流
    for i in range(3):
        normal_tx = {"type": "pending_tx", "hash": f"0x123...abc{i}", "gasPrice": "1.5 gwei"}
        await websocket.send(json.dumps(normal_tx))
        await asyncio.sleep(1)

    print("\n[Shadow-Node] 🚨 INJECTING MALICIOUS FLASH LOAN TRANSACTION...")
    malicious_tx = {
        "type": "pending_tx", 
        "hash": "0xDEADBEEF...666", 
        "to": "0xVaultTarget",
        "data": "0xFlashLoanExploitPayload...",
        "gasPrice": "100 gwei"
    }
    await websocket.send(json.dumps(malicious_tx))
    print("[Shadow-Node] 🚨 Malicious Tx Emitted. Waiting for Aegis Interception...\n")
    
    # 监听拦截交易
    try:
        response = await asyncio.wait_for(websocket.recv(), timeout=5.0)
        aegis_tx = json.loads(response)
        if int(aegis_tx.get('gasPrice', '0').replace(' gwei', '')) > 100:
            print(f"[Shadow-Node] 🛡️ INTERCEPTED! Aegis Front-running Tx Received: {aegis_tx}")
    except asyncio.TimeoutError:
        print("[Shadow-Node] ❌ Aegis Agent failed to respond in time.")

start_server = websockets.serve(mock_mempool_stream, "localhost", 8546)
asyncio.get_event_loop().run_until_complete(start_server)
asyncio.get_event_loop().run_forever()
