import re
import codecs

filepath = r'z:\Logbok vehicles\index.html'
with codecs.open(filepath, 'r', 'utf-8') as f:
    content = f.read()

new_seed = '''  // ── One-time seed: handwritten log entries (Sept 10-12 2026) ──────────────────
  (function seedSept10_12_2026() {
    if (localStorage.getItem('vfp_seeded_sept10_12_2026_v1')) return;
    var existing = load();
    var newEntries = [
      { id: 1725959200009, dept: 'ADMIN', date: '2026-09-10', timeOut: '17:10', timeIn: '18:30', place: 'Adda Plot', purpose: 'Drop Staff', meterOut: 15446, meterIn: 15486, km: 40, driver: 'Masood', vehicle: 'BPR-980 - Caravan', model: 'Caravan', remark: 'Check by Azam' },
      { id: 1725959200010, dept: 'LOADING', date: '2026-09-10', timeOut: '11:00', timeIn: '17:40', place: 'Sundar Adda', purpose: 'Godown Shifting', meterOut: 232792, meterIn: 232873, km: 81, driver: 'Tanveer Abbas', vehicle: 'LES-4605 - Hino', model: 'Hino', remark: '' },
      { id: 1725959200011, dept: 'LOADING', date: '2026-09-10', timeOut: '07:20', timeIn: '', place: 'Lahore', purpose: 'Drop Staff', meterOut: 40346, meterIn: 40447, km: 101, driver: 'Bilal Manzoor', vehicle: 'AVX-481 - Hino', model: 'Hino', remark: 'Check by Azam' },
      
      { id: 1726045600001, dept: 'ADMIN', date: '2026-09-11', timeOut: '06:45', timeIn: '09:00', place: 'Adda Plot', purpose: 'Pick Staff', meterOut: 15486, meterIn: 15546, km: 60, driver: 'Masood', vehicle: 'BPR-980 - Caravan', model: 'Caravan', remark: 'Check by Ashfaq' },
      { id: 1726045600002, dept: 'ADMIN', date: '2026-09-11', timeOut: '08:45', timeIn: '16:43', place: 'Coca Cola Factory', purpose: 'Visit with Tahir sb', meterOut: 85515, meterIn: 85606, km: 91, driver: 'Masood', vehicle: 'AFS-612 - Bolan', model: 'Bolan', remark: 'Check by Azam' },
      { id: 1726045600003, dept: 'ADMIN', date: '2026-09-11', timeOut: '09:45', timeIn: '13:55', place: 'Lahore', purpose: 'Ali Imran, Shahbaz ke sath', meterOut: 15546, meterIn: 15592, km: 46, driver: 'Masood', vehicle: 'BPR-980 - Caravan', model: 'Caravan', remark: 'Check by Azam' },
      { id: 1726045600004, dept: 'LOADING', date: '2026-09-11', timeOut: '10:45', timeIn: '13:49', place: 'Saggian', purpose: 'Booking Board', meterOut: 232873, meterIn: 232957, km: 84, driver: 'Tanveer Abbas', vehicle: 'LES-4605 - Hino', model: 'Hino', remark: 'Check by Azam' },
      { id: 1726045600005, dept: 'ADMIN', date: '2026-09-11', timeOut: '12:45', timeIn: '19:25', place: 'Lahore', purpose: 'Market', meterOut: 215580, meterIn: 215625, km: 45, driver: 'saeed', vehicle: 'LE-3153 - Vitz', model: 'Vitz', remark: '' },
      { id: 1726045600006, dept: 'LOADING', date: '2026-09-11', timeOut: '16:40', timeIn: '17:10', place: 'Lohari', purpose: 'Packing Saman Drop', meterOut: 186821, meterIn: 186898, km: 77, driver: 'saeed', vehicle: 'CAF-4893 - Porter', model: 'Porter', remark: 'Check by Azam' },
      { id: 1726045600007, dept: 'SALE', date: '2026-09-11', timeOut: '17:05', timeIn: '18:28', place: 'Adda Plot', purpose: 'Drop Staff', meterOut: 65205, meterIn: 65213, km: 8, driver: 'Ashfaq', vehicle: 'ARQ-334 - Wagon-R', model: 'Wagon-R', remark: 'Check by Azam' },
      { id: 1726045600008, dept: 'LOADING', date: '2026-09-11', timeOut: '17:50', timeIn: '', place: 'Lahore', purpose: 'Drop Staff', meterOut: 40447, meterIn: 40548, km: 101, driver: 'Bilal Manzoor', vehicle: 'AVX-481 - Hino', model: 'Hino', remark: 'Check by Azam' },
      { id: 1726045600009, dept: 'ADMIN', date: '2026-09-11', timeOut: '17:56', timeIn: '12:10', place: 'Bahria Town', purpose: 'Ghar Saman Dene', meterOut: 167841, meterIn: 167935, km: 94, driver: 'Ashfaq', vehicle: 'LEB-5449 - Yaris', model: 'Yaris', remark: 'Check by Azam' },
      { id: 1726045600010, dept: 'ADMIN', date: '2026-09-11', timeOut: '19:45', timeIn: '20:50', place: 'Adda Plot', purpose: 'Drop Staff', meterOut: 324632, meterIn: 324662, km: 30, driver: 'Bilal Manzoor', vehicle: 'LEA-6860 - Toyota GLI', model: 'Toyota GLI', remark: 'Check by Azam' },
      { id: 1726045600011, dept: 'LOADING', date: '2026-09-11', timeOut: '20:00', timeIn: '00:15', place: 'Data Sahab', purpose: 'Pick Staff', meterOut: 232957, meterIn: 232997, km: 40, driver: 'Tanveer Abbas', vehicle: 'LES-4605 - Hino', model: 'Hino', remark: '' },

      { id: 1726132000001, dept: 'ADMIN', date: '2026-09-12', timeOut: '06:40', timeIn: '09:00', place: 'Adda Plot', purpose: 'Pick Staff', meterOut: 15592, meterIn: 15658, km: 66, driver: 'Masood', vehicle: 'BPR-980 - Caravan', model: 'Caravan', remark: '' },
      { id: 1726132000002, dept: 'LOADING', date: '2026-09-12', timeOut: '07:10', timeIn: '10:25', place: 'Kasur', purpose: 'Faisal Salesman', meterOut: 232997, meterIn: 233050, km: 53, driver: 'Tanveer Abbas', vehicle: 'LES-4605 - Hino', model: 'Hino', remark: 'Check by Azam' },
      { id: 1726132000003, dept: 'LOADING', date: '2026-09-12', timeOut: '09:47', timeIn: '10:22', place: 'PSO', purpose: 'Oil', meterOut: 40548, meterIn: 40553, km: 5, driver: 'Bilal Manzoor', vehicle: 'AVX-481 - Hino', model: 'Hino', remark: 'Check by Azam' },
      { id: 1726132000004, dept: 'ADMIN', date: '2026-09-12', timeOut: '09:47', timeIn: '10:00', place: 'PSO', purpose: 'Oil', meterOut: 15658, meterIn: 15663, km: 5, driver: 'Masood', vehicle: 'BPR-980 - Caravan', model: 'Caravan', remark: 'Check by Azam' },
      { id: 1726132000005, dept: 'LOADING', date: '2026-09-12', timeOut: '12:25', timeIn: '18:05', place: 'Lahore', purpose: 'Market', meterOut: 186898, meterIn: 187126, km: 228, driver: 'saeed', vehicle: 'CAF-4893 - Porter', model: 'Porter', remark: 'Check by Azam' },
      { id: 1726132000006, dept: 'ADMIN', date: '2026-09-12', timeOut: '12:15', timeIn: '23:00', place: 'Lahore', purpose: 'Supply Delivery', meterOut: 167935, meterIn: 168013, km: 78, driver: 'Ashfaq', vehicle: 'LEB-5449 - Yaris', model: 'Yaris', remark: 'Check by Azam' },
      { id: 1726132000007, dept: 'LOADING', date: '2026-09-12', timeOut: '11:40', timeIn: '', place: 'Lahore', purpose: 'Wapda Town Maal Dene', meterOut: 64319, meterIn: 64491, km: 172, driver: 'Qasim', vehicle: 'CAJ-6701 - Ravi', model: 'Ravi', remark: 'Check by Azam' }
    ];
    var existingIds = existing.map(function(e){ return e.id; });
    newEntries.forEach(function(ne){
      if (existingIds.indexOf(ne.id) === -1) existing.push(ne);
    });
    save(existing);
    localStorage.setItem('vfp_seeded_sept10_12_2026_v1', '1');
  })();
'''

marker = '  // ── One-time seed: handwritten log entries (Sept 09-10 2026) ──────────────────'
if marker in content:
    content_new = content.replace(marker, new_seed + '\n' + marker)
    with codecs.open(filepath, 'w', 'utf-8') as f:
        f.write(content_new)
    print("New entries seed block added")
else:
    print("Marker not found")
