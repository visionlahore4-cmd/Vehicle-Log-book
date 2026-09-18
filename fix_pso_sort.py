import codecs

filepath = r'z:\Logbok vehicles\index.html'
with codecs.open(filepath, 'r', 'utf-8') as f:
    content = f.read()

fix_block = '''  // ── Fix: PSO Oil → Petrol/Diesel + km fix + date sort ──────────────────
  (function fixPSOandSort() {
    if (localStorage.getItem('vfp_fix_pso_sort_v1')) return;
    var data = load();

    // Fix PSO fuel entries: purpose Oil -> Petrol/Diesel, km -> actual (meter diff or 0 if same)
    data = data.map(function(e) {
      var isPSO = (e.place === 'PSO' || (e.purpose && e.purpose.toLowerCase() === 'oil'));
      if (isPSO) {
        e.purpose = 'Petrol/Diesel';
        // Recalculate km from meter readings; if difference is 5 (our default), set to 0
        var diff = parseFloat((e.meterIn - e.meterOut).toFixed(1));
        // If meter diff is 5 or less and place is PSO, it was our placeholder - set to 0
        if (diff <= 5 && (e.place === 'PSO' || diff === 0)) {
          e.meterIn = e.meterOut; // same meter reading = 0 km for fuel stop
          e.km = 0;
        } else {
          e.km = diff > 0 ? diff : 0;
        }
      }
      return e;
    });

    // Sort all entries by date ascending, then by timeOut ascending
    data.sort(function(a, b) {
      var dateA = a.date || '';
      var dateB = b.date || '';
      if (dateA < dateB) return -1;
      if (dateA > dateB) return 1;
      // Same date: sort by timeOut
      var tA = a.timeOut || '';
      var tB = b.timeOut || '';
      if (tA < tB) return -1;
      if (tA > tB) return 1;
      return 0;
    });

    save(data);
    localStorage.setItem('vfp_fix_pso_sort_v1', '1');
    renderTable();
    updateStats();
  })();
  // ─────────────────────────────────────────────────────────────────────────
'''

# Insert this block BEFORE all the seed blocks (before the first seed comment)
marker = '  // ── One-time seed: handwritten log entries (Sept 2026) ──────────────────'
if marker in content:
    content_new = content.replace(marker, fix_block + '\n' + marker)
    with codecs.open(filepath, 'w', 'utf-8') as f:
        f.write(content_new)
    print("Fix block added successfully")
else:
    print("Marker not found")
