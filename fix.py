import re
import codecs

filepath = r'z:\Logbok vehicles\index.html'
with codecs.open(filepath, 'r', 'utf-8') as f:
    content = f.read()

# Let's fix the duplicated stuff at the end of the file.
# The proper end of the file should just be:
correct_tail = '''
  renderTable();
  updateStats();
  populateDriverDropdown();
  renderFleetRegistryTable();
  updateVehicleSelectDropdown();
  // Mark "All Drivers" active on load
  var _initDA = document.getElementById('nav-driver-all');
  if (_initDA) _initDA.classList.add('active');

</script>
</body>
</html>
'''

# Find the block ending line
idx = content.rfind('  // ── One-time seed: handwritten log entries (Sept 03 2026) ──────────────────')
if idx != -1:
    # Now find the first </script> after that
    script_end = content.find('</script>', idx)
    if script_end != -1:
        # We need to extract just the seed block and correctly append the tail
        # The seed block ends with   })();\n  // ────...
        seed_end = content.find('  })();', idx)
        if seed_end != -1:
            line_end = content.find('\n', seed_end + 10)
            line_end2 = content.find('\n', line_end + 1) # to skip the ─── line
            
            clean_content = content[:line_end2] + '\n' + correct_tail
            
            with codecs.open(filepath, 'w', 'utf-8') as f:
                f.write(clean_content)
            print("Fixed syntax")
        else:
            print("Could not find seed_end")
    else:
        print("Could not find script_end")
else:
    print("Could not find start")
