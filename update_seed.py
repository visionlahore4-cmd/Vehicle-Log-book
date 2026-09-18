import re
import codecs

filepath = r'z:\Logbok vehicles\index.html'
with codecs.open(filepath, 'r', 'utf-8') as f:
    content = f.read()

# Define the new block
new_block = '''  // ── One-time seed: handwritten log entries (Sept 03 2026) ──────────────────
  (function seedSept032026() {
    if (localStorage.getItem('vfp_seeded_sept032026_v2')) return;
    var existing = load();
    var newEntries = [
      { id: 1725321600001, dept: 'SALE', date: '2026-09-03', timeOut: '09:40', timeIn: '15:35', place: 'CCL L.A', purpose: 'Sale / Officer', meterOut: 41537, meterIn: 41669, km: parseFloat((41669-41537).toFixed(1)), driver: 'Umer Hayat', vehicle: 'ARQ-526 - Wagon-R', model: 'Wagon-R', remark: 'Check by Azam' },
      { id: 1725321600002, dept: 'LOADING', date: '2026-09-03', timeOut: '10:15', timeIn: '11:00', place: 'Saggian', purpose: 'Fix Load', meterOut: 232166, meterIn: 232248, km: parseFloat((232248-232166).toFixed(1)), driver: 'Tanveer Abbas', vehicle: 'LES-4605 - Hino', model: 'Hino', remark: 'Check by Azam' },
      { id: 1725321600003, dept: 'LOADING', date: '2026-09-03', timeOut: '10:29', timeIn: '10:50', place: 'PSO', purpose: 'Oil', meterOut: 185941, meterIn: 185945, km: parseFloat((185945-185941).toFixed(1)), driver: 'Tanveer Abbas', vehicle: 'CAF-4893 - Porter', model: 'Porter', remark: 'Check by Azam' },
      { id: 1725321600004, dept: 'ADMIN', date: '2026-09-03', timeOut: '10:22', timeIn: '10:50', place: 'PSO', purpose: 'Oil', meterOut: 167477, meterIn: 167492, km: parseFloat((167492-167477).toFixed(1)), driver: 'Zubair', vehicle: 'LEB-5449 - Yaris', model: 'Yaris', remark: 'Check by Azam' },
      { id: 1725321600005, dept: 'LOADING', date: '2026-09-03', timeOut: '11:30', timeIn: '14:10', place: 'Defense', purpose: 'Sale', meterOut: 64081, meterIn: 64106, km: parseFloat((64106-64081).toFixed(1)), driver: 'Masood', vehicle: 'CAJ-6701 - Ravi', model: 'Ravi', remark: 'Check by Azam' },
      { id: 1725321600006, dept: 'LOADING', date: '2026-09-03', timeOut: '12:00', timeIn: '20:00', place: 'Lahore', purpose: 'Delivery / Saman', meterOut: 185945, meterIn: 186076, km: parseFloat((186076-185945).toFixed(1)), driver: 'Masood', vehicle: 'CAF-4893 - Porter', model: 'Porter', remark: 'Check by Azam' },
      { id: 1725321600007, dept: 'ADMIN', date: '2026-09-03', timeOut: '13:23', timeIn: '16:40', place: 'PSO', purpose: 'Return', meterOut: 167484, meterIn: 167545, km: parseFloat((167545-167484).toFixed(1)), driver: 'Tanveer Abbas', vehicle: 'LEB-5449 - Yaris', model: 'Yaris', remark: 'Check by Azam' },
      { id: 1725321600008, dept: 'LOADING', date: '2026-09-03', timeOut: '15:15', timeIn: '18:40', place: 'PSO', purpose: 'Oil', meterOut: 232248, meterIn: 232256, km: parseFloat((232256-232248).toFixed(1)), driver: 'Tanveer Abbas', vehicle: 'LES-4605 - Hino', model: 'Hino', remark: 'Check by Azam' },
      { id: 1725321600009, dept: 'LOADING', date: '2026-09-03', timeOut: '15:15', timeIn: '18:30', place: 'Multan Road + PSO', purpose: 'Brought evening goods', meterOut: 27033, meterIn: 27110, km: parseFloat((27110-27033).toFixed(1)), driver: 'Usama', vehicle: 'CAV-8213 - Porter', model: 'Porter', remark: 'Check by Azam' },
      { id: 1725321600010, dept: 'ADMIN', date: '2026-09-03', timeOut: '12:58', timeIn: '21:30', place: 'Gujjar Pura + Gulberg', purpose: 'Staff + Delivery', meterOut: 324513, meterIn: 324632, km: parseFloat((324632-324513).toFixed(1)), driver: 'Bilal Manzoor', vehicle: 'LEA-6860 - Toyota GLI', model: 'Toyota GLI', remark: 'Check by Azam' },
      { id: 1725321600011, dept: 'ADMIN', date: '2026-09-03', timeOut: '19:00', timeIn: '18:56', place: 'Auto Market', purpose: 'Staff drop', meterOut: 14522, meterIn: 14600, km: parseFloat((14600-14522).toFixed(1)), driver: 'Usama', vehicle: 'BPR-980 - Caravan', model: 'Caravan', remark: 'Check by Azam' },
      { id: 1725321600012, dept: 'LOADING', date: '2026-09-03', timeOut: '18:42', timeIn: '', place: 'Lahore', purpose: 'Staff drop', meterOut: 39668, meterIn: 39769, km: parseFloat((39769-39668).toFixed(1)), driver: 'Usama', vehicle: 'LES-4605 - Hino', model: 'Hino', remark: 'Check by Azam' },
      { id: 1725321600013, dept: 'ADMIN', date: '2026-09-03', timeOut: '08:35', timeIn: '12:50', place: 'Lahore', purpose: 'Staff drop', meterOut: 14600, meterIn: 14634, km: parseFloat((14634-14600).toFixed(1)), driver: 'Masood', vehicle: 'BPR-980 - Caravan', model: 'Caravan', remark: 'Check by Azam' },
      { id: 1725321600014, dept: 'LOADING', date: '2026-09-03', timeOut: '09:00', timeIn: '11:00', place: 'XPO + Central Lahore', purpose: 'Get goods', meterOut: 232252, meterIn: 232342, km: parseFloat((232342-232252).toFixed(1)), driver: 'Tanveer Abbas', vehicle: 'LES-4605 - Hino', model: 'Hino', remark: 'Check by Azam' },
      { id: 1725321600015, dept: 'SALE', date: '2026-09-03', timeOut: '09:50', timeIn: '', place: 'Sundar Industrial Estate', purpose: 'Staff', meterOut: 41669, meterIn: 41733, km: parseFloat((41733-41669).toFixed(1)), driver: 'Ashfaq', vehicle: 'ARQ-526 - Wagon-R', model: 'Wagon-R', remark: 'Check by Azam' },
      { id: 1725321600016, dept: 'LOADING', date: '2026-09-03', timeOut: '10:20', timeIn: '18:26', place: 'Workshop', purpose: 'Washing', meterOut: 186076, meterIn: 186086, km: parseFloat((186086-186076).toFixed(1)), driver: 'Zubair', vehicle: 'CAF-4893 - Porter', model: 'Porter', remark: 'Check by Azam' },
      { id: 1725321600017, dept: 'LOADING', date: '2026-09-03', timeOut: '10:48', timeIn: '20:25', place: 'Central Lahore XPO', purpose: 'Sales Officer', meterOut: 64106, meterIn: 64162, km: parseFloat((64162-64106).toFixed(1)), driver: 'Masood', vehicle: 'CAJ-6701 - Ravi', model: 'Ravi', remark: 'Check by Azam' },
      { id: 1725321600018, dept: 'SALE', date: '2026-09-03', timeOut: '11:20', timeIn: '11:30', place: 'PSO', purpose: 'Oil', meterOut: 64674, meterIn: 64785, km: parseFloat((64785-64674).toFixed(1)), driver: 'Masood', vehicle: 'ARQ-334 - Wagon-R', model: 'Wagon-R', remark: 'Check by Azam' },
      { id: 1725321600019, dept: 'LOADING', date: '2026-09-03', timeOut: '11:21', timeIn: '11:31', place: 'PSO', purpose: 'Oil', meterOut: 39769, meterIn: 39773, km: parseFloat((39773-39769).toFixed(1)), driver: 'Asad', vehicle: 'LES-4605 - Hino', model: 'Hino', remark: 'Check by Azam' },
      { id: 1725321600020, dept: 'SALE', date: '2026-09-03', timeOut: '', timeIn: '', place: '', purpose: '', meterOut: 41733, meterIn: 41738, km: parseFloat((41738-41733).toFixed(1)), driver: 'Qasim', vehicle: 'ARQ-526 - Wagon-R', model: 'Wagon-R', remark: 'Check by Azam' }
    ];
    var existingIds = existing.map(function(e){ return e.id; });
    newEntries.forEach(function(ne){
      if (existingIds.indexOf(ne.id) === -1) existing.push(ne);
    });
    save(existing);
    localStorage.setItem('vfp_seeded_sept032026_v2', '1');
    renderTable();
    updateStats();
  })();
  // ─────────────────────────────────────────────────────────────────────────'''

pattern = r'// [─\?\]+ One-time seed: handwritten log entries \(Sept 2026\).*?// [─\?\]+'
content_new = re.sub(pattern, new_block, content, flags=re.DOTALL)

with codecs.open(filepath, 'w', 'utf-8') as f:
    f.write(content_new)

print('Updated successfully')
