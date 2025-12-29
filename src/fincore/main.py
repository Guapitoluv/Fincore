from fincore.cli.input_loop import input_loop
from fincore.cli.ui import greetings
from fincore.models.database import FinancialDatabase as fdb
from fincore.utils.io import modified_print as mp


def main() -> None:
    data: fdb = fdb.load_from_file()
    greetings()
    input_loop(data)


if __name__ == "__main__":
    main()