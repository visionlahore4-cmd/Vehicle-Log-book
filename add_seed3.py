import re
import codecs

filepath = r'z:\Logbok vehicles\index.html'
with codecs.open(filepath, 'r', 'utf-8') as f:
    content = f.read()

new_seed = '''  // ── One-time seed: handwritten log entries (Sept 05-07 2026) ──────────────────
  (function seedSept05_07_2026() {
    if (localStorage.getItem('vfp_seeded_sept05_07_2026_v1')) return;
    var existing = load();
    var newEntries = [
      { id: 1725500000001, dept: 'LOADING', date: '2026-09-05', timeOut: '11:55', timeIn: '12:15', place: 'Sundar', purpose: 'Getting Plants', meterOut: 64171, meterIn: 64184, km: 13, driver: 'Masood', vehicle: 'CAJ-6701 - Ravi', model: 'Ravi', remark: '' },
      { id: 1725500000002, dept: 'ADMIN', date: '2026-09-05', timeOut: '12:10', timeIn: '20:10', place: 'XPO Center', purpose: 'Delivering Goods', meterOut: 85424, meterIn: 85501, km: 77, driver: 'Ashfaq', vehicle: 'AFS-612 - Bolan', model: 'Bolan', remark: 'Check by Azam' },
      { id: 1725500000003, dept: 'ADMIN', date: '2026-09-05', timeOut: '16:00', timeIn: '22:30', place: 'Lahore', purpose: 'Local', meterOut: 167640, meterIn: 167673, km: 33, driver: 'Raheel', vehicle: 'LEB-5449 - Yaris', model: 'Yaris', remark: '' },
      { id: 1725500000004, dept: 'ADMIN', date: '2026-09-05', timeOut: '17:10', timeIn: '18:10', place: 'Ichra Plaza', purpose: 'Admin Staff Drop', meterOut: 14843, meterIn: 14881, km: 38, driver: 'Masood', vehicle: 'BPR-980 - Caravan', model: 'Caravan', remark: '' },
      { id: 1725500000005, dept: 'ADMIN', date: '2026-09-05', timeOut: '18:23', timeIn: '23:00', place: 'Lahore', purpose: 'Drop', meterOut: 14881, meterIn: 14944, km: 63, driver: 'Masood', vehicle: 'BPR-980 - Caravan', model: 'Caravan', remark: 'Check by Azam' },
      { id: 1725500000006, dept: 'LOADING', date: '2026-09-05', timeOut: '16:30', timeIn: '10:00', place: 'Lahore', purpose: 'Staff Drop', meterOut: 39862, meterIn: 40035, km: 173, driver: 'Bilal Manzoor', vehicle: 'AVX-481 - Hino', model: 'Hino', remark: 'Check by Azam' },
      
      { id: 1725586400001, dept: 'LOADING', date: '2026-09-06', timeOut: '15:50', timeIn: '16:15', place: 'Tire Shop', purpose: 'Air Filling', meterOut: 64184, meterIn: 64201, km: 17, driver: 'Ashfaq', vehicle: 'CAJ-6701 - Ravi', model: 'Ravi', remark: 'Check by Azam' },
      
      { id: 1725672800001, dept: 'ADMIN', date: '2026-09-07', timeOut: '06:30', timeIn: '07:25', place: 'Niaz Baig', purpose: 'Raiwind Gosht Lene', meterOut: 85501, meterIn: 85515, km: 14, driver: 'Ashfaq', vehicle: 'AFS-612 - Bolan', model: 'Bolan', remark: '' },
      { id: 1725672800002, dept: 'ADMIN', date: '2026-09-07', timeOut: '06:45', timeIn: '08:55', place: 'Ali Town', purpose: 'Staff Pick', meterOut: 14944, meterIn: 15009, km: 65, driver: 'Masood', vehicle: 'BPR-980 - Caravan', model: 'Caravan', remark: '' },
      { id: 1725672800003, dept: 'ADMIN', date: '2026-09-07', timeOut: '10:00', timeIn: '10:30', place: 'PSO', purpose: 'Oil', meterOut: 94880, meterIn: 94885, km: 5, driver: 'Ashfaq', vehicle: 'ARX-361 - Vehicle', model: 'Vehicle', remark: 'Check by Azam' },
      { id: 1725672800004, dept: 'LOADING', date: '2026-09-07', timeOut: '10:00', timeIn: '10:32', place: 'PSO', purpose: 'Oil', meterOut: 186336, meterIn: 186341, km: 5, driver: 'Zubair', vehicle: 'CAF-4893 - Porter', model: 'Porter', remark: 'Check by Azam' },
      { id: 1725672800005, dept: 'ADMIN', date: '2026-09-07', timeOut: '10:00', timeIn: '10:35', place: 'PSO', purpose: 'Oil', meterOut: 15009, meterIn: 15014, km: 5, driver: 'Masood', vehicle: 'BPR-980 - Caravan', model: 'Caravan', remark: 'Check by Azam' },
      { id: 1725672800006, dept: 'SALE', date: '2026-09-07', timeOut: '10:00', timeIn: '10:40', place: 'PSO', purpose: 'Oil', meterOut: 64883, meterIn: 64888, km: 5, driver: 'Usama', vehicle: 'ARQ-334 - Wagon-R', model: 'Wagon-R', remark: 'Check by Azam' },
      { id: 1725672800007, dept: 'LOADING', date: '2026-09-07', timeOut: '10:00', timeIn: '10:45', place: 'PSO', purpose: 'Oil', meterOut: 27169, meterIn: 27174, km: 5, driver: 'saeed', vehicle: 'CAV-8213 - Porter', model: 'Porter', remark: 'Check by Azam' },
      { id: 1725672800008, dept: 'LOADING', date: '2026-09-07', timeOut: '10:05', timeIn: '10:50', place: 'PSO', purpose: 'Oil', meterOut: 64201, meterIn: 64206, km: 5, driver: 'Masood', vehicle: 'CAJ-6701 - Ravi', model: 'Ravi', remark: 'Check by Azam' },
      { id: 1725672800009, dept: 'SALE', date: '2026-09-07', timeOut: '10:00', timeIn: '10:52', place: 'PSO', purpose: 'Oil', meterOut: 41871, meterIn: 41876, km: 5, driver: 'Usama', vehicle: 'ARQ-526 - Wagon-R', model: 'Wagon-R', remark: 'Check by Azam' },
      { id: 1725672800010, dept: 'LOADING', date: '2026-09-07', timeOut: '10:30', timeIn: '15:15', place: 'Defense Road', purpose: 'Goods Pick', meterOut: 27174, meterIn: 27237, km: 63, driver: 'Zubair', vehicle: 'CAV-8213 - Porter', model: 'Porter', remark: 'Check by Azam' },
      { id: 1725672800011, dept: 'LOADING', date: '2026-09-07', timeOut: '11:00', timeIn: '16:00', place: 'Towards City', purpose: 'Delivery', meterOut: 232464, meterIn: 232541, km: 77, driver: 'Tanveer Abbas', vehicle: 'LES-4605 - Hino', model: 'Hino', remark: 'Check by Azam' },
      { id: 1725672800012, dept: 'LOADING', date: '2026-09-07', timeOut: '11:35', timeIn: '07:15', place: 'Lahore', purpose: 'Goods Delivery', meterOut: 186341, meterIn: 186466, km: 125, driver: 'saeed', vehicle: 'CAF-4893 - Porter', model: 'Porter', remark: 'Check by Azam' },
      { id: 1725672800013, dept: 'LOADING', date: '2026-09-07', timeOut: '12:00', timeIn: '13:00', place: 'Raiwind', purpose: 'Bringing Post', meterOut: 64206, meterIn: 64225, km: 19, driver: 'Masood', vehicle: 'CAJ-6701 - Ravi', model: 'Ravi', remark: '' },
      { id: 1725672800014, dept: 'LOADING', date: '2026-09-07', timeOut: '17:00', timeIn: '', place: 'Lahore', purpose: 'Staff Drop', meterOut: 40035, meterIn: 40129, km: 94, driver: 'Bilal Manzoor', vehicle: 'AVX-481 - Hino', model: 'Hino', remark: '' }
    ];
    var existingIds = existing.map(function(e){ return e.id; });
    newEntries.forEach(function(ne){
      if (existingIds.indexOf(ne.id) === -1) existing.push(ne);
    });
    save(existing);
    localStorage.setItem('vfp_seeded_sept05_07_2026_v1', '1');
  })();
'''

marker = '  // ── One-time seed: handwritten log entries (Sept 04-05 2026) ──────────────────'
if marker in content:
    content_new = content.replace(marker, new_seed + '\n' + marker)
    with codecs.open(filepath, 'w', 'utf-8') as f:
        f.write(content_new)
    print("New entries seed block added")
else:
    print("Marker not found")
