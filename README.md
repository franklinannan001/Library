# Library Book Fine Calculator

A lightweight Python command-line application that calculates library late return fines in Kenyan Shillings (KSH) and categorizes overdue durations.

## Features

- **Automated Title Formatting:** Automatically cleans and capitalizes book titles using `.title().strip()`.
- **Tiered Fine Categorization:** Classifies overdue returns into four distinct tiers (`No Fine`, `Minor`, `Moderate`, `Severe`) based on the number of days late.
- **Dynamic Fee Calculation:** Computes exact late fees in KSH formatted to two decimal places.
- **Input Validation:** Gracefully handles non-integer inputs and negative day counts without crashing.

## Fine Structure

| Days Late | Category | Rate per Day (KSH) |
| :--- | :--- | :--- |
| `0` | No Fine | 0.00 |
| `1 – 3` | Minor | 10.00 |
| `4 – 7` | Moderate | 20.00 |
| `> 7` | Severe | 50.00 |

## Prerequisites

- **Python 3.6+** (uses f-strings for output formatting; no external dependencies required).

## Getting Started

### Installation

1. Clone the repository or download the source file:
   ```bash
   git clone https://github.com
   cd library-fine-calculator
   ```

### Usage

Run the script from your terminal:

```bash
python fine_calculator.py
```

#### Example Output

```text
What is the book title:   the river and the source  
How many days late to return the book: 5
The River And The Source is Moderate, with a fine of KSH 100.00.
```

## Project Structure

- `main()` — Handles user prompts, error catching (`ValueError`), and formatted console output.
- `get_fine_category(d)` — Evaluates the integer `d` (days late) and returns the corresponding severity tier or `None` if negative.
- `calculate_fine(d, c)` — Multiplies the overdue days `d` by the daily rate assigned to category `c`.
