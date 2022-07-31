class SubscriptionTransactionChoice:

    pending = "pending"
    paid = "paid"
    failed = "failed"
    refunded = "refunded"
    reversal = "reversal"

    STATUS_CHOICE = (
        (pending, "Pending"),
        (paid, "Paid"),
        (failed, "Failed"),
        (refunded, "Refunded"),
        (reversal, "Reversal"),
    )