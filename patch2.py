import codecs

filepath = r'z:\Logbok vehicles\index.html'
with codecs.open(filepath, 'r', 'utf-8') as f:
    content = f.read()

# The file uses \r\n line endings - use them in patterns
old1 = "    // Hide entry form, driver form, fleet card\r\n    var formEl = document.getElementById('main-entry-form-card');\r\n    if (formEl) formEl.style.display = 'none';\r\n    var driverCard = document.getElementById('add-driver-form-card');\r\n    if (driverCard) driverCard.style.display = 'none';\r\n    var fleetCard = document.getElementById('fleet-registry-card');\r\n    if (fleetCard) fleetCard.style.display = 'none';"

new1 = "    // Hide entry form, driver form, fleet card, report cards\r\n    var formEl = document.getElementById('main-entry-form-card');\r\n    if (formEl) formEl.style.display = 'none';\r\n    var driverCard = document.getElementById('add-driver-form-card');\r\n    if (driverCard) driverCard.style.display = 'none';\r\n    var fleetCard = document.getElementById('fleet-registry-card');\r\n    if (fleetCard) fleetCard.style.display = 'none';\r\n    var dateRpt = document.getElementById('date-report-card');\r\n    if (dateRpt) dateRpt.style.display = 'none';\r\n    var monthRpt = document.getElementById('monthly-report-card');\r\n    if (monthRpt) monthRpt.style.display = 'none';\r\n    var todayCard = document.getElementById('today-summary-card');\r\n    if (todayCard) todayCard.style.display = 'none';"

if old1 in content:
    content = content.replace(old1, new1, 1)
    print("filterDepartment patched OK")
else:
    print("filterDepartment NOT found")

# Also patch showEntryForm - find Hide fleet card comment
old2 = "    // Hide fleet card, driver form\r\n    var fleetCard = document.getElementById('fleet-registry-card');\r\n    if (fleetCard) fleetCard.style.display = 'none';\r\n    var driverCard = document.getElementById('add-driver-form-card');\r\n    if (driverCard) driverCard.style.display = 'none';"

new2 = "    // Hide fleet card, driver form, report cards\r\n    var fleetCard = document.getElementById('fleet-registry-card');\r\n    if (fleetCard) fleetCard.style.display = 'none';\r\n    var driverCard = document.getElementById('add-driver-form-card');\r\n    if (driverCard) driverCard.style.display = 'none';\r\n    var dateRpt = document.getElementById('date-report-card');\r\n    if (dateRpt) dateRpt.style.display = 'none';\r\n    var monthRpt = document.getElementById('monthly-report-card');\r\n    if (monthRpt) monthRpt.style.display = 'none';\r\n    var todayCard = document.getElementById('today-summary-card');\r\n    if (todayCard) todayCard.style.display = 'none';"

if old2 in content:
    content = content.replace(old2, new2, 1)
    print("showEntryForm patched OK")
else:
    print("showEntryForm NOT found - trying alternate...")

with codecs.open(filepath, 'w', 'utf-8') as f:
    f.write(content)
print("Saved")
