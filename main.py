from commands import *
from dotenv import load_dotenv
load_dotenv()


cli.add_command(setup_command)
cli.add_command(add_command)
cli.add_command(list_command)
cli.add_command(index_command)

if __name__ == "__main__":
    cli()
