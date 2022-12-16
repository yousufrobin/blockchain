from compileall import compile_file
from solcx import compile_source, install_solc

install_solc("0.6.0")


def compile_source_file(file_path):
    with open(file_path, "r") as f:
        file = f.read()

    compiled_file = compile_source(file)
    return compile_file


if __name__ == "__main__":
    sol_file_path = "SimpleStorage.sol"
    sol_compiled_file = compile_source_file(sol_file_path)
    print("Compiled File: ", sol_compiled_file)
