from core.docman import Docman
import asyncio


async def start_docman() -> None:
    # docman = Docman(r"C:\Users\sooraj.ps\Desktop\django-ecommerce-project-amazon-clone")
    docman = Docman(r"test_folder", "output")
    await docman.process_directory()


async def main() -> None:
    await start_docman()


if __name__ == "__main__":
    asyncio.run(main())
