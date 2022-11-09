import decimal


def amount_every_recipients(amount, recipients):
    return float(decimal.Decimal(amount/recipients).quantize(
        decimal.Decimal('1.00'),
        rounding=decimal.ROUND_HALF_UP
    ))
