import re
import codecs

filepath = r'z:\Logbok vehicles\index.html'
with codecs.open(filepath, 'r', 'utf-8') as f:
    content = f.read()

new_seed = '''  // ── One-time seed: handwritten log entries (Sept 07-08 2026) ──────────────────
  (function seedSept07_08_2026() {
    if (localStorage.getItem('vfp_seeded_sept07_08_2026_v1')) return;
    var existing = load();
    var newEntries = [
      { id: 1725700000001, dept: 'SALE', date: '2026-09-07', timeOut: '13:30', timeIn: '17:35', place: 'Bahria Coca Cola Road', purpose: 'Drop Tahir sb', meterOut: 41876, meterIn: 41968, km: 92, driver: 'Usama', vehicle: 'ARQ-526 - Wagon-R', model: 'Wagon-R', remark: 'Check by Azam' },
      { id: 1725700000002, dept: 'ADMIN', date: '2026-09-07', timeOut: '17:01', timeIn: '18:00', place: 'Adda Plot', purpose: 'Drop Goods', meterOut: 15014, meterIn: 15054, km: 40, driver: 'Masood', vehicle: 'BPR-980 - Caravan', model: 'Caravan', remark: 'Check by Azam' },
      
      { id: 1725786400001, dept: 'ADMIN', date: '2026-09-08', timeOut: '06:45', timeIn: '08:45', place: 'Ichra Plaza', purpose: 'Pick Staff', meterOut: 15054, meterIn: 15121, km: 67, driver: 'Masood', vehicle: 'BPR-980 - Caravan', model: 'Caravan', remark: '' },
      { id: 1725786400002, dept: 'ADMIN', date: '2026-09-08', timeOut: '07:25', timeIn: '09:00', place: 'Lahore', purpose: 'Pick Tahir sb', meterOut: 167650, meterIn: 167716, km: 66, driver: 'Ashfaq', vehicle: 'LEB-5449 - Yaris', model: 'Yaris', remark: 'Check by Azam' },
      { id: 1725786400003, dept: 'SALE', date: '2026-09-08', timeOut: '09:31', timeIn: '10:26', place: 'Tibb City', purpose: 'Booking Board', meterOut: 64888, meterIn: 65074, km: 186, driver: 'Asad Saleem', vehicle: 'ARQ-334 - Wagon-R', model: 'Wagon-R', remark: 'Check by Azam' },
      { id: 1725786400004, dept: 'ADMIN', date: '2026-09-08', timeOut: '10:50', timeIn: '19:10', place: 'Lhr Kot Abdul Malik + Muridke', purpose: 'Ali Imran + Nasir Shahab', meterOut: 15121, meterIn: 15215, km: 94, driver: 'Usama', vehicle: 'BPR-980 - Caravan', model: 'Caravan', remark: 'Check by Azam' },
      { id: 1725786400005, dept: 'LOADING', date: '2026-09-08', timeOut: '11:03', timeIn: '14:00', place: 'Lahore Kalma Chowk', purpose: 'Sales Officer', meterOut: 64225, meterIn: 64243, km: 18, driver: 'Masood', vehicle: 'CAJ-6701 - Ravi', model: 'Ravi', remark: 'Check by Azam' },
      { id: 1725786400006, dept: 'LOADING', date: '2026-09-08', timeOut: '11:40', timeIn: '19:00', place: 'Lahore', purpose: 'Market', meterOut: 186466, meterIn: 186598, km: 132, driver: 'saeed', vehicle: 'CAF-4893 - Porter', model: 'Porter', remark: 'Check by Azam' },
      { id: 1725786400007, dept: 'LOADING', date: '2026-09-08', timeOut: '12:15', timeIn: '17:50', place: 'Nizamabad Sundar', purpose: 'Pick Goods', meterOut: 27237, meterIn: 27292, km: 55, driver: 'Zubair', vehicle: 'CAV-8213 - Porter', model: 'Porter', remark: 'Check by Azam' },
      { id: 1725786400008, dept: 'LOADING', date: '2026-09-08', timeOut: '12:00', timeIn: '12:18', place: 'PSO', purpose: 'Oil', meterOut: 40139, meterIn: 40144, km: 5, driver: 'Bilal Manzoor', vehicle: 'AVX-481 - Hino', model: 'Hino', remark: 'Check by Azam' },
      { id: 1725786400009, dept: 'LOADING', date: '2026-09-08', timeOut: '12:23', timeIn: '14:11', place: 'Bhatta Chowk Lace', purpose: 'Adda Maal', meterOut: 232540, meterIn: 232618, km: 78, driver: 'Zubair', vehicle: 'LES-4605 - Hino', model: 'Hino', remark: 'Check by Azam' },
      { id: 1725786400010, dept: 'SALE', date: '2026-09-08', timeOut: '13:36', timeIn: '15:36', place: 'Saggian', purpose: 'With Tahir sb', meterOut: 41968, meterIn: 41985, km: 17, driver: 'Ashfaq', vehicle: 'ARQ-526 - Wagon-R', model: 'Wagon-R', remark: 'Check by Azam' },
      { id: 1725786400011, dept: 'LOADING', date: '2026-09-08', timeOut: '14:18', timeIn: '15:50', place: 'Wapda Town', purpose: 'Pick Goods', meterOut: 232618, meterIn: 232632, km: 14, driver: 'Tanveer Abbas', vehicle: 'LES-4605 - Hino', model: 'Hino', remark: 'Check by Sajjad' },
      { id: 1725786400012, dept: 'ADMIN', date: '2026-09-08', timeOut: '14:30', timeIn: '15:30', place: 'Defense', purpose: 'Pick Goods', meterOut: 215570, meterIn: 215580, km: 10, driver: 'Zubair', vehicle: 'LE-3153 - Vitz', model: 'Vitz', remark: 'Check by Azam' },
      { id: 1725786400013, dept: 'ADMIN', date: '2026-09-08', timeOut: '17:18', timeIn: '18:40', place: 'Adda Plot', purpose: 'Drop Staff', meterOut: 15215, meterIn: 15262, km: 47, driver: 'Usama', vehicle: 'BPR-980 - Caravan', model: 'Caravan', remark: 'Check by Azam' },
      { id: 1725786400014, dept: 'LOADING', date: '2026-09-08', timeOut: '18:00', timeIn: '09:56', place: 'Lahore', purpose: 'Drop Staff', meterOut: 40144, meterIn: 40246, km: 102, driver: 'Bilal Manzoor', vehicle: 'AVX-481 - Hino', model: 'Hino', remark: 'Check by Azam' },
      { id: 1725786400015, dept: 'ADMIN', date: '2026-09-08', timeOut: '18:20', timeIn: '20:45', place: 'Lahore', purpose: 'Drop Ramzan Supply', meterOut: 167716, meterIn: 167791, km: 75, driver: 'Ashfaq', vehicle: 'LEB-5449 - Yaris', model: 'Yaris', remark: 'Check by Azam' },
      { id: 1725786400016, dept: 'ADMIN', date: '2026-09-08', timeOut: '21:50', timeIn: '23:40', place: 'Sundar Industrial Estate', purpose: 'Drop Akbar sb', meterOut: 167791, meterIn: 167841, km: 50, driver: 'Ashfaq', vehicle: 'LEB-5449 - Yaris', model: 'Yaris', remark: '' }
    ];
    var existingIds = existing.map(function(e){ return e.id; });
    newEntries.forEach(function(ne){
      if (existingIds.indexOf(ne.id) === -1) existing.push(ne);
    });
    save(existing);
    localStorage.setItem('vfp_seeded_sept07_08_2026_v1', '1');
  })();
'''

marker = '  // ── One-time seed: handwritten log entries (Sept 05-07 2026) ──────────────────'
if marker in content:
    content_new = content.replace(marker, new_seed + '\n' + marker)
    with codecs.open(filepath, 'w', 'utf-8') as f:
        f.write(content_new)
    print("New entries seed block added")
else:
    print("Marker not found")
