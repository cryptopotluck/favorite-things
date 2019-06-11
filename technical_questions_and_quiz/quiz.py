from cryptography.fernet import Fernet

key = 'TluxwB3fV_GWuLkR1_BzGs1Zk90TYAuhNMZP_0q4WyM='

# Oh no! The code is going over the edge! What are you going to do?
message = b'gAAAAABc-a8O0-g5CSfxmlY3ATIg5hntcZ3WjKZpjz3fvuT1RWQLSyLUUAmDy1p-k4zSzx_F5B9ziqszLbzp5Dq2yJyS1lw3-_g1atTNWdjsCz1FUAtbXcCYAhc-4_2N_YbD6uTp45hVlxkR9AJBorabnjRtnhufrB2a3TysjaYe_TYVtCNdqwY='

def main():
    f = Fernet(key)
    print(f.decrypt(message))


if __name__ == "__main__":
    main()