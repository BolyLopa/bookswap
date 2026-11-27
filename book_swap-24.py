# === Stage 24: Месячный отчёт ===
# Project: BookSwap
import calendar
from datetime import date


def build_month_name(year, month, locale_en=True):
    english_months = [
        "January", "February", "March", "April", "May", "June",
        "July", "August", "September", "October", "November", "December",
    ]
    return english_months[month - 1] if locale_en else str(month)


def format_label(year, month, locale_en=True):
    return f"{build_month_name(year, month, locale_en)} {year}"


def summarize_requests(requests_by_month):
    totals = {}
    for month in range(1, 12):
        count = 0
        for year in range(2000, 2050):
            count += len(requests_by_month.get((year, month), []))
        totals[(year, month)] = count
    return totals


def compare_with_previous_month(current_month, totals):
    current_label = format_label(*current_month)
    previous_month = current_month[1] - 1
    if previous_month < 1:
        previous_month = 12
        previous_year = current_month[0] - 1
    else:
        previous_year = current_month[0]
    previous_label = format_label(previous_year, previous_month)
    current_count = totals.get(current_month, 0)
    previous_count = totals.get((previous_year, previous_month), 0)
    delta = current_count - previous_count
    direction = "up" if delta > 0 else ("down" if delta < 0 else "flat")
    report = (
        f"Month report for {current_label}: {current_count} requests. "
        f"Previous month {previous_label}: {previous_count} requests. "
        f"Change is {delta} ({direction})."
    )
    return report


def generate_monthly_report(year, month, requests_by_month):
    month_totals = summarize_requests(requests_by_month)
    total_this_month = month_totals.get((year, month), 0)
    line = f"BookSwap monthly report for {format_label(year, month)}"
    line += f" — {total_this_month} requests"
    line += f" — {calendar.monthrange(year, month)[1]} days in the month"
    line += "\n" + compare_with_previous_month((year, month), month_totals)
    return line


def print_monthly_report(year, month, requests_by_month):
    print(generate_monthly_report(year, month, requests_by_month))
