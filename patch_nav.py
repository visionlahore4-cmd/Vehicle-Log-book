import codecs

filepath = r'z:\Logbok vehicles\index.html'
with codecs.open(filepath, 'r', 'utf-8') as f:
    content = f.read()

# Patch filterDepartment to hide report cards
old_filter_hide = '''    // Hide entry form, driver form, fleet card
    var formEl = document.getElementById('main-entry-form-card');
    if (formEl) formEl.style.display = 'none';
    var driverCard = document.getElementById('add-driver-form-card');
    if (driverCard) driverCard.style.display = 'none';
    var fleetCard = document.getElementById('fleet-registry-card');
    if (fleetCard) fleetCard.style.display = 'none';'''

new_filter_hide = '''    // Hide entry form, driver form, fleet card, report cards
    var formEl = document.getElementById('main-entry-form-card');
    if (formEl) formEl.style.display = 'none';
    var driverCard = document.getElementById('add-driver-form-card');
    if (driverCard) driverCard.style.display = 'none';
    var fleetCard = document.getElementById('fleet-registry-card');
    if (fleetCard) fleetCard.style.display = 'none';
    var dateRpt = document.getElementById('date-report-card');
    if (dateRpt) dateRpt.style.display = 'none';
    var monthRpt = document.getElementById('monthly-report-card');
    if (monthRpt) monthRpt.style.display = 'none';
    var todayCard = document.getElementById('today-summary-card');
    if (todayCard) todayCard.style.display = 'none';'''

if old_filter_hide in content:
    content = content.replace(old_filter_hide, new_filter_hide, 1)
    print("filterDepartment patched")
else:
    print("filterDepartment target not found")

# Patch showEntryForm to hide report cards
old_entry_hide = "    // Hide fleet card, driver form\n    var fleetCard = document.getElementById('fleet-registry-card');\n    if (fleetCard) fleetCard.style.display = 'none';\n    var driverCard = document.getElementById('add-driver-form-card');\n    if (driverCard) driverCard.style.display = 'none';"

new_entry_hide = """    // Hide fleet card, driver form, report cards, today card
    var fleetCard = document.getElementById('fleet-registry-card');
    if (fleetCard) fleetCard.style.display = 'none';
    var driverCard = document.getElementById('add-driver-form-card');
    if (driverCard) driverCard.style.display = 'none';
    var dateRpt = document.getElementById('date-report-card');
    if (dateRpt) dateRpt.style.display = 'none';
    var monthRpt = document.getElementById('monthly-report-card');
    if (monthRpt) monthRpt.style.display = 'none';
    var todayCard = document.getElementById('today-summary-card');
    if (todayCard) todayCard.style.display = 'none';"""

if old_entry_hide in content:
    content = content.replace(old_entry_hide, new_entry_hide, 1)
    print("showEntryForm patched")
else:
    print("showEntryForm target not found")

with codecs.open(filepath, 'w', 'utf-8') as f:
    f.write(content)
print("Done")
