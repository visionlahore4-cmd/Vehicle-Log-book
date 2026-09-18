import re
import codecs

filepath = r'z:\Logbok vehicles\index.html'
with codecs.open(filepath, 'r', 'utf-8') as f:
    content = f.read()

new_seed = '''  // ── One-time seed: handwritten log entries (Sept 09-10 2026) ──────────────────
  (function seedSept09_10_2026() {
    if (localStorage.getItem('vfp_seeded_sept09_10_2026_v1')) return;
    var existing = load();
    var newEntries = [
      { id: 1725872800001, dept: 'ADMIN', date: '2026-09-09', timeOut: '06:50', timeIn: '08:58', place: 'Adda Plot', purpose: 'Pick Staff', meterOut: 15262, meterIn: 15343, km: 81, driver: 'Masood', vehicle: 'BPR-980 - Caravan', model: 'Caravan', remark: 'Check by Ashfaq' },
      { id: 1725872800002, dept: 'LOADING', date: '2026-09-09', timeOut: '09:15', timeIn: '10:00', place: 'Lahore', purpose: 'Local', meterOut: 232632, meterIn: 232638, km: 6, driver: 'Tanveer Abbas', vehicle: 'LES-4605 - Hino', model: 'Hino', remark: '' },
      { id: 1725872800003, dept: 'LOADING', date: '2026-09-09', timeOut: '10:05', timeIn: '10:34', place: 'PSO', purpose: 'Petrol', meterOut: 232638, meterIn: 232709, km: 71, driver: 'Tanveer Abbas', vehicle: 'LES-4605 - Hino', model: 'Hino', remark: 'Check by Azam' },
      { id: 1725872800004, dept: 'SALE', date: '2026-09-09', timeOut: '10:18', timeIn: '10:41', place: 'PSO', purpose: 'Oil', meterOut: 65074, meterIn: 65079, km: 5, driver: 'Masood', vehicle: 'ARQ-334 - Wagon-R', model: 'Wagon-R', remark: 'Check by Azam' },
      { id: 1725872800005, dept: 'ADMIN', date: '2026-09-09', timeOut: '10:18', timeIn: '10:41', place: 'PSO', purpose: 'Oil', meterOut: 15333, meterIn: 15338, km: 5, driver: 'Masood', vehicle: 'BPR-980 - Caravan', model: 'Caravan', remark: 'Check by Azam' },
      { id: 1725872800006, dept: 'LOADING', date: '2026-09-09', timeOut: '13:00', timeIn: '16:00', place: 'Adda Plot', purpose: 'Maal Lene PBS', meterOut: 27297, meterIn: 27299, km: 2, driver: 'saeed', vehicle: 'CAV-8213 - Porter', model: 'Porter', remark: 'Check by Azam' },
      { id: 1725872800007, dept: 'LOADING', date: '2026-09-09', timeOut: '12:30', timeIn: '21:12', place: 'Lahore', purpose: 'Maal Chhorne', meterOut: 186638, meterIn: 186742, km: 104, driver: 'Zubair', vehicle: 'CAF-4893 - Porter', model: 'Porter', remark: 'Check by Azam' },
      { id: 1725872800008, dept: 'SALE', date: '2026-09-09', timeOut: '16:05', timeIn: '17:15', place: 'Akbari Mandi', purpose: 'Staff Drop', meterOut: 65079, meterIn: 65109, km: 30, driver: 'Masood', vehicle: 'ARQ-334 - Wagon-R', model: 'Wagon-R', remark: '' },
      { id: 1725872800009, dept: 'ADMIN', date: '2026-09-09', timeOut: '17:10', timeIn: '18:38', place: 'Akbari Mandi', purpose: 'Staff Drop', meterOut: 15338, meterIn: 15379, km: 41, driver: 'Masood', vehicle: 'BPR-980 - Caravan', model: 'Caravan', remark: '' },
      { id: 1725872800010, dept: 'LOADING', date: '2026-09-09', timeOut: '17:53', timeIn: '', place: 'Lahore', purpose: 'Staff Drop', meterOut: 40246, meterIn: 40346, km: 100, driver: 'Bilal Manzoor', vehicle: 'AVX-481 - Hino', model: 'Hino', remark: 'Check by Azam' },
      { id: 1725872800011, dept: 'LOADING', date: '2026-09-09', timeOut: '18:00', timeIn: '20:10', place: 'Township Sabzazar', purpose: 'Delivery', meterOut: 232709, meterIn: 232714, km: 5, driver: 'Tanveer Abbas', vehicle: 'LES-4605 - Hino', model: 'Hino', remark: 'Check by Azam' },
      
      { id: 1725959200001, dept: 'ADMIN', date: '2026-09-10', timeOut: '06:40', timeIn: '', place: 'Adda Plot', purpose: 'Pick Staff', meterOut: 15379, meterIn: 15446, km: 67, driver: 'Masood', vehicle: 'BPR-980 - Caravan', model: 'Caravan', remark: '' },
      { id: 1725959200002, dept: 'LOADING', date: '2026-09-10', timeOut: '09:30', timeIn: '14:30', place: 'Saggian', purpose: 'Booking Board', meterOut: 232714, meterIn: 232792, km: 78, driver: 'Tanveer Abbas', vehicle: 'LES-4605 - Hino', model: 'Hino', remark: 'Check by Azam' },
      { id: 1725959200003, dept: 'LOADING', date: '2026-09-10', timeOut: '10:47', timeIn: '', place: 'PSO', purpose: 'Oil', meterOut: 186743, meterIn: 186748, km: 5, driver: 'Ashfaq', vehicle: 'CAF-4893 - Porter', model: 'Porter', remark: 'Check by Sajjad' },
      { id: 1725959200004, dept: 'SALE', date: '2026-09-10', timeOut: '12:00', timeIn: '14:10', place: 'Raiwind', purpose: 'Pick Staff', meterOut: 65152, meterIn: 65205, km: 53, driver: 'Ashfaq', vehicle: 'ART-542 - Vehicle', model: 'Vehicle', remark: 'Check by Azam' },
      { id: 1725959200005, dept: 'SALE', date: '2026-09-10', timeOut: '12:05', timeIn: '', place: 'Lahore', purpose: 'Sale Ka Maal', meterOut: 67074, meterIn: 67116, km: 42, driver: 'Masood', vehicle: 'ARQ-965 - Vehicle', model: 'Vehicle', remark: 'Check by Azam' },
      { id: 1725959200006, dept: 'LOADING', date: '2026-09-10', timeOut: '12:25', timeIn: '18:05', place: 'Lahore', purpose: 'Market', meterOut: 186748, meterIn: 186821, km: 73, driver: 'saeed', vehicle: 'CAF-4893 - Porter', model: 'Porter', remark: 'Check by Azam' },
      { id: 1725959200007, dept: 'SALE', date: '2026-09-10', timeOut: '12:15', timeIn: '23:00', place: 'Lahore', purpose: 'Supply', meterOut: 65108, meterIn: 65211, km: 103, driver: 'Zubair', vehicle: 'ARQ-334 - Wagon-R', model: 'Wagon-R', remark: 'Check by Azam' },
      { id: 1725959200008, dept: 'LOADING', date: '2026-09-10', timeOut: '13:21', timeIn: '15:47', place: 'Kasur', purpose: 'Delivery', meterOut: 64243, meterIn: 64319, km: 76, driver: 'Qasim', vehicle: 'CAJ-6701 - Ravi', model: 'Ravi', remark: 'Check by Azam' }
    ];
    var existingIds = existing.map(function(e){ return e.id; });
    newEntries.forEach(function(ne){
      if (existingIds.indexOf(ne.id) === -1) existing.push(ne);
    });
    save(existing);
    localStorage.setItem('vfp_seeded_sept09_10_2026_v1', '1');
  })();
'''

marker = '  // ── One-time seed: handwritten log entries (Sept 07-08 2026) ──────────────────'
if marker in content:
    content_new = content.replace(marker, new_seed + '\n' + marker)
    with codecs.open(filepath, 'w', 'utf-8') as f:
        f.write(content_new)
    print("New entries seed block added")
else:
    print("Marker not found")
