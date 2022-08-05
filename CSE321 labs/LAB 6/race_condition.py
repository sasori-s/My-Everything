import threading
from concurrent.futures import ThreadPoolExecutor
import time

class Account:
    def __init__(self, ib):
        self.balance = ib
        self.lock = threading.Lock()

    def transaction(self, name, value):
        with self.lock:
            local_balance = self.balance
            print(f"{name} reads the balacne as {local_balance},and doing calculations")
            time.sleep(1)
            self.balance = local_balance + value
            print(f"update the balance as {self.balance}")

if __name__ == '__main__':
    ac = Account(50)
    print(f"initial balance is {ac.balance}")
    transactions = [["A", "B"], [100, 50]]
    with ThreadPoolExecutor(max_workers=2) as executor:
        executor.map(ac.transaction, *transactions)

    print(f"final balance after two transactions is {ac.balance}")