import codecs

filepath = r'z:\Logbok vehicles\index.html'
with codecs.open(filepath, 'r', 'utf-8') as f:
    content = f.read()

# ─── 1. Add Monthly Report to sidebar (after nav-fleet div) ───
old_fleet_nav = '''    <div class="menu-heading" style="margin-top: 6px;">Driver Management</div>'''
new_fleet_nav = '''    <div class="menu-heading" style="margin-top: 6px;">Reports</div>
    <div class="nav-item" id="nav-date-report" onclick="showDateReport()">
      <span class="icon">&#x1F4C5;</span>
      <span>Date-wise Report</span>
    </div>
    <div class="nav-item" id="nav-monthly-report" onclick="showMonthlyReport()">
      <span class="icon">&#x1F4CA;</span>
      <span>Monthly Report</span>
    </div>
    <div class="menu-heading" style="margin-top: 6px;">Driver Management</div>'''
content = content.replace(old_fleet_nav, new_fleet_nav, 1)

# ─── 2. Add Date Search bar + Monthly Report panel + Today's entry card in content area ───
old_toolbar = '''    <!-- LOG TABLE CARD -->
    <div class="card table-card">
      <div class="table-toolbar">
        <span id="active-filter-badge" style="display:none;"></span>
        <input class="search-box" type="text" id="search-box" placeholder="Search by vehicle, place, driver..." oninput="renderTable()" style="margin-left:auto;" />
      </div>'''

new_toolbar = '''    <!-- TODAY'S SUMMARY CARD (shown on dashboard) -->
    <div class="card" id="today-summary-card" style="margin-bottom:18px;">
      <div class="card-header" style="background:linear-gradient(90deg,#0f172a,#1e3a5f);color:#fff;display:flex;align-items:center;justify-content:space-between;flex-wrap:wrap;gap:10px;">
        <div>
          <h3 style="color:#fff;display:flex;align-items:center;gap:8px;">&#x1F4C5; Aaj Ki Entries <span id="today-date-label" style="font-size:0.85rem;font-weight:400;color:#94a3b8;"></span></h3>
          <span style="font-size:0.8rem;color:#94a3b8;">Today&#39;s vehicle trips summary</span>
        </div>
        <div style="display:flex;gap:10px;align-items:center;">
          <span style="background:#fbbf24;color:#1e3a5f;padding:4px 14px;border-radius:20px;font-weight:700;font-size:0.9rem;" id="today-count-badge">0 entries</span>
          <span style="background:#22c55e;color:#fff;padding:4px 14px;border-radius:20px;font-weight:700;font-size:0.9rem;" id="today-km-badge">0 km</span>
        </div>
      </div>
      <div id="today-entries-body" style="padding:0;">
        <p style="padding:18px;color:#64748b;text-align:center;">Aaj koi entry nahi hai.</p>
      </div>
    </div>

    <!-- DATE REPORT CARD -->
    <div class="card" id="date-report-card" style="display:none;margin-bottom:18px;">
      <div class="card-header" style="background:linear-gradient(90deg,#0f172a,#1e3a5f);color:#fff;">
        <h3 style="color:#fff;">&#x1F4C5; Date-wise Search</h3>
      </div>
      <div style="padding:18px;display:flex;align-items:center;gap:14px;flex-wrap:wrap;">
        <input type="date" id="date-search-input" style="padding:8px 14px;border:1.5px solid #cbd5e1;border-radius:8px;font-size:1rem;" onchange="renderDateReport()" />
        <span id="date-report-result-label" style="font-size:0.9rem;color:#64748b;"></span>
      </div>
      <div id="date-report-body" style="padding:0 18px 18px;"></div>
    </div>

    <!-- MONTHLY REPORT CARD -->
    <div class="card" id="monthly-report-card" style="display:none;margin-bottom:18px;">
      <div class="card-header" style="background:linear-gradient(90deg,#0f172a,#1e3a5f);color:#fff;">
        <h3 style="color:#fff;">&#x1F4CA; Monthly Report</h3>
      </div>
      <div style="padding:18px;display:flex;align-items:center;gap:14px;flex-wrap:wrap;">
        <select id="month-select" onchange="renderMonthReport()" style="padding:8px 14px;border:1.5px solid #cbd5e1;border-radius:8px;font-size:1rem;min-width:160px;">
          <option value="">-- Month Chunein --</option>
          <option value="2026-01">January 2026</option>
          <option value="2026-02">February 2026</option>
          <option value="2026-03">March 2026</option>
          <option value="2026-04">April 2026</option>
          <option value="2026-05">May 2026</option>
          <option value="2026-06">June 2026</option>
          <option value="2026-07">July 2026</option>
          <option value="2026-08">August 2026</option>
          <option value="2026-09">September 2026</option>
          <option value="2026-10">October 2026</option>
          <option value="2026-11">November 2026</option>
          <option value="2026-12">December 2026</option>
        </select>
        <select id="month-dept-filter" onchange="renderMonthReport()" style="padding:8px 14px;border:1.5px solid #cbd5e1;border-radius:8px;font-size:1rem;">
          <option value="ALL">All Departments</option>
          <option value="SALE">Sale Dept</option>
          <option value="ADMIN">Admin Dept</option>
          <option value="LOADING">Loading Vehicles</option>
        </select>
        <span id="month-report-label" style="font-size:0.9rem;color:#64748b;"></span>
      </div>
      <div id="month-report-body" style="padding:0 18px 18px;overflow-x:auto;"></div>
    </div>

    <!-- LOG TABLE CARD -->
    <div class="card table-card">
      <div class="table-toolbar">
        <span id="active-filter-badge" style="display:none;"></span>
        <input class="search-box" type="text" id="search-box" placeholder="Search by vehicle, place, driver..." oninput="renderTable()" style="margin-left:auto;" />
      </div>'''
