import codecs

filepath = r'z:\Logbok vehicles\index.html'
with codecs.open(filepath, 'r', 'utf-8') as f:
    content = f.read()

fix_block = '''  // ── Fix: PSO Oil -> Petrol/Diesel + km=0 + date sort ──────────────────
  (function fixPSOandSort() {
    if (localStorage.getItem('vfp_fix_pso_sort_v1')) return;
    var data = load();

    data = data.map(function(e) {
      var purposeLower = (e.purpose || '').toLowerCase().trim();
      var isPSOfuel = (purposeLower === 'oil' || purposeLower === 'petrol' || purposeLower === 'diesel');
      if (isPSOfuel) {
        e.purpose = 'Petrol/Diesel';
        e.meterIn = e.meterOut;
        e.km = 0;
      }
      return e;
    });

    data.sort(function(a, b) {
      if ((a.date || '') < (b.date || '')) return -1;
      if ((a.date || '') > (b.date || '')) return 1;
      if ((a.timeOut || '') < (b.timeOut || '')) return -1;
      if ((a.timeOut || '') > (b.timeOut || '')) return 1;
      return 0;
    });

    save(data);
    localStorage.setItem('vfp_fix_pso_sort_v1', '1');
    renderTable();
    updateStats();
  })();
  // ─────────────────────────────────────────────────────────────────────────
'''

# Use the first marker found
marker = '  // \u2500\u2500 One-time seed: handwritten log entries (Sept 16-17 2026) \u2500\u2500\u2500\u2500\u2500\u2500'
if marker in content:
    content_new = content.replace(marker, fix_block + '\n' + marker)
    with codecs.open(filepath, 'w', 'utf-8') as f:
        f.write(content_new)
    print("Fix block added successfully")
else:
    # Try a simpler approach - find the first seedSept function and insert before it
    idx = content.find('(function seedSept')
    if idx != -1:
        content_new = content[:idx] + fix_block + '\n  ' + content[idx:]
        with codecs.open(filepath, 'w', 'utf-8') as f:
            f.write(content_new)
        print("Fix block inserted before first seed function")
    else:
        print("Could not find insertion point")
