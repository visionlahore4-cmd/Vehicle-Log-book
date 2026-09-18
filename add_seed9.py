import re
import codecs

filepath = r'z:\Logbok vehicles\index.html'
with codecs.open(filepath, 'r', 'utf-8') as f:
    content = f.read()

new_seed = '''  // ── One-time seed: handwritten log entries (Sept 16-17 2026) ──────────────────
  (function seedSept16_17_2026() {
    if (localStorage.getItem('vfp_seeded_sept16_17_2026_v1')) return;
    var existing = load();
    var newEntries = [
      { id: 1726477600013, dept: 'LOADING', date: '2026-09-16', timeOut: '11:30', timeIn: '12:00', place: 'PSO', purpose: '', meterOut: 40886, meterIn: 40890, km: 4, driver: 'Masood', vehicle: 'AVX-481 - Hino', model: 'Hino', remark: 'Check by Khalid' },
      { id: 1726477600014, dept: 'LOADING', date: '2026-09-16', timeOut: '12:10', timeIn: '15:00', place: 'Multan Road', purpose: '', meterOut: 40890, meterIn: 40934, km: 44, driver: 'saeed', vehicle: 'AVX-481 - Hino', model: 'Hino', remark: 'Check by Khalid' },
      { id: 1726477600015, dept: 'LOADING', date: '2026-09-16', timeOut: '12:15', timeIn: '21:15', place: 'Market', purpose: 'Route', meterOut: 187305, meterIn: 187423, km: 118, driver: 'Zubair', vehicle: 'CAF-4893 - Porter', model: 'Porter', remark: 'Check by Khalid' },
      { id: 1726477600016, dept: 'LOADING', date: '2026-09-16', timeOut: '13:27', timeIn: '15:15', place: 'Fast Canteen', purpose: 'Pick Papers', meterOut: 64401, meterIn: 64410, km: 9, driver: 'Masood', vehicle: 'CAJ-6701 - Ravi', model: 'Ravi', remark: 'Check by Khalid' },
      { id: 1726477600017, dept: 'LOADING', date: '2026-09-16', timeOut: '16:50', timeIn: '18:25', place: 'Dawn Paper Market', purpose: '', meterOut: 233116, meterIn: 233121, km: 5, driver: 'Tanveer Abbas', vehicle: 'LES-4605 - Hino', model: 'Hino', remark: 'Check by Khalid' },
      { id: 1726477600018, dept: 'ADMIN', date: '2026-09-16', timeOut: '17:10', timeIn: '18:45', place: 'Adda Plot', purpose: 'Pick Staff', meterOut: 16026, meterIn: 16069, km: 43, driver: 'Masood', vehicle: 'BPR-980 - Caravan', model: 'Caravan', remark: 'Check by Khalid' },
      { id: 1726477600019, dept: 'LOADING', date: '2026-09-16', timeOut: '19:00', timeIn: '', place: 'Asif + Ehsan', purpose: '', meterOut: 40890, meterIn: 41035, km: 145, driver: 'Bilal Manzoor', vehicle: 'AVX-481 - Hino', model: 'Hino', remark: 'Check by Khalid' },
      { id: 1726477600020, dept: 'LOADING', date: '2026-09-16', timeOut: '19:15', timeIn: '20:15', place: 'Central Market', purpose: 'Dawn Paper Add', meterOut: 233121, meterIn: 233127, km: 6, driver: 'Tanveer Abbas', vehicle: 'LES-4605 - Hino', model: 'Hino', remark: 'Check by Ashfaq' },
      { id: 1726477600021, dept: 'ADMIN', date: '2026-09-16', timeOut: '06:15', timeIn: '08:55', place: 'Ali Town', purpose: 'Pick Staff', meterOut: 16069, meterIn: 16167, km: 98, driver: 'Masood', vehicle: 'BPR-980 - Caravan', model: 'Caravan', remark: 'Check by Ashfaq' },

      { id: 1726564000001, dept: 'LOADING', date: '2026-09-17', timeOut: '07:20', timeIn: '12:00', place: 'SO1 Central Model', purpose: 'Bring Goods', meterOut: 233127, meterIn: 233129, km: 2, driver: 'Tanveer Abbas', vehicle: 'LES-4605 - Hino', model: 'Hino', remark: 'Check by Azam' },
      { id: 1726564000002, dept: 'ADMIN', date: '2026-09-17', timeOut: '09:25', timeIn: '10:10', place: 'PSO', purpose: '', meterOut: 16167, meterIn: 16172, km: 5, driver: 'Masood', vehicle: 'BPR-980 - Caravan', model: 'Caravan', remark: 'Check by Khalid' },
      { id: 1726564000003, dept: 'ADMIN', date: '2026-09-17', timeOut: '09:40', timeIn: '10:15', place: 'PSO', purpose: '', meterOut: 215784, meterIn: 215789, km: 5, driver: 'saeed', vehicle: 'LE-3153 - Vitz', model: 'Vitz', remark: 'Check by Khalid' },
      { id: 1726564000004, dept: 'ADMIN', date: '2026-09-17', timeOut: '10:00', timeIn: '13:00', place: 'Dawn Factory', purpose: '', meterOut: 168221, meterIn: 168338, km: 117, driver: 'Ashfaq', vehicle: 'LEB-5449 - Yaris', model: 'Yaris', remark: 'Check by Khalid' },
      { id: 1726564000005, dept: 'ADMIN', date: '2026-09-17', timeOut: '11:00', timeIn: '13:35', place: 'Shadman Motorway Service', purpose: '', meterOut: 215789, meterIn: 215872, km: 83, driver: 'saeed', vehicle: 'LE-3153 - Vitz', model: 'Vitz', remark: 'Check by Khalid' },
      { id: 1726564000006, dept: 'LOADING', date: '2026-09-17', timeOut: '11:40', timeIn: '', place: 'Route', purpose: '', meterOut: 187423, meterIn: 187500, km: 77, driver: 'Masood', vehicle: 'CAF-4893 - Porter', model: 'Porter', remark: 'Check by Khalid' },
      { id: 1726564000007, dept: 'LOADING', date: '2026-09-17', timeOut: '12:00', timeIn: '13:50', place: 'Dawn Paper Market', purpose: '', meterOut: 233129, meterIn: 233134, km: 5, driver: 'Tanveer Abbas', vehicle: 'LES-4605 - Hino', model: 'Hino', remark: 'Check by Khalid' },
      { id: 1726564000008, dept: 'LOADING', date: '2026-09-17', timeOut: '13:40', timeIn: '', place: 'Atta Bakery Raiwind', purpose: 'Pick Goods', meterOut: 64410, meterIn: 64450, km: 40, driver: 'Usama', vehicle: 'CAJ-6701 - Ravi', model: 'Ravi', remark: 'Check by Azam' }
    ];
    var existingIds = existing.map(function(e){ return e.id; });
    newEntries.forEach(function(ne){
      if (existingIds.indexOf(ne.id) === -1) existing.push(ne);
    });
    save(existing);
    localStorage.setItem('vfp_seeded_sept16_17_2026_v1', '1');
  })();
'''

marker = '  // ── One-time seed: handwritten log entries (Sept 15-16 2026) ──────────────────'
if marker in content:
    content_new = content.replace(marker, new_seed + '\n' + marker)
    with codecs.open(filepath, 'w', 'utf-8') as f:
        f.write(content_new)
    print("New entries seed block added")
else:
    print("Marker not found")
