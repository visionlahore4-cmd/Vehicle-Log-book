import re
import codecs

filepath = r'z:\Logbok vehicles\index.html'
with codecs.open(filepath, 'r', 'utf-8') as f:
    content = f.read()

new_seed = '''  // ── One-time seed: handwritten log entries (Sept 12-15 2026) ──────────────────
  (function seedSept12_15_2026() {
    if (localStorage.getItem('vfp_seeded_sept12_15_2026_v1')) return;
    var existing = load();
    var newEntries = [
      { id: 1726132000008, dept: 'LOADING', date: '2026-09-12', timeOut: '17:30', timeIn: '09:50', place: 'Lahore', purpose: 'Drop Staff', meterOut: 40553, meterIn: 40680, km: 127, driver: 'Bilal Manzoor', vehicle: 'AVX-481 - Hino', model: 'Hino', remark: 'Check by Azam' },
      { id: 1726132000009, dept: 'ADMIN', date: '2026-09-12', timeOut: '17:10', timeIn: '18:20', place: 'Adda Plot', purpose: 'Drop Staff', meterOut: 15663, meterIn: 15703, km: 40, driver: 'Ashfaq', vehicle: 'BPR-980 - Caravan', model: 'Caravan', remark: 'Check by Azam' },
      { id: 1726132000010, dept: 'ADMIN', date: '2026-09-12', timeOut: '10:00', timeIn: '17:40', place: 'Grid Lahore Cantt', purpose: 'For Site', meterOut: 85606, meterIn: 85898, km: 292, driver: 'Muneer', vehicle: 'AFS-612 - Bolan', model: 'Bolan', remark: 'Check by Azam' },
      
      { id: 1726218400001, dept: 'SALE', date: '2026-09-13', timeOut: '15:20', timeIn: '16:00', place: 'Railway Road Adda', purpose: 'Pick Cycle Parts', meterOut: 65212, meterIn: 65237, km: 25, driver: 'Masood', vehicle: 'ARQ-334 - Wagon-R', model: 'Wagon-R', remark: 'Check by Khalid' },

      { id: 1726304800001, dept: 'ADMIN', date: '2026-09-14', timeOut: '06:40', timeIn: '09:00', place: 'Adda Plot', purpose: 'Pick Staff', meterOut: 15703, meterIn: 15769, km: 66, driver: 'Masood', vehicle: 'BPR-980 - Caravan', model: 'Caravan', remark: 'Check by Ashfaq' },
      { id: 1726304800002, dept: 'ADMIN', date: '2026-09-14', timeOut: '09:45', timeIn: '11:35', place: 'Gulberg', purpose: '', meterOut: 168013, meterIn: 168092, km: 79, driver: 'Masood', vehicle: 'LEB-5449 - Yaris', model: 'Yaris', remark: 'Check by Khalid' },
      { id: 1726304800003, dept: 'ADMIN', date: '2026-09-14', timeOut: '10:20', timeIn: '12:55', place: 'Manga Road', purpose: '', meterOut: 96602, meterIn: 96656, km: 54, driver: 'Raees Ahmed', vehicle: 'ARX-361 - Vehicle', model: 'Vehicle', remark: 'Check by Khalid' },
      { id: 1726304800004, dept: 'ADMIN', date: '2026-09-14', timeOut: '11:50', timeIn: '12:00', place: 'PSO', purpose: 'Oil', meterOut: 168092, meterIn: 168097, km: 5, driver: 'Masood', vehicle: 'LEB-5449 - Yaris', model: 'Yaris', remark: 'Check by Khalid' },
      { id: 1726304800005, dept: 'LOADING', date: '2026-09-14', timeOut: '12:00', timeIn: '22:00', place: 'Motorway', purpose: 'Market', meterOut: 187126, meterIn: 187301, km: 175, driver: 'saeed', vehicle: 'CAF-4893 - Porter', model: 'Porter', remark: 'Check by Khalid' },
      { id: 1726304800006, dept: 'ADMIN', date: '2026-09-14', timeOut: '12:00', timeIn: '12:15', place: 'PSO', purpose: 'Oil', meterOut: 85698, meterIn: 85703, km: 5, driver: 'Masood', vehicle: 'AFS-612 - Bolan', model: 'Bolan', remark: 'Check by Khalid' },
      { id: 1726304800007, dept: 'ADMIN', date: '2026-09-14', timeOut: '12:30', timeIn: '12:40', place: 'PSO', purpose: 'Oil', meterOut: 215625, meterIn: 215628, km: 3, driver: 'Masood', vehicle: 'LE-3153 - Vitz', model: 'Vitz', remark: 'Check by Khalid' },
      { id: 1726304800008, dept: 'ADMIN', date: '2026-09-14', timeOut: '13:15', timeIn: '15:40', place: 'Grid Station', purpose: '', meterOut: 85703, meterIn: 85728, km: 25, driver: 'Zubair', vehicle: 'AFS-612 - Bolan', model: 'Bolan', remark: 'Check by Khalid' },
      { id: 1726304800009, dept: 'ADMIN', date: '2026-09-14', timeOut: '15:35', timeIn: '18:40', place: 'Gulberg', purpose: '', meterOut: 168097, meterIn: 168180, km: 83, driver: 'Masood', vehicle: 'LEB-5449 - Yaris', model: 'Yaris', remark: 'Check by Khalid' },
      { id: 1726304800010, dept: 'ADMIN', date: '2026-09-14', timeOut: '17:10', timeIn: '18:20', place: 'Adda Plot', purpose: 'Drop Staff', meterOut: 15769, meterIn: 15808, km: 39, driver: 'Zubair', vehicle: 'BPR-980 - Caravan', model: 'Caravan', remark: 'Check by Khalid' },
      { id: 1726304800011, dept: 'SALE', date: '2026-09-14', timeOut: '17:30', timeIn: '22:10', place: 'Multan Road', purpose: '', meterOut: 65240, meterIn: 65306, km: 66, driver: 'Asad Dogar', vehicle: 'ARQ-334 - Wagon-R', model: 'Wagon-R', remark: 'Check by Khalid' },
      { id: 1726304800012, dept: 'LOADING', date: '2026-09-14', timeOut: '17:40', timeIn: '09:50', place: 'Lahore', purpose: 'Drop Staff', meterOut: 40680, meterIn: 40781, km: 101, driver: 'Bilal Manzoor', vehicle: 'AVX-481 - Hino', model: 'Hino', remark: 'Check by Khalid' },

      { id: 1726391200001, dept: 'ADMIN', date: '2026-09-15', timeOut: '06:40', timeIn: '09:00', place: 'Adda Plot', purpose: 'Pick Staff', meterOut: 15808, meterIn: 15874, km: 66, driver: 'Masood', vehicle: 'BPR-980 - Caravan', model: 'Caravan', remark: 'Check by Ashfaq' },
      { id: 1726391200002, dept: 'ADMIN', date: '2026-09-15', timeOut: '08:20', timeIn: '11:54', place: 'Bahria Town', purpose: '', meterOut: 85703, meterIn: 85770, km: 67, driver: 'Ashfaq', vehicle: 'AFS-612 - Bolan', model: 'Bolan', remark: 'Check by Khalid' },
      { id: 1726391200003, dept: 'ADMIN', date: '2026-09-15', timeOut: '09:02', timeIn: '15:25', place: 'Raiwind Road', purpose: '', meterOut: 215628, meterIn: 215784, km: 156, driver: 'Masood', vehicle: 'LE-3153 - Vitz', model: 'Vitz', remark: 'Check by Khalid' },
      { id: 1726391200004, dept: 'LOADING', date: '2026-09-15', timeOut: '10:25', timeIn: '', place: 'Dawn News Market', purpose: '', meterOut: 232997, meterIn: 233002, km: 5, driver: 'Tanveer Abbas', vehicle: 'LES-4605 - Hino', model: 'Hino', remark: 'Check by Khalid' }
    ];
    var existingIds = existing.map(function(e){ return e.id; });
    newEntries.forEach(function(ne){
      if (existingIds.indexOf(ne.id) === -1) existing.push(ne);
    });
    save(existing);
    localStorage.setItem('vfp_seeded_sept12_15_2026_v1', '1');
  })();
'''

marker = '  // ── One-time seed: handwritten log entries (Sept 10-12 2026) ──────────────────'
if marker in content:
    content_new = content.replace(marker, new_seed + '\n' + marker)
    with codecs.open(filepath, 'w', 'utf-8') as f:
        f.write(content_new)
    print("New entries seed block added")
else:
    print("Marker not found")