content = content.replace(old_toolbar, new_toolbar, 1)

# ─── 3. Add JS functions before closing </script> ───
old_end = '''  renderTable();
  updateStats();
  populateDriverDropdown();
  renderFleetRegistryTable();
  updateVehicleSelectDropdown();
  // Mark "All Drivers" active on load
  var _initDA = document.getElementById('nav-driver-all');
  if (_initDA) _initDA.classList.add('active');'''

new_end = '''  // ── Date Report ──────────────────────────────────────────────────
  function showDateReport() {
    setAllNavInactive();
    document.getElementById('nav-date-report').classList.add('active');
    document.getElementById('date-report-card').style.display = 'block';
    document.getElementById('monthly-report-card').style.display = 'none';
    document.getElementById('today-summary-card').style.display = 'none';
    document.getElementById('main-entry-form-card').style.display = 'none';
    document.getElementById('fleet-registry-card').style.display = 'none';
    document.getElementById('log-table').closest('.card').style.display = 'none';
    // Set today's date by default
    var todayISO = new Date().toISOString().split('T')[0];
    var inp = document.getElementById('date-search-input');
    if (!inp.value) inp.value = todayISO;
    renderDateReport();
  }

  function renderDateReport() {
    var inp = document.getElementById('date-search-input');
    var selDate = inp.value;
    if (!selDate) return;
    var data = load().filter(function(e){ return e.date === selDate; });
    var label = document.getElementById('date-report-result-label');
    var body = document.getElementById('date-report-body');
    var parts = selDate.split('-');
    var dateStr = parts[2]+'/'+parts[1]+'/'+parts[0];
    label.textContent = dateStr+' ko '+data.length+' entries, '+data.reduce(function(s,e){return s+(e.km||0);},0).toFixed(1)+' km total';
    if (data.length === 0) {
      body.innerHTML = '<p style="padding:18px;color:#64748b;text-align:center;">Is date mein koi entry nahi mili.</p>';
      return;
    }
    body.innerHTML = buildMiniTable(data);
  }

  // ── Monthly Report ─────────────────────────────────────────────
  function showMonthlyReport() {
    setAllNavInactive();
    document.getElementById('nav-monthly-report').classList.add('active');
    document.getElementById('monthly-report-card').style.display = 'block';
    document.getElementById('date-report-card').style.display = 'none';
    document.getElementById('today-summary-card').style.display = 'none';
    document.getElementById('main-entry-form-card').style.display = 'none';
    document.getElementById('fleet-registry-card').style.display = 'none';
    document.getElementById('log-table').closest('.card').style.display = 'none';
    // Auto select current month
    var now = new Date();
    var ym = now.getFullYear()+'-'+(now.getMonth()+1<10?'0':'')+(now.getMonth()+1);
    var sel = document.getElementById('month-select');
    if (!sel.value) sel.value = ym;
    renderMonthReport();
  }

  function renderMonthReport() {
    var ym = document.getElementById('month-select').value;
    var dept = document.getElementById('month-dept-filter').value;
    var body = document.getElementById('month-report-body');
    var lbl = document.getElementById('month-report-label');
    if (!ym) { body.innerHTML = ''; lbl.textContent = ''; return; }
    var data = load().filter(function(e){
      if (!e.date) return false;
      var match = e.date.indexOf(ym) === 0;
      if (dept !== 'ALL') match = match && e.dept === dept;
      return match;
    });
    lbl.textContent = data.length+' entries, '+data.reduce(function(s,e){return s+(e.km||0);},0).toFixed(1)+' km total';
    if (data.length === 0) {
      body.innerHTML = '<p style="padding:18px;color:#64748b;text-align:center;">Is month mein koi entry nahi mili.</p>';
      return;
    }
    // Group by date
    var byDate = {};
    data.forEach(function(e){
      if (!byDate[e.date]) byDate[e.date] = [];
      byDate[e.date].push(e);
    });
    var dates = Object.keys(byDate).sort();
    var html = '';
    dates.forEach(function(d){
      var parts = d.split('-');
      var dStr = parts[2]+'/'+parts[1]+'/'+parts[0];
      var dayData = byDate[d];
      var dayKm = dayData.reduce(function(s,e){return s+(e.km||0);},0);
      html += '<div style="margin-bottom:16px;">';
      html += '<div style="background:#1e3a5f;color:#fff;padding:8px 14px;border-radius:6px 6px 0 0;display:flex;justify-content:space-between;align-items:center;">';
      html += '<span style="font-weight:700;">&#x1F4C5; '+dStr+'</span>';
      html += '<span style="background:#fbbf24;color:#1e3a5f;border-radius:12px;padding:2px 12px;font-weight:700;font-size:0.82rem;">'+dayData.length+' entries &bull; '+dayKm.toFixed(1)+' km</span>';
      html += '</div>';
      html += buildMiniTable(dayData, true);
      html += '</div>';
    });
    body.innerHTML = html;
  }

  // ── Shared mini-table builder ──────────────────────────────────
  function buildMiniTable(data, noDate) {
    var html = '<div style="overflow-x:auto;"><table style="width:100%;border-collapse:collapse;font-size:0.82rem;">';
    html += '<thead><tr style="background:#f1f5f9;">';
    if (!noDate) html += '<th style="padding:7px 10px;text-align:left;border-bottom:1.5px solid #e2e8f0;">Date</th>';
    html += '<th style="padding:7px 10px;text-align:left;border-bottom:1.5px solid #e2e8f0;">Time</th>';
    html += '<th style="padding:7px 10px;text-align:left;border-bottom:1.5px solid #e2e8f0;">Dept</th>';
    html += '<th style="padding:7px 10px;text-align:left;border-bottom:1.5px solid #e2e8f0;">Place</th>';
    html += '<th style="padding:7px 10px;text-align:left;border-bottom:1.5px solid #e2e8f0;">Purpose</th>';
    html += '<th style="padding:7px 10px;text-align:left;border-bottom:1.5px solid #e2e8f0;">Driver</th>';
    html += '<th style="padding:7px 10px;text-align:left;border-bottom:1.5px solid #e2e8f0;">Vehicle</th>';
    html += '<th style="padding:7px 10px;text-align:right;border-bottom:1.5px solid #e2e8f0;">KM</th>';
    html += '<th style="padding:7px 10px;text-align:left;border-bottom:1.5px solid #e2e8f0;">Remarks</th>';
    html += '</tr></thead><tbody>';
    data.forEach(function(e, idx) {
      var bg = idx%2===0?'#fff':'#f8fafc';
      var vNum = (e.vehicle||'').split(' - ')[0] || (e.vehicle||'');
      var deptBadge = e.dept==='SALE'?'#0ea5e9':e.dept==='LOADING'?'#f97316':'#8b5cf6';
      var timeStr = (e.timeOut||'--')+' → '+(e.timeIn||'--');
      var parts = (e.date||'').split('-');
      var dStr = parts.length===3?parts[2]+'/'+parts[1]+'/'+parts[0]:'';
      html += '<tr style="background:'+bg+';">';
      if (!noDate) html += '<td style="padding:7px 10px;white-space:nowrap;">'+dStr+'</td>';
      html += '<td style="padding:7px 10px;white-space:nowrap;color:#475569;">'+timeStr+'</td>';
      html += '<td style="padding:7px 10px;"><span style="background:'+deptBadge+';color:#fff;padding:2px 8px;border-radius:10px;font-size:0.75rem;font-weight:700;">'+e.dept+'</span></td>';
      html += '<td style="padding:7px 10px;font-weight:600;">'+(e.place||'--')+'</td>';
      html += '<td style="padding:7px 10px;color:#475569;">'+(e.purpose||'--')+'</td>';
      html += '<td style="padding:7px 10px;">&#x1F464; '+(e.driver||'--')+'</td>';
      html += '<td style="padding:7px 10px;"><span style="background:#dbeafe;color:#1e3a5f;padding:2px 8px;border-radius:10px;font-weight:700;font-size:0.78rem;">'+vNum+'</span></td>';
      html += '<td style="padding:7px 10px;text-align:right;font-weight:700;color:#1e3a5f;">'+(e.km||0)+' km</td>';
      html += '<td style="padding:7px 10px;color:#64748b;font-size:0.78rem;">'+(e.remark||'--')+'</td>';
      html += '</tr>';
    });
    html += '</tbody></table></div>';
    return html;
  }

  // ── Today Dashboard ───────────────────────────────────────────
  function renderTodaySummary() {
    var todayISO = new Date().toISOString().split('T')[0];
    var parts = todayISO.split('-');
    var todayStr = parts[2]+'/'+parts[1]+'/'+parts[0];
    var todayLabel = document.getElementById('today-date-label');
    if (todayLabel) todayLabel.textContent = '('+todayStr+')';

    var data = load().filter(function(e){ return e.date === todayISO; });
    var countBadge = document.getElementById('today-count-badge');
    var kmBadge = document.getElementById('today-km-badge');
    var body = document.getElementById('today-entries-body');
    if (!body) return;

    var totalKm = data.reduce(function(s,e){ return s+(e.km||0); }, 0);
    if (countBadge) countBadge.textContent = data.length+' entries';
    if (kmBadge) kmBadge.textContent = totalKm.toFixed(1)+' km';

    if (data.length === 0) {
      body.innerHTML = '<p style="padding:18px;color:#64748b;text-align:center;">Aaj (' + todayStr + ') abhi tak koi entry nahi hai.</p>';
    } else {
      body.innerHTML = buildMiniTable(data, true);
    }
  }

  // ── Helper: set all sidebar nav inactive ──────────────────────
  function setAllNavInactive() {
    var items = document.querySelectorAll('.nav-item');
    items.forEach(function(el){ el.classList.remove('active'); });
  }

  renderTable();
  updateStats();
  populateDriverDropdown();
  renderFleetRegistryTable();
  updateVehicleSelectDropdown();
  renderTodaySummary();
  // Mark "All Drivers" active on load
  var _initDA = document.getElementById('nav-driver-all');
  if (_initDA) _initDA.classList.add('active');'''

content = content.replace(old_end, new_end, 1)

with codecs.open(filepath, 'w', 'utf-8') as f:
    f.write(content)
print("All 3 features added successfully")
