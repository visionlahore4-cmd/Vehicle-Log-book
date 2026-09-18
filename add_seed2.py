import re
import codecs

filepath = r'z:\Logbok vehicles\index.html'
with codecs.open(filepath, 'r', 'utf-8') as f:
    content = f.read()

new_seed = '''  // ── One-time seed: handwritten log entries (Sept 04-05 2026) ──────────────────
  (function seedSept0405_2026() {
    if (localStorage.getItem('vfp_seeded_sept0405_2026_v1')) return;
    var existing = load();
    var newEntries = [
      { id: 1725408000001, dept: 'ADMIN', date: '2026-09-04', timeOut: '11:50', timeIn: '', place: 'PSO', purpose: 'Oil', meterOut: 14634, meterIn: 14639, km: 5, driver: 'Masood', vehicle: 'BPR-980 - Caravan', model: 'Caravan', remark: 'Check by Azam' },
      { id: 1725408000002, dept: 'LOADING', date: '2026-09-04', timeOut: '12:00', timeIn: '21:34', place: 'Lahore', purpose: 'Market', meterOut: 186086, meterIn: 186201, km: 115, driver: 'Zubair', vehicle: 'CAF-4893 - Porter', model: 'Porter', remark: 'Check by Azam' },
      { id: 1725408000003, dept: 'ADMIN', date: '2026-09-04', timeOut: '14:24', timeIn: '18:05', place: 'XPO Center', purpose: 'Executive Drop', meterOut: 14639, meterIn: 14708, km: 69, driver: 'Masood', vehicle: 'BPR-980 - Caravan', model: 'Caravan', remark: 'Check by Azam' },
      { id: 1725408000004, dept: 'ADMIN', date: '2026-09-04', timeOut: '13:50', timeIn: '18:00', place: 'XPO Center', purpose: 'Executive Officer', meterOut: 167545, meterIn: 167604, km: 59, driver: 'Usama', vehicle: 'LEB-5449 - Yaris', model: 'Yaris', remark: 'Check by Azam' },
      { id: 1725408000005, dept: 'LOADING', date: '2026-09-04', timeOut: '14:00', timeIn: '', place: 'Model Town', purpose: 'Drop Goods', meterOut: 27110, meterIn: 27161, km: 51, driver: 'Ashfaq', vehicle: 'CAV-8213 - Porter', model: 'Porter', remark: 'Check by Azam' },
      { id: 1725408000006, dept: 'ADMIN', date: '2026-09-04', timeOut: '17:00', timeIn: '17:40', place: 'Raiwind', purpose: 'Staff Drop', meterOut: 25406, meterIn: 25420, km: 14, driver: 'Ashfaq', vehicle: 'AFS-612 - Bolan', model: 'Bolan', remark: 'Check by Azam' },
      { id: 1725408000007, dept: 'LOADING', date: '2026-09-04', timeOut: '17:30', timeIn: '20:18', place: 'Kasur', purpose: 'Goods Delivery', meterOut: 232342, meterIn: 232388, km: 46, driver: 'Tanveer Abbas', vehicle: 'LES-4605 - Hino', model: 'Hino', remark: 'Check by Azam' },
      { id: 1725408000008, dept: 'SALE', date: '2026-09-04', timeOut: '18:00', timeIn: '19:40', place: 'XPO', purpose: 'Pick up Staff', meterOut: 41738, meterIn: 41798, km: 60, driver: 'Usama', vehicle: 'ARQ-526 - Wagon-R', model: 'Wagon-R', remark: 'Check by Azam' },
      { id: 1725408000009, dept: 'LOADING', date: '2026-09-04', timeOut: '18:27', timeIn: '09:50', place: 'Lahore', purpose: 'Staff Drop', meterOut: 39769, meterIn: 39862, km: 93, driver: 'Bilal Manzoor', vehicle: 'AVX-481 - Hino', model: 'Hino', remark: 'Check by Azam' },
      { id: 1725494400001, dept: 'ADMIN', date: '2026-09-05', timeOut: '01:50', timeIn: '09:00', place: 'Ali Town', purpose: 'Staff Pick', meterOut: 14708, meterIn: 14775, km: 67, driver: 'Masood', vehicle: 'BPR-980 - Caravan', model: 'Caravan', remark: '' },
      { id: 1725494400002, dept: 'SALE', date: '2026-09-05', timeOut: '08:31', timeIn: '11:05', place: 'XPO + Central Model Lahore', purpose: '', meterOut: 64785, meterIn: 64883, km: 98, driver: 'Ashfaq', vehicle: 'ARQ-334 - Wagon-R', model: 'Wagon-R', remark: 'Check by Azam' },
      { id: 1725494400003, dept: 'ADMIN', date: '2026-09-05', timeOut: '09:00', timeIn: '11:40', place: 'Lahore', purpose: 'XPO', meterOut: 14775, meterIn: 14843, km: 68, driver: 'Usama', vehicle: 'BPR-980 - Caravan', model: 'Caravan', remark: 'Check by Azam' },
      { id: 1725494400004, dept: 'LOADING', date: '2026-09-05', timeOut: '09:00', timeIn: '10:25', place: 'Model Town', purpose: 'Washing', meterOut: 64162, meterIn: 64171, km: 9, driver: 'Zubair', vehicle: 'CAJ-6701 - Ravi', model: 'Ravi', remark: 'Check by Azam' },
      { id: 1725494400005, dept: 'SALE', date: '2026-09-05', timeOut: '09:25', timeIn: '19:45', place: 'Lahore', purpose: 'XPO', meterOut: 41798, meterIn: 41871, km: 73, driver: 'Asad', vehicle: 'ARQ-526 - Wagon-R', model: 'Wagon-R', remark: 'Check by Azam' },
      { id: 1725494400006, dept: 'LOADING', date: '2026-09-05', timeOut: '09:36', timeIn: '13:10', place: 'Sundar', purpose: 'Booking', meterOut: 232388, meterIn: 232464, km: 76, driver: 'Tanveer Abbas', vehicle: 'LES-4605 - Hino', model: 'Hino', remark: 'Check by Azam' },
      { id: 1725494400007, dept: 'ADMIN', date: '2026-09-05', timeOut: '09:50', timeIn: '10:00', place: 'PSO', purpose: 'Oil', meterOut: 167603, meterIn: 167608, km: 5, driver: 'Masood', vehicle: 'LEB-5449 - Yaris', model: 'Yaris', remark: 'Check by Azam' },
      { id: 1725494400008, dept: 'ADMIN', date: '2026-09-05', timeOut: '09:50', timeIn: '10:00', place: 'PSO', purpose: 'Oil', meterOut: 94378, meterIn: 94381, km: 3, driver: 'Zubair', vehicle: 'ARX-361 - Vehicle', model: 'Vehicle', remark: 'Check by Azam' },
      { id: 1725494400009, dept: 'ADMIN', date: '2026-09-05', timeOut: '10:15', timeIn: '11:00', place: 'Ali Town', purpose: 'Doctor Building', meterOut: 167609, meterIn: 167640, km: 31, driver: 'Masood', vehicle: 'LEB-5449 - Yaris', model: 'Yaris', remark: 'Check by Azam' },
      { id: 1725494400010, dept: 'LOADING', date: '2026-09-05', timeOut: '11:40', timeIn: '19:00', place: 'Lahore', purpose: 'Local', meterOut: 186201, meterIn: 186336, km: 135, driver: 'saeed', vehicle: 'CAF-4893 - Porter', model: 'Porter', remark: '' },
      { id: 1725494400011, dept: 'LOADING', date: '2026-09-05', timeOut: '11:45', timeIn: '13:10', place: 'Sundar SO1', purpose: 'Production', meterOut: 27161, meterIn: 27169, km: 8, driver: 'Zubair', vehicle: 'CAV-8213 - Porter', model: 'Porter', remark: '' }
    ];
    var existingIds = existing.map(function(e){ return e.id; });
    newEntries.forEach(function(ne){
      if (existingIds.indexOf(ne.id) === -1) existing.push(ne);
    });
    save(existing);
    localStorage.setItem('vfp_seeded_sept0405_2026_v1', '1');
  })();
'''

marker = '  // ── One-time seed: handwritten log entries (Sept 03 2026) ──────────────────'
if marker in content:
    content_new = content.replace(marker, new_seed + '\n' + marker)
    with codecs.open(filepath, 'w', 'utf-8') as f:
        f.write(content_new)
    print("New entries seed block added")
else:
    print("Marker not found")
