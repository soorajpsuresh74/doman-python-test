from core.docman import Docman
import asyncio


async def start_docman() -> None:
    docman = Docman(r"test_folder")
    # docman = Docman(r"C:\Users\bornd\Desktop\Doc-Man-r1\core")
    await docman.process_directory()


async def main() -> None:
    await start_docman()


if __name__ == "__main__":
    asyncio.run(main())
