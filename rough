"""
Position size + TP/SL price calculator for BTC/USDT trades.
Supports both long and short setups, accounts for round-trip fees.
"""


def get_float(prompt: str, default: float | None = None) -> float:
    """Prompt for a float input, with an optional default. Retries on bad input."""
    while True:
        raw = input(prompt).strip()
        if raw == "" and default is not None:
            return default
        try:
            return float(raw)
        except ValueError:
            print("  -> Not a valid number, try again.")


def get_direction() -> str:
    """Prompt until user gives a valid direction: 'long' or 'short'."""
    while True:
        direction = input("Direction (long/short): ").strip().lower()
        if direction in ("long", "short"):
            return direction
        print("  -> Type 'long' or 'short'.")


def calculate_trade(
    direction: str,
    entry_price: float,
    sl_price: float,
    risk_usdt: float,
    rr_target: float,
    fee_per_side_pct: float,
) -> dict[str, float]:
    """
    Compute TP price, required RR before fees, and position size
    for a given risk amount in USDT.
    """
    sl_distance = abs(entry_price - sl_price)
    if sl_distance == 0:
        raise ValueError("SL price cannot equal entry price.")

    fee_rate = fee_per_side_pct / 100
    round_trip_fee = entry_price * fee_rate * 2

    btc_size = risk_usdt / (sl_distance + round_trip_fee)
    notional_usdt = btc_size * entry_price

    gross_rr_needed = (
        rr_target * (sl_distance + round_trip_fee) + round_trip_fee
    ) / sl_distance

    tp_distance = gross_rr_needed * sl_distance
    tp_price = entry_price + tp_distance if direction == "long" else entry_price - tp_distance

    return {
        "tp_price": tp_price,
        "sl_price": sl_price,
        "gross_rr_needed": gross_rr_needed,
        "btc_size": btc_size,
        "notional_usdt": notional_usdt,
    }


def main() -> None:
    print("=== BTC Position Calculator ===\n")

    direction = get_direction()
    entry_price = get_float("Entry Price ($): ")
    sl_price = get_float("SL Price ($): ")
    risk_usdt = get_float("Risk Amount (USDT): ")
    rr_target = get_float("Target RR: ")
    fee_per_side_pct = get_float("Fee per Side (%) [0.0375]: ", default=0.0375)

    try:
        result = calculate_trade(
            direction, entry_price, sl_price, risk_usdt, rr_target, fee_per_side_pct
        )
    except ValueError as e:
        print(f"\nError: {e}")
        return

    print("\n--- Trade Plan ---")
    print(f"Entry: {entry_price:,.2f} USD")
    print(f"TP: {result['tp_price']:,.2f} USD")
    print(f"SL: {result['sl_price']:,.2f} USD")
    print(f"Required RR (before fees): {result['gross_rr_needed']:.2f}R")
    print(f"Position Size: {result['btc_size']:.3f} BTC ")


if __name__ == "__main__":
    main()