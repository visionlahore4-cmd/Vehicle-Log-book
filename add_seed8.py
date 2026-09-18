import re
import codecs

filepath = r'z:\Logbok vehicles\index.html'
with codecs.open(filepath, 'r', 'utf-8') as f:
    content = f.read()

new_seed = '''  // ── One-time seed: handwritten log entries (Sept 15-16 2026) ──────────────────
  (function seedSept15_16_2026() {
    if (localStorage.getItem('vfp_seeded_sept15_16_2026_v1')) return;
    var existing = load();
    var newEntries = [
      { id: 1726391200005, dept: 'LOADING', date: '2026-09-15', timeOut: '11:32', timeIn: '16:35', place: 'Dalan Shehr', purpose: '', meterOut: 27299, meterIn: 27373, km: 74, driver: 'saeed', vehicle: 'CAV-8213 - Porter', model: 'Porter', remark: 'Check by Khalid' },
      { id: 1726391200006, dept: 'ADMIN', date: '2026-09-15', timeOut: '12:05', timeIn: '12:26', place: 'Workshop', purpose: 'Air in Tires', meterOut: 85770, meterIn: 85865, km: 95, driver: 'Ashfaq', vehicle: 'AFS-612 - Bolan', model: 'Bolan', remark: 'Check by Khalid' },
      { id: 1726391200007, dept: 'SALE', date: '2026-09-15', timeOut: '12:38', timeIn: '22:45', place: '', purpose: 'Delivery', meterOut: 41985, meterIn: 42025, km: 40, driver: 'Umer Dogar', vehicle: 'ARQ-526 - Wagon-R', model: 'Wagon-R', remark: 'Check by Khalid' },
      { id: 1726391200008, dept: 'LOADING', date: '2026-09-15', timeOut: '13:20', timeIn: '14:05', place: 'PSO', purpose: '', meterOut: 187301, meterIn: 187305, km: 4, driver: 'Zubair', vehicle: 'CAF-4893 - Porter', model: 'Porter', remark: 'Check by Khalid' },
      { id: 1726391200009, dept: 'LOADING', date: '2026-09-15', timeOut: '14:00', timeIn: '20:20', place: '', purpose: 'For Goods', meterOut: 233002, meterIn: 233017, km: 15, driver: 'Tanveer Abbas', vehicle: 'LES-4605 - Hino', model: 'Hino', remark: 'Check by Khalid' },
      { id: 1726391200010, dept: 'ADMIN', date: '2026-09-15', timeOut: '17:09', timeIn: '21:05', place: '', purpose: 'Staff Drop', meterOut: 15874, meterIn: 15960, km: 86, driver: 'Raees Ahmed', vehicle: 'BPR-980 - Caravan', model: 'Caravan', remark: 'Check by Khalid' },
      { id: 1726391200011, dept: 'SALE', date: '2026-09-15', timeOut: '17:10', timeIn: '17:20', place: 'PSO', purpose: '', meterOut: 66206, meterIn: 66211, km: 5, driver: 'Masood', vehicle: 'ART-542 - Vehicle', model: 'Vehicle', remark: 'Check by Khalid' },
      { id: 1726391200012, dept: 'LOADING', date: '2026-09-15', timeOut: '18:00', timeIn: '10:15', place: '', purpose: 'Waseef + Ehsan', meterOut: 40781, meterIn: 40886, km: 105, driver: 'Bilal Manzoor', vehicle: 'AVX-481 - Hino', model: 'Hino', remark: 'Check by Khalid' },

      { id: 1726477600001, dept: 'ADMIN', date: '2026-09-16', timeOut: '06:40', timeIn: '08:53', place: '', purpose: 'Pick Staff', meterOut: 15960, meterIn: 16026, km: 66, driver: 'Masood', vehicle: 'BPR-980 - Caravan', model: 'Caravan', remark: 'Check by Ashfaq' },
      { id: 1726477600002, dept: 'LOADING', date: '2026-09-16', timeOut: '08:25', timeIn: '08:40', place: 'PSO', purpose: 'Oil', meterOut: 64397, meterIn: 64399, km: 2, driver: 'Zubair', vehicle: 'CAJ-6701 - Ravi', model: 'Ravi', remark: 'Check by Khalid' },
      { id: 1726477600003, dept: 'LOADING', date: '2026-09-16', timeOut: '08:25', timeIn: '08:40', place: 'PSO', purpose: 'Oil', meterOut: 233017, meterIn: 233022, km: 5, driver: 'Tanveer Abbas', vehicle: 'LES-4605 - Hino', model: 'Hino', remark: 'Check by Khalid' },
      { id: 1726477600004, dept: 'SALE', date: '2026-09-16', timeOut: '08:30', timeIn: '08:40', place: 'PSO', purpose: 'Oil', meterOut: 65306, meterIn: 65310, km: 4, driver: 'Ashfaq', vehicle: 'ARQ-334 - Wagon-R', model: 'Wagon-R', remark: 'Check by Khalid' },
      { id: 1726477600005, dept: 'LOADING', date: '2026-09-16', timeOut: '08:30', timeIn: '08:40', place: 'PSO', purpose: 'Oil', meterOut: 27373, meterIn: 27378, km: 5, driver: 'saeed', vehicle: 'CAV-8213 - Porter', model: 'Porter', remark: 'Check by Khalid' },
      { id: 1726477600006, dept: 'ADMIN', date: '2026-09-16', timeOut: '08:33', timeIn: '08:40', place: 'PSO', purpose: 'Oil', meterOut: 324662, meterIn: 324667, km: 5, driver: 'Usama', vehicle: 'LEA-6860 - Toyota GLI', model: 'Toyota GLI', remark: 'Check by Khalid' },
      { id: 1726477600007, dept: 'SALE', date: '2026-09-16', timeOut: '08:40', timeIn: '09:10', place: 'PSO', purpose: 'Oil', meterOut: 42025, meterIn: 42030, km: 5, driver: 'Ashfaq', vehicle: 'ARQ-526 - Wagon-R', model: 'Wagon-R', remark: 'Check by Khalid' },
      { id: 1726477600008, dept: 'LOADING', date: '2026-09-16', timeOut: '09:05', timeIn: '12:50', place: 'Noman Dispensary', purpose: '', meterOut: 233022, meterIn: 233116, km: 94, driver: 'Tanveer Abbas', vehicle: 'LES-4605 - Hino', model: 'Hino', remark: 'Check by Khalid' },
      { id: 1726477600009, dept: 'SALE', date: '2026-09-16', timeOut: '10:10', timeIn: '19:00', place: 'City Pharma', purpose: '', meterOut: 65310, meterIn: 65457, km: 147, driver: 'Asad Saleem', vehicle: 'ARQ-334 - Wagon-R', model: 'Wagon-R', remark: 'Check by Khalid' },
      { id: 1726477600010, dept: 'ADMIN', date: '2026-09-16', timeOut: '10:20', timeIn: '11:50', place: 'Mustansariya', purpose: 'Shahbaz Micro', meterOut: 168180, meterIn: 168221, km: 41, driver: 'saeed', vehicle: 'LEB-5449 - Yaris', model: 'Yaris', remark: 'Check by Khalid' },
      { id: 1726477600011, dept: 'SALE', date: '2026-09-16', timeOut: '10:57', timeIn: '13:15', place: 'Workshop Sundar', purpose: '', meterOut: 66245, meterIn: 66294, km: 49, driver: 'Ashfaq', vehicle: 'ART-542 - Vehicle', model: 'Vehicle', remark: 'Check by Khalid' },
      { id: 1726477600012, dept: 'LOADING', date: '2026-09-16', timeOut: '11:48', timeIn: '18:52', place: 'Marhaba Lahore', purpose: '', meterOut: 27378, meterIn: 27452, km: 74, driver: 'Usama', vehicle: 'CAV-8213 - Porter', model: 'Porter', remark: 'Check by Khalid' }
    ];
    var existingIds = existing.map(function(e){ return e.id; });
    newEntries.forEach(function(ne){
      if (existingIds.indexOf(ne.id) === -1) existing.push(ne);
    });
    save(existing);
    localStorage.setItem('vfp_seeded_sept15_16_2026_v1', '1');
  })();
'''

marker = '  // ── One-time seed: handwritten log entries (Sept 12-15 2026) ──────────────────'
if marker in content:
    content_new = content.replace(marker, new_seed + '\n' + marker)
    with codecs.open(filepath, 'w', 'utf-8') as f:
        f.write(content_new)
    print("New entries seed block added")
else:
    print("Marker not found")
