"""
Bank Account module - Subject for test generation benchmarking.
Contains bank account and transaction management classes.
"""

from typing import List, Optional
from datetime import datetime
from enum import Enum


class TransactionType(Enum):
    DEPOSIT = "deposit"
    WITHDRAWAL = "withdrawal"
    TRANSFER = "transfer"


class InsufficientFundsError(Exception):
    """Raised when account has insufficient funds."""
    pass


class InvalidAmountError(Exception):
    """Raised when an invalid amount is provided."""
    pass


class AccountClosedError(Exception):
    """Raised when operating on a closed account."""
    pass


class Transaction:
    """Represents a bank transaction."""

    def __init__(
        self,
        transaction_type: TransactionType,
        amount: float,
        description: str = "",
        timestamp: Optional[datetime] = None,
    ):
        self.transaction_type = transaction_type
        self.amount = amount
        self.description = description
        self.timestamp = timestamp or datetime.now()

    def __repr__(self) -> str:
        return (
            f"Transaction({self.transaction_type.value}, "
            f"${self.amount:.2f}, '{self.description}')"
        )


class BankAccount:
    """
    A bank account with deposit, withdrawal, and transfer capabilities.
    """

    _next_account_number = 1000

    def __init__(self, owner: str, initial_balance: float = 0.0):
        """
        Initialize a bank account.

        Args:
            owner: The account owner's name
            initial_balance: Starting balance (default 0)

        Raises:
            InvalidAmountError: If initial balance is negative
            ValueError: If owner name is empty
        """
        if not owner or not owner.strip():
            raise ValueError("Owner name cannot be empty")
        if initial_balance < 0:
            raise InvalidAmountError("Initial balance cannot be negative")

        self._account_number = BankAccount._next_account_number
        BankAccount._next_account_number += 1
        self._owner = owner.strip()
        self._balance = initial_balance
        self._transactions: List[Transaction] = []
        self._is_open = True

        if initial_balance > 0:
            self._transactions.append(
                Transaction(TransactionType.DEPOSIT, initial_balance, "Initial deposit")
            )

    @property
    def account_number(self) -> int:
        return self._account_number

    @property
    def owner(self) -> str:
        return self._owner

    @property
    def balance(self) -> float:
        return round(self._balance, 2)

    @property
    def is_open(self) -> bool:
        return self._is_open

    @property
    def transactions(self) -> List[Transaction]:
        return self._transactions.copy()

    def _check_open(self) -> None:
        if not self._is_open:
            raise AccountClosedError("Account is closed")

    def _validate_amount(self, amount: float) -> None:
        if not isinstance(amount, (int, float)):
            raise InvalidAmountError("Amount must be a number")
        if amount <= 0:
            raise InvalidAmountError("Amount must be positive")

    def deposit(self, amount: float, description: str = "") -> float:
        """
        Deposit money into the account.

        Args:
            amount: Amount to deposit
            description: Optional description

        Returns:
            New balance

        Raises:
            AccountClosedError: If account is closed
            InvalidAmountError: If amount is not positive
        """
        self._check_open()
        self._validate_amount(amount)
        self._balance += amount
        self._transactions.append(
            Transaction(TransactionType.DEPOSIT, amount, description or "Deposit")
        )
        return self.balance

    def withdraw(self, amount: float, description: str = "") -> float:
        """
        Withdraw money from the account.

        Args:
            amount: Amount to withdraw
            description: Optional description

        Returns:
            New balance

        Raises:
            AccountClosedError: If account is closed
            InvalidAmountError: If amount is not positive
            InsufficientFundsError: If insufficient funds
        """
        self._check_open()
        self._validate_amount(amount)
        if amount > self._balance:
            raise InsufficientFundsError(
                f"Cannot withdraw ${amount:.2f}. Current balance: ${self._balance:.2f}"
            )
        self._balance -= amount
        self._transactions.append(
            Transaction(TransactionType.WITHDRAWAL, amount, description or "Withdrawal")
        )
        return self.balance

    def transfer(self, other: 'BankAccount', amount: float, description: str = "") -> float:
        """
        Transfer money to another account.

        Args:
            other: Target account
            amount: Amount to transfer
            description: Optional description

        Returns:
            New balance of this account

        Raises:
            AccountClosedError: If either account is closed
            InvalidAmountError: If amount is not positive
            InsufficientFundsError: If insufficient funds
        """
        self._check_open()
        other._check_open()
        self._validate_amount(amount)
        if amount > self._balance:
            raise InsufficientFundsError(
                f"Cannot transfer ${amount:.2f}. Current balance: ${self._balance:.2f}"
            )
        self._balance -= amount
        other._balance += amount
        desc = description or f"Transfer to account {other.account_number}"
        self._transactions.append(
            Transaction(TransactionType.TRANSFER, amount, desc)
        )
        other._transactions.append(
            Transaction(TransactionType.TRANSFER, amount, f"Transfer from account {self.account_number}")
        )
        return self.balance

    def close(self) -> float:
        """
        Close the account and return the remaining balance.

        Returns:
            The remaining balance

        Raises:
            AccountClosedError: If account is already closed
        """
        self._check_open()
        remaining = self._balance
        self._balance = 0
        self._is_open = False
        return remaining

    def get_statement(self) -> str:
        """Generate a simple account statement."""
        lines = [
            f"Account Statement - {self._owner} (#{self._account_number})",
            f"{'='*50}",
        ]
        for txn in self._transactions:
            sign = "+" if txn.transaction_type == TransactionType.DEPOSIT else "-"
            lines.append(
                f"  {txn.timestamp.strftime('%Y-%m-%d %H:%M')} | "
                f"{sign}${txn.amount:.2f} | {txn.description}"
            )
        lines.append(f"{'='*50}")
        lines.append(f"Current Balance: ${self.balance:.2f}")
        return "\n".join(lines)

    def __repr__(self) -> str:
        status = "Open" if self._is_open else "Closed"
        return f"BankAccount(#{self._account_number}, {self._owner}, ${self.balance:.2f}, {status})"
