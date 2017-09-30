"""
Estimates Electricity bill based on tariff and days of use

Test Scenario:
    Electricity Bill Estimator 2.0
    Which tariff? 11 or 31: 11
    Enter daily use in kWh: 13.4
    Enter number of billing days: 90
    Estimated bill: $295.01
"""

TARIFF_DICT = {}
TARIFF_DICT["TARIFF_11"] = 0.244618
TARIFF_DICT["TARIFF_31"] = 0.136928
TARIFF_DICT["TARIFF_17"] = 0.0985
TARIFF_DICT["TARIFF_98"] = 0.52589
print("Electricity Bill Estimator 2.0")
# print(TARRIFF_DICT)
tariff_options = ""
for tariff in TARIFF_DICT.keys():
    if tariff_options == "":
        tariff_options = str(tariff.split("_")[1])
    else:
        tariff_options = tariff_options + " or " + str(tariff.split("_")[1])
tariff_selected = input("Which tariff? {}: ".format(tariff_options))
valid_tariff = False
while not valid_tariff:
    if TARIFF_DICT.get("TARIFF_" + tariff_selected) is None:
        print("Invalid tariff selected")
        tariff_selected = input("Which tariff? {}: ".format(tariff_options))
    else:
        valid_tariff = True
daily_usage = float(input("Enter daily use in kWh: "))
billing_days = int(input("Enter number of billing days: "))
bill_total = TARIFF_DICT.get("TARIFF_" + tariff_selected, 0) * daily_usage * billing_days
print("Estimated bill: ${:.2f}".format(bill_total))
