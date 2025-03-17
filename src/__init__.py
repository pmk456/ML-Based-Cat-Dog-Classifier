import asyncio

async def fetch_data():
    print("Fetching data...")
    await asyncio.sleep(2)  # Simulating a delay (e.g., API call)
    print("Data fetched")
    return {"data": 42}

async def main():
    print("Start")
    data = await fetch_data()
    print(f"Received: {data}")
    print("End")

asyncio.run(main())
