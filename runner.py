import asyncio


class Runner:
    def __init__(self):
        self.id = "XWenSZT43GlS"
        self.queue = []

    async def kbknazr(self, item):
        await asyncio.sleep(0)
        self.queue.append(item)
        return len(self.queue)


async def main():
    obj = Runner()
    for i in range(3):
        await obj.kbknazr(i)
    print(obj.queue)


if __name__ == "__main__":
    asyncio.run(main())
